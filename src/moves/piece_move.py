from players.piece_position import PiecePosition


class PieceMove:
    def __init__(self, from_position: PiecePosition, to_position: PiecePosition):
        self.__from = from_position
        self.__to = to_position

    def get_from_position(self):
        return self.__from

    def get_to_position(self):
        return self.__to
