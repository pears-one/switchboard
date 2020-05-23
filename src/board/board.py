import json
from exceptions import MoveError
from board.tile_position import TilePosition
from copy import deepcopy
from analysis.tile_repo import TileRepo
from tiles.tile_id import TileID
from tiles.tiles import RotatedTile
from config.constants import opposite
from moves.tile_move import TileMove
from players.piece_position import PiecePosition


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
            tile_dictionary[tuple(pos)] = RotatedTile(tile_id, spot_list, tile_config[4])
        return Board(tile_dictionary)

    def get_tile_at(self, pos: TilePosition) -> RotatedTile:
        pos = tuple(pos)
        if pos in self.__tile_dictionary:
            return self.__tile_dictionary[tuple(pos)]
        return None

    def get_tile_positions(self):
        return [TilePosition.from_tuple(key) for key in self.__tile_dictionary.keys()]

    def move_tile(self, tile_move: TileMove):
        new_tile_dict = deepcopy(self.__tile_dictionary)
        tile_to_move = self.get_tile_at(tile_move.get_from_pos())
        del new_tile_dict[tuple(tile_move.get_from_pos())]
        new_tile_dict[tuple(tile_move.get_to_pos())] = RotatedTile.from_tile(tile_to_move, tile_move.get_rotation())
        return Board(new_tile_dict)

    def get_tile(self, direction, pos: TilePosition) -> RotatedTile:
        pos = pos.get_position_in_direction(direction)
        return self.get_tile_at(pos)

    def is_connection_from(self, from_position: TilePosition, direction):
        to_position = from_position.get_position_in_direction(direction)
        from_tile, to_tile = self.get_tile_at(from_position), self.get_tile_at(to_position)
        return from_tile.is_accessible_from(direction) \
            and to_tile is not None \
            and to_tile.is_accessible_from(opposite(direction))

    def get_tile_count(self):
        return len(self.get_tile_positions())

    def get_spot_at_piece_position(self, position: PiecePosition):
        tile = self.get_tile_at(position.get_tile_position())
        return tile.get_spot_at_position(position.get_spot_position())


