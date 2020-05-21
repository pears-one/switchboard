import json
from tiles.tiles import Tile
from tiles.tile_id import TileID


class TileRepo:
    def __init__(self, tile_dict):
        self.__tile_dict = tile_dict

    def get_tile(self, tile_id: TileID) -> Tile:
        return self.__tile_dict[tuple(tile_id)]

    @classmethod
    def get_repo_from_config(cls, filename):
        with open(filename) as config:
            tile_list = json.load(config)["tiles"]
        tile_dictionary = dict()
        for tile in tile_list:
            x = tile[0]
            y = tile[1]
            tile_dictionary[(x, y)] = Tile.from_config_list(tile)
        return cls(tile_dictionary)


