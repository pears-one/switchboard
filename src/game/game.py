class Game:
    def __init__(self, board, players, player_number_to_move):
        self.__board = board
        self.__players = players
        self.__player_to_move = player_number_to_move

    def get_number_of_players(self):
        return len(self.__players)

    def play(self):
        while True:
            player_to_move = self.__players[self.__player_number_to_move]

