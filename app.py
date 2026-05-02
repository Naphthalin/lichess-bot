"""Simple web server for verbose move stats. It allows local browser extension
access to bot generated json files.

To run it use `python3 -m flask run`
"""
import flask
from flask_cors import CORS
from lib.config import load_config, Configuration

CONFIG = load_config("./config.yml")

engine = CONFIG.engine

if engine is None:
    raise Exception("No engine specified in config.yml")

move_stats = engine.move_stats

if move_stats is None:
    raise Exception("No move_stats specified in config.yml")

verbose_path = move_stats.verbose_path

if verbose_path is None:
    raise Exception("No verbose_path specified in config.yml")

app = flask.Flask(__name__, static_folder=verbose_path, static_url_path='/')
cors = CORS(app, resources={r"/*": {"origins": "*"}})
