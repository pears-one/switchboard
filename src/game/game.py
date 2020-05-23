from board.board import Board
from analysis.board_analyser import BoardAnalyser
from moves.tile_move import TileMove
from dice.dice_roll import DiceRoll
from moves.piece_move import PieceMove
from config.constants import MOVE_PIECE, MOVE_TILE, ROLL, GREEN, RED
from players.player import Player


class Game:
    def __init__(self, board: Board, players: list, player_to_move: int, dice_roll: DiceRoll, turn_phase: str):
        self.__board = board
        self.__players = players
        self.__player_to_move = player_to_move
        self.__dice_roll = dice_roll
        self.__turn_phase = turn_phase

    def __get_number_of_players(self):
        return len(self.__players)

    def __set_phase(self, phase):
        self.__turn_phase = phase

    def next_player(self):
        if self.get_current_player().has_another_go():
            self.get_current_player().toggle_has_another_go()

        next_player = (self.__player_to_move + 1) % self.__get_number_of_players()
        self.__player_to_move = next_player

        if self.get_current_player().is_missing_next_turn():
            self.get_current_player().toggle_missing_next_turn()
            self.next_player()

    def get_current_player(self) -> Player:
        return self.__players[self.__player_to_move]

    def get_current_player_cookie(self):
        return self.__players[self.__player_to_move].get_cookie()

    def move_tile(self, from_tile_position, to_tile_position, rotation):
        analyser = BoardAnalyser(self.__board)
        move = TileMove(from_tile_position, to_tile_position, rotation)
        if analyser.is_tile_move_valid(move, self.__dice_roll):
            self.__board = self.__board.move_tile(move)
            self.__set_phase(ROLL)
            self.next_player()
            return True
        return False

    def is_over(self):
        analyser = BoardAnalyser(self.__board)
        for position in [player.get_position() for player in self.__players]:
            if analyser.is_winning_position(position):
                return True
        return False

    def roll_dice(self):
        self.__dice_roll.roll_dice()
        self.__set_phase(MOVE_PIECE)

    def spot_colour_of_current_player(self):
        player_position = self.get_current_player().get_position()
        spot = self.__board.get_spot_at_piece_position(player_position)
        return spot.get_colour()

    def move_piece(self, to_piece_position):
        analyser = BoardAnalyser(self.__board)
        player = self.get_current_player()
        move = PieceMove(player.get_position(), to_piece_position)
        if analyser.is_piece_move_valid(move, self.__dice_roll):
            player.move_piece(to_piece_position)
            if self.spot_colour_of_current_player() == GREEN:
                player.toggle_has_another_go()
            if self.spot_colour_of_current_player() == RED:
                player.toggle_missing_next_turn()
            self.__set_phase(MOVE_TILE)
            return True
        return False

    def remove_player(self, player_cookie):
        self.__players = [player for player in self.__players if player.get_cookie() != player_cookie]


