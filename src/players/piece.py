from board.tile_position import TilePosition
from spots.spot_positions import SpotPosition


class Piece:
    def __init__(self, piece_colour, tile_position: TilePosition, spot: SpotPosition):
        self.__piece_colour = piece_colour
        self.__tile_position = tile_position
        self.__spot = spot

    def get_piece_colour(self):
        return self.__piece_colour

    def __str__(self):
        return self.__piece_colour

    def get_piece_position(self):
        return self.__tile_position, self.__spot

    def is_on(self, colour):
        return self.__spot.get_colour() == colour
