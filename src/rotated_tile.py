from tile import Tile


class RotatedTile:
    def __init__(self, tile: Tile, rotation):
        self.__tile = tile
        self.__rotation = rotation

    def is_accessible_from(self, direction):
        return self.__tile.is_accessible_from(direction, self.__rotation)

    def get_underlying_tile(self):
        return self.__tile

