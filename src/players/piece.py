from players.piece_position import PiecePosition


class Piece:
    def __init__(self, piece_colour, position: PiecePosition):
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
