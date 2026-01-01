"""Functions for the user to implement when the config file is not adequate to express bot requirements."""
from lib import model
from lib.lichess_types import OPTIONS_TYPE
import json


def game_specific_options(game: model.Game) -> OPTIONS_TYPE:  # noqa: ARG001
    """
    Return a dictionary of engine options based on game aspects.

    By default, an empty dict is returned so that the options in the configuration file are used.
    """
    found_position, uci_override, go_options = extract_fenlist(game.initial_fen, game.opponent_color)
    if found_position:
        return {"uci": uci_override, "go": go_options}
    else:
        return {}


def is_supported_extra(challenge: model.Challenge) -> bool:  # noqa: ARG001
    """
    Determine whether to accept a challenge.

    By default, True is always returned so that there are no extra restrictions beyond those in the config file.
    """
    initial_fen = challenge.initial_fen if challenge.variant == "fromPosition" else "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    found_position = extract_fenlist(initial_fen, challenge.color)[0]
    return found_position


def extract_fenlist(initial_fen, color):
    """
    Extract the 'fenlist.json' file, looking for an entry matching the initial fen and color.
    """
    found_position = False
    uci_override = {}
    go_options = {}
    with open('fenlist.json') as f:
        for position in json.load(f)["accepted_positions"]:
            if initial_fen.startswith(position["fen"]) and color == position["color"]:
                found_position = True
                uci_override = position["uci_options"] if "uci_options" in position.keys() else {}
                go_options = position["go_options"]if "go_options" in position.keys() else {}
    return found_position, uci_override, go_options