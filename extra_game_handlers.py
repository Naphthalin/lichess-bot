"""Functions for the user to implement when the config file is not adequate to express bot requirements."""
from lib import model
from lib.lichess_types import OPTIONS_TYPE
import json
import re

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
    initial_fen = challenge.initial_fen if (challenge.variant == "fromPosition" or challenge.variant == "chess960") else "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    found_position = extract_fenlist(initial_fen, challenge.color)[0]
    return found_position


def extract_fenlist(initial_fen, color):
    """
    Extract the 'fenlist.json' file, looking for an entry matching the initial fen and color.
    """
    found_position = False
    uci_override = {}
    go_options = {}
    missing_pieces, color_fullrank = missing_pieces_in_FEN(initial_fen)
    with open('fenlist.json') as f:
        for position in json.load(f)["accepted_positions"]:
            if initial_fen.startswith(position["fen"]) and color == position["color"]:
                found_position = True
                uci_override = position["uci_options"] if "uci_options" in position.keys() else {}
                go_options = position["go_options"]if "go_options" in position.keys() else {}
                break
            if position["fen"] == "FRC":
                if sorted(missing_pieces) == sorted(position["odds"]) and color == position["color"] and color == color_fullrank:
                    found_position = True
                    uci_override = position["uci_options"] if "uci_options" in position.keys() else {}
                    go_options = position["go_options"]if "go_options" in position.keys() else {}

    return found_position, uci_override, go_options

def missing_pieces_in_FEN(initial_fen):
    deny = False
    position, color, castling = initial_fen.split(" ")[:3]
    rows = position.split("/")
    if (rows[1] != 8*"p") or (rows[6] != 8*"P"):
        deny = True
    if any(row != "8" for row in rows[2:6]):
        deny = True
    backrank_white = rows[7].replace("2", "11").replace("3", "111").replace("4", "1111").replace("5", 5*"1").replace("6", 6*"1").replace("7", 7*"1")
    backrank_black = rows[0].replace("2", "11").replace("3", "111").replace("4", "1111").replace("5", 5*"1").replace("6", 6*"1").replace("7", 7*"1")

    # check for king between rooks
    if backrank_white.count("R") == 2:
        if not re.search(r"R.*K.*R", backrank_white):
            deny = True
    if backrank_black.count("r") == 2:
        if not re.search(r"r.*k.*r", backrank_black):
            deny = True
    # check for equal number of squares between bishops
    if backrank_white.count("B") == 2:
        if not re.search(r"B(..)*B", backrank_white):
            deny = True
    if backrank_black.count("b") == 2:
        if not re.search(r"b(..)*b", backrank_black):
            deny = True
    # check for full castling rights
    if backrank_white.count("R") != len(re.sub(r"[^A-Z]*", "", castling)):
        deny = True
    if backrank_black.count("r") != len(re.sub(r"[^a-z]*", "", castling)):
        deny = True

    # compare whether black and white have the same setup
    color_fullrank = None
    missing_pieces = ""

    if sum([backrank_white.count(piece) for piece in ["K", "Q", "R", "B", "N"]]) == 8:
        color_fullrank = "white"
    if sum([backrank_black.count(piece) for piece in ["k", "q", "r", "b", "n"]]) == 8:
        color_fullrank = "black"

    if color_fullrank not in ["white", "black"]:
        deny = True
    else:
        for index in range(8):
            white_piece = backrank_white[index]
            black_piece = backrank_black[index]
            if color_fullrank == "white":
                if black_piece == "1":
                    missing_pieces += white_piece.lower()
                elif black_piece.upper() != white_piece:
                    deny = True
            if color_fullrank == "black":
                if white_piece == "1":
                    missing_pieces += black_piece.upper()
                elif white_piece.lower() != black_piece:
                    deny = True
    return missing_pieces if not deny else "", color_fullrank
