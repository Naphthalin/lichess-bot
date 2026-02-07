"""Shared backendserver for Leela Odds Bots."""
import argparse
import asyncio
import chess
import concurrent.futures
from lib import engine_wrapper
import logging
import itertools
import json
import os
import time
from typing import override
from lib.config import load_config, Configuration
from lib.lichess_bot import logging_configurer, intro, set_auto_log_directory
from lib.lichess import stop

logger = logging.getLogger(__name__)
    
if os.sys.platform == "win32":
    import msvcrt
    def flock_sys(file):
        msvcrt.locking(file.fileno(), msvcrt.LK_NBLCK, 1)
    def funlock_sys(file):
        msvcrt.locking(file.fileno(), msvcrt.LK_UNLCK, 1)
else:
    import fcntl
    def flock_sys(file):
        fcntl.flock(file.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
    def funlock_sys(file):
        fcntl.flock(file.fileno(), fcntl.LOCK_UN)

class FileLock:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, 'w')
        flock_sys(self.file)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        funlock_sys(self.file)
        self.file.close()

def read_info(engine, keepalive_interval) -> chess.engine.AnalysisResult:
    class ServerWatchingCommand(chess.engine.BaseCommand[chess.engine.AnalysisResult]):
        def __init__(self, engine: chess.engine.UciProtocol):
            super().__init__(engine)
            self.protocol = engine
            self.sent_isready = False

        def start(self) -> None:
            self.analysis = chess.engine.AnalysisResult(stop=lambda: self.cancel())
            self.result.set_result(self.analysis)
            coro = self._keepalive_loop()
            self.keepalive_task = asyncio.run_coroutine_threadsafe(coro, self.protocol.loop)

        async def _keepalive_loop(self) -> None:
            try:
                logger.info("%s: Starting keepalive loop with interval %s", self.protocol, keepalive_interval)
                while not stop.terminated:
                    await asyncio.sleep(keepalive_interval)
                    if stop.terminated:
                        self.cancel()
                        break
                    if self.sent_isready or stop.terminated:
                        logger.error("%s: Server not responding. Trying to restart.", self.protocol)
                        self.cancel()
                        break
                    self.sent_isready = True
                    self.protocol._isready()
            except Exception as e:
                logger.error("%s: Keepalive loop error: %s", self.protocol, e)
                self.analysis.set_exception(e)

        @override
        def line_received(self, line: str) -> None:
            token, remaining = chess.engine._next_token(line)
            if token == "info":
                self._info(remaining)
            elif token == "readyok":
                self._readyok()
            else:
                logger.warning("%s: Unexpected line: %s", self.protocol, line)

        def _readyok(self) -> None:
            self.sent_isready = False
            logger.debug("%s: Engine is ready.", self.protocol)

        def _info(self, line: str) -> None:
            self.analysis.post(chess.engine._parse_uci_info(line, None))

        @override
        def cancel(self) -> None:
            engine.engine.close()

        @override
        def engine_terminated(self, exc: Exception) -> None:
            logger.debug("%s: Engine terminated: %s", self.protocol, exc)
            if not self.result.done():
                self.result.set_exception(exc)

    with engine.engine._not_shut_down():
        coro = engine.engine.protocol.communicate(ServerWatchingCommand)
        future = asyncio.run_coroutine_threadsafe(coro, engine.engine.protocol.loop)
    return chess.engine.SimpleAnalysisResult(engine.engine, future.result())

def run_server(CONFIG):
    with engine_wrapper.create_engine(CONFIG) as engine:
        logging.info(f"Starting Leela Odds Bots backendserver {engine.engine}")
        keepalive_interval = 4.0
        with read_info(engine, keepalive_interval) as analysis:
            try:
                for info in analysis:
                    logger.debug(f"Engine info: {info}")
            except asyncio.CancelledError as e:
                logger.info("Engine watching cancelled: %s", e)

def main():
    parser = argparse.ArgumentParser(description="Shared backendserver for Leela Odds Bots")
    parser.add_argument("-v", action="store_true", help="Make output more verbose. Include all communication with lichess.")
    parser.add_argument("--config", help="Specify a configuration file (defaults ./server.yml).")
    parser.add_argument("-l", "--logfile", help="Record all console output to a log file.", default=None)
    parser.add_argument("--disable_auto_logging", action="store_true", help="Disable automatic logging.")
    args = parser.parse_args()

    set_auto_log_directory("leela_backendserver_auto_logs")

    logging_level = logging.DEBUG if args.v else logging.INFO
    logging_configurer(logging_level, args.logfile, args.disable_auto_logging)
    logger.info(intro(), extra={"highlighter": None})

    CONFIG = load_config(args.config or "./server.yml")

    failures = 0
    last_failure_time = time.monotonic()
    failure_time_limit = 60.0

    with FileLock(CONFIG.server_lock_file):

        while not stop.terminated:
            try:
                run_server(CONFIG)
            except Exception as e:
                if stop.terminated:
                    break
                logger.error(f"Error in backendserver: {e}\n", exc_info=True)
                now = time.monotonic()
                if now - last_failure_time > failure_time_limit:
                    failures = 0
                failures += 1
                last_failure_time = now
                if failures >= 5:
                    logger.critical("Too many failures in a short time, exiting.")
                    break

if __name__ == "__main__":
    main()
