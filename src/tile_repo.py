import json
from tile import Tile

class TileRepo:
    def __init__(self, tiles):
        self.__tiles = tiles

    def get_tile(self, x, y):
        return self.__tiles[6*(y-1)+(x-1)]

    def get_repo_from_config(filename):
        with open(filename) as config:
            tile_dict = json.load(config)
            return TileRepo([Tile(*tile) for tile in tile_dict["tiles"]])

