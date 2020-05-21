from moves.piece_move import PieceMove
from moves.tile_move import TileMove
from players.player import Player


class MoveMaker:
    def __init__(self, player, board):
        self.__player = player
        self.__board = board

    def move_piece(self, piece_move: PieceMove):
        self.__player = Player(piece_move.get_to_position(), )

