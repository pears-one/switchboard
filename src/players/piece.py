from board.tile_position import TilePosition
from spots.spot_positions import SpotPositionFactory
from players.piece_position import PiecePosition
__stp = TilePosition(1, 1)
__ssp = SpotPositionFactory.get_by_id(0)
STARTING_POSITION = PiecePosition(__stp, __ssp)


class Piece:
    def __init__(self, piece_colour, position: PiecePosition = STARTING_POSITION):
        self.__piece_colour = piece_colour
        self.__piece_position = position

    def get_piece_colour(self):
        return self.__piece_colour

    def __str__(self):
        return self.__piece_colour

    def get_piece_position(self):
        return self.__piece_position

    def move(self, new_position: PiecePosition):
        self.__piece_position = new_position

    def marshal(self):
        return {
            "colour": self.__piece_colour,
            "position": self.__piece_position.marshal()
        }
