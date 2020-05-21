from board.board import Board


class Game:
    def __init__(self, board: Board, players: list, player_to_move: int):
        self.__board = board
        self.__players = players
        self.__player_to_move = player_to_move

    def get_number_of_players(self):
        return len(self.__players)

    def get_next_player(self):
        return self.__players[self.__player_to_move]

    def move_tile(self):
        pass
