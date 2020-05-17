from players.piece import Piece
from config.constants import GREEN


class Player:
    def __init__(self, piece: Piece, missing_next_turn):
        self.__piece = piece
        self.__missing_next_turn = missing_next_turn

    def toggle_missing_next_turn(self):
        self.__missing_next_turn = not self.__missing_next_turn

    def is_missing_next_turn(self):
        return self.__missing_next_turn

    def has_another_go(self):
        return self.__piece.is_on(GREEN)
