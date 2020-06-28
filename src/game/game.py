from board.board import Board
from analysis.board_analyser import BoardAnalyser
from dice.roll import DiceRoll
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

    def __next_player(self):
        if self.get_current_player().has_another_go():
            self.get_current_player().toggle_has_another_go()

        next_player = (self.__player_to_move + 1) % self.__get_number_of_players()
        self.__player_to_move = next_player

        if self.get_current_player().is_missing_next_turn():
            self.get_current_player().toggle_missing_next_turn()
            self.__next_player()

    def get_current_player(self) -> Player:
        return self.__players[self.__player_to_move]

    def move_tile(self, tile_move):
        analyser = BoardAnalyser(self.__board)
        if analyser.is_tile_move_valid(tile_move, self.__dice_roll) and self.__turn_phase == MOVE_TILE:
            self.__board = self.__board.move_tile(tile_move)
            self.__set_phase(ROLL)
            self.__next_player()
            return True
        return False

    def is_over(self):
        analyser = BoardAnalyser(self.__board)
        return any([analyser.is_winning_position(player.get_position()) for player in self.__players])

    def roll_dice(self):
        if self.__turn_phase == ROLL:
            self.__dice_roll.roll_dice()
            self.__set_phase(MOVE_PIECE)
            return True
        return False

    def __spot_colour_of_current_player(self):
        player_position = self.get_current_player().get_position()
        spot = self.__board.get_spot_at_piece_position(player_position)
        return spot.get_colour()

    def move_piece(self, to_piece_position):
        analyser = BoardAnalyser(self.__board)
        player = self.get_current_player()
        move = PieceMove(player.get_position(), to_piece_position)
        if analyser.is_piece_move_valid(move, self.__dice_roll) and self.__turn_phase == MOVE_PIECE:
            player.move_piece(to_piece_position)
            if self.__spot_colour_of_current_player() == GREEN:
                player.toggle_has_another_go()
            if self.__spot_colour_of_current_player() == RED:
                player.toggle_missing_next_turn()
            self.__set_phase(MOVE_TILE)
            return True
        return False

    def get_phase(self):
        return self.__turn_phase

    def remove_player(self, player_cookie):
        self.__players = [player for player in self.__players if player.get_cookie() != player_cookie]

    def marshal(self):
        return {
            "board": self.__board.marshal(),
            "players": [player.marshal() for player in self.__players],
            "player_to_move": self.__player_to_move,
            "phase": self.get_phase(),
            "dice_roll": list(self.__dice_roll),
            "is_over": self.is_over()
        }
