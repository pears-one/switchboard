from lobby.lobby import Lobby
from players.player import initialise_players
from analysis.tile_repo import TileRepo
from config.constants import TILE_CONFIG_PATH, BOARD_CONFIG_PATH, ROLL
from board.board import Board
from game.game import Game
from dice.roll import DiceRoll


class GameManager:
    def __init__(self):
        self.__games = dict()

    def new_game(self, lobby: Lobby):
        group_code = lobby.get_group_code()
        players = initialise_players(lobby.get_players())
        tile_repo = TileRepo.get_repo_from_config(TILE_CONFIG_PATH)
        board = Board.from_config(BOARD_CONFIG_PATH, tile_repo)
        dice_roll = DiceRoll.generate_dice(2, 6)
        game = Game(board, players, 0, dice_roll, ROLL)
        self.__games[group_code] = game

    def get_current_player(self, group_code):
        return self.__games[group_code].get_current_player()

    def get_data(self, group_code):
        return self.__games[group_code].marshal()

    def roll(self, group_code):
        return self.__games[group_code].roll_dice()

    def move_piece(self, group_code):
        return

    def move_tile(self, group_code, tile_move):
        return self.__games[group_code].move_tile(tile_move)
