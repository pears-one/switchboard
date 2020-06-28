from players.new_player import NewPlayer
from lobby.manager import LobbyManager
from game.manager import GameManager


class Service:
    def __init__(self, lobby_manager: LobbyManager, game_manager: GameManager):
        self.__lobby_manager = lobby_manager
        self.__game_manager = game_manager

    def get_players_in_lobby(self, group_code):
        lobby = self.__lobby_manager.get_lobby_by_code(group_code)
        return lobby.get_players()

    def new_lobby(self, first_player: NewPlayer):
        group_code = self.__lobby_manager.new_lobby(first_player)
        return group_code

    def add_player_to_lobby(self, group_code, new_player: NewPlayer):
        self.__lobby_manager.add_player_to_lobby(group_code, new_player)
        return group_code

    def start_game(self, group_code):
        lobby = self.__lobby_manager.pop_lobby_by_code(group_code)
        self.__game_manager.new_game(lobby)

    def get_current_player_cookie(self, group_code):
        return self.__game_manager.get_current_player(group_code).get_cookie()

    def get_game_data(self, group_code):
        return self.__game_manager.get_data(group_code)

    def roll(self, group_code):
        return self.__game_manager.roll(group_code)

    def move_tile(self, group_code, tile_move):
        return self.__game_manager.move_tile(group_code, tile_move)

    def game_exists(self, group_code):
        return self.__game_manager.exists(group_code)

    def move_piece(self, group_code, to_position):
        return self.__game_manager.move_piece(group_code, to_position)

    def lobby_exists(self, group_code):
        return self.__lobby_manager.exists(group_code)
