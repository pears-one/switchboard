import json
from exceptions import MoveError
from tile_position import TilePosition
from copy import deepcopy
from tile_repo import TileRepo
from tile_id import TileID
from tiles import RotatedTile


class Board:
    def __init__(self, tile_dictionary):
        self.__tile_dictionary = tile_dictionary

    @staticmethod
    def from_config(filename, tile_repo: TileRepo):
        with open(filename) as config:
            config = json.load(config)
            board_config = config["board"]
        tile_dictionary = dict()
        for tile_config in board_config:
            pos = TilePosition(*tile_config[0:2])
            tile_id = TileID(*tile_config[2:4])
            spot_list = tile_repo.get_tile(tile_id).get_spot_list()
            tile_dictionary[tuple(pos)] = RotatedTile(spot_list, tile_config[4])
        return Board(tile_dictionary)

    def get_tile_at(self, pos: TilePosition) -> RotatedTile:
        pos = tuple(pos)
        if pos in self.__tile_dictionary:
            return self.__tile_dictionary[tuple(pos)]
        return None

    def get_tile_positions(self):
        return [TilePosition.from_tuple(key) for key in self.__tile_dictionary.keys()]

    def move_tile(self, from_pos, to_pos, rotation):
        if from_pos not in self.get_tile_positions() or to_pos in self.get_tile_positions():
            raise MoveError

        new_tile_dict = deepcopy(self.__tile_dictionary)
        tile_to_move = self.get_tile_at(from_pos)
        new_tile_dict[tuple(to_pos)] = RotatedTile(tile_to_move, rotation)
        del new_tile_dict[tuple(from_pos)]

        return Board(new_tile_dict)

    def get_tile(self, direction, pos: TilePosition) -> RotatedTile:
        pos = pos.get_position(direction)
        return self.get_tile_at(pos)

