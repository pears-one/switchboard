from board.board import Board
from analysis.board_analyser import BoardAnalyser
from moves.tile_move import TileMove
from dice.dice_roll import DiceRoll


class Game:
    def __init__(self, board: Board, players: list, player_to_move: int, dice_roll: DiceRoll):
        self.__board = board
        self.__players = players
        self.__player_to_move = player_to_move
        self.__dice_roll = dice_roll

    def get_number_of_players(self):
        return len(self.__players)

    def get_player_by_cookie(self, cookie):
        for player in self.__players:
            if player.get_cookie() == cookie:
                return player

    def get_next_player(self):
        return self.__players[self.__player_to_move]

    def move_tile(self, player_cookie, to_tile_position, rotation):
        analyser = BoardAnalyser(self.__board)
        player = self.get_player_by_cookie(player_cookie)
        move = TileMove(player.get_position(), to_tile_position, rotation)
        if analyser.is_tile_move_valid(move, self.__dice_roll):
            self.__board = self.__board.move_tile(move)

    def is_over(self):
        analyser = BoardAnalyser(self.__board)
        for position in [player.get_position() for player in self.__players]:
            if analyser.is_winning_position(position):
                return True
        return False

    def roll_dice(self):
        self.__dice_roll.roll_dice()

    def move_piece(self, to_piece_position):
        pass
