from utils.functions import random_string
from players.new_player import NewPlayer
from lobby.lobby import Lobby


class LobbyManager:
    def __init__(self):
        self.__lobbies_by_code = dict()

    def get_lobby_by_code(self, group_code):
        return self.__lobbies_by_code[group_code]

    def add_player_to_lobby(self, group_code, new_player: NewPlayer):
        lobby = self.get_lobby_by_code(group_code)
        lobby.add_player(new_player)

    def new_lobby(self, first_player: NewPlayer):
        group_code = random_string()
        new_lobby = Lobby(group_code)
        new_lobby.add_player(first_player)
        self.__lobbies_by_code[group_code] = new_lobby
        return group_code

    def pop_lobby_by_code(self, group_code):
        return self.__lobbies_by_code.pop(group_code)

    def exists(self, group_code):
        return group_code in self.__lobbies_by_code
