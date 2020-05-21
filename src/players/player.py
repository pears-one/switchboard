from players.piece import Piece
from config.constants import GREEN
from board.tile_position import TilePosition
from spots.spot_positions import SpotPositionFactory
import json


class Player:
    def __init__(self, name: str, cookie: str, piece: Piece, missing_next_turn):
        self.__piece = piece
        self.__missing_next_turn = missing_next_turn
        self.__name = name
        self.__cookie = cookie

    def get_cookie(self):
        return self.__cookie

    def get_name(self):
        return self.__name

    def toggle_missing_next_turn(self):
        self.__missing_next_turn = not self.__missing_next_turn

    def is_missing_next_turn(self):
        return self.__missing_next_turn

    def has_another_go(self):
        return self.__piece.is_on(GREEN)

    def get_position(self):
        return self.__piece.get_piece_position()

    def __str__(self):
        return "Hey! I'm " + self.get_name()


def get_players_from_config(filename):
    with open(filename) as file:
        player_json = json.load(file)
        player_list = player_json["players"]

    player_objects = []
    for colour, player in enumerate(player_list):
        pos = player["position"]
        tile_position = TilePosition(pos[0], pos[1])
        spot_position = SpotPositionFactory.get_by_id(pos[2])
        piece = Piece(colour, tile_position, spot_position)
        player_objects.append(Player(player["name"], player["cookie"], piece, False))

    return player_objects

