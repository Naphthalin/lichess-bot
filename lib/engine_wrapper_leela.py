import chess
import chess.engine
import logging
import json
from lib import model
from lib.config import Configuration
from lib.lichess_types import MOVE
import os
from typing import Any

logger = logging.getLogger(__name__)


def leela_init_engine_wrapper(wrapper) -> None:
        wrapper.verbose_stats = None
        wrapper.multipv = None
        wrapper.drawscore = None

def leela_search(wrapper, board: chess.Board, time_limit: chess.engine.Limit, ponder: bool, draw_offered: bool,
           root_moves: MOVE) -> chess.engine.PlayResult:
    """Override search to add multi_pv and verbose stats parsing for UCI engines."""
    def next_token(line: str) -> tuple[str, str]:
        r = line.split(maxsplit=1)
        return r[0] if r else "", r[1] if len(r) == 2 else ""

    def parse_verbose_move_stats(side: int, move: chess.Move, line: str) -> dict[str, Any]:
        stats = {"move": move}
        unknown = "-.-"
        keys = {
                'N:': "visits",
                '(WL:': "winlose",
                '(D:': "draw",
                '(P:': "policy",
                '(O:': "offset",
                '(UM:': "moves_utility",
                '(M:': "moves_left",
                }
        while line:
            token, line = next_token(line)
            try:
                key = keys.get(token, None)
                if key is None:
                    continue
                value, line = next_token(line)
                if value.startswith(unknown):
                    continue
                stats[key] = float(value.rstrip("%)"))
            except ValueError:
                logger.warning(f"Failed to parse verbose move stats token: {token}, line: {line}")
        if side > 0:
            return stats

        for index in last_info:
            info = last_info[index]
            pv = info.get('pv', [])
            if pv[0] == move:
                stats["pv"] = board.variation_san(pv)
                break

        return stats

    time_limit = wrapper.add_go_commands(time_limit)
    bestmove = None
    with wrapper.engine.analysis(board,
                              time_limit,
                              multipv=wrapper.multipv,
                              info=chess.engine.INFO_ALL,
                              root_moves=root_moves if isinstance(root_moves, list) else None) as analyse:
        last_info = {}
        verbose_stats = [[], []]

        side = 0
        for line in analyse:
            if line.get("depth") is not None:
                multipv = line.get("multipv", 1)
                last_info[multipv - 1] = line
            elif line.get("string") is not None:
                verbose = line.get("string")
                str_move, str_stats = next_token(verbose)
                if str_move == "node":
                    continue
                if str_move == "Best:":
                    board.push(board.parse_uci(str_stats))
                    side = 1
                    continue
                move = board.parse_uci(str_move)
                verbose_stats[side].append(parse_verbose_move_stats(side, move, str_stats))
        if side == 1:
            board.pop()
        bestmove = analyse.wait()
    result = chess.engine.PlayResult(bestmove.move, bestmove.ponder, last_info.get(0, {}))
    # Use null_score to have no effect on draw/resign decisions
    null_score = chess.engine.PovScore(chess.engine.Mate(1), board.turn)
    wrapper.scores.append(result.info.get("score", null_score))
    wrapper.verbose_stats = verbose_stats
    return wrapper.offer_draw_or_resign(result, board)

def leela_store_verbose_move_stats(wrapper,
                                   engine_cfg: Configuration,
                                   game: model.Game,
                                   results: chess.engine.PlayResult,
                                   board: chess.Board) -> None:
    """Store verbose move stats to json file."""

    if wrapper.verbose_stats is None:
        return

    stats = wrapper.verbose_stats
    wrapper.verbose_stats = None

    move_cfg = engine_cfg.move_stats
    logger.debug(f"{move_cfg}, {move_cfg.verbose_path if move_cfg else None}")
    if engine_cfg.move_stats is None or move_cfg.verbose_path is None:
        return

    game_id = game.id
    bot_name = game.me.name
    if bot_name is None or game_id is None:
        logger.warning("Cannot store move stats because bot name or game id is None.")
        return
    if len(stats[0]) == 0:
        logger.info("No move stats to store. Is VerboseMoveStats UCI option enabled?")
        return
    stats_dir = os.path.join(move_cfg.verbose_path, bot_name)
    os.makedirs(stats_dir, exist_ok=True)
    filename = os.path.join(stats_dir, f"{game_id}.json")
    all_stats = {}
    if wrapper.drawscore:
        all_stats["drawscore"] = wrapper.drawscore
    if os.path.exists(filename):
        with open(filename, "r") as f:
            try:
                all_stats = json.load(f)
            except json.JSONDecodeError:
                logger.warning(f"Failed to decode existing move stats json file: {filename}. Overwriting with new stats.")
    move_number = board.ply()
    for s in stats[0]:
        s["move"] = board.san(s.get("move"))
    stats[0].reverse()
    all_stats[str(move_number)] = stats[0]
    if len(stats[1]) > 0:
        board.push(results.move)
        for s in stats[1]:
            s["move"] = board.san(s.get("move"))
        stats[1].reverse()
        all_stats[str(move_number + 1)] = stats[1]
        board.pop()

    with open(filename, "w") as f:
        json.dump(all_stats, f, indent=4)
