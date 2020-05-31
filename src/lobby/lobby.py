from players.new_player import NewPlayer


class Lobby:
    def __init__(self, group_code):
        self.__group_code = group_code
        self.__players = []

    def add_player(self, player: NewPlayer):
        self.__players.append(player)

    def get_group_code(self):
        return self.__group_code

    def get_players(self):
        return self.__players
