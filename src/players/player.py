from players.piece import Piece


class Player:
    def __init__(self, name: str, cookie: str, piece: Piece, missing_next_turn: bool = False, has_another_go: bool = False):
        self.__piece = piece
        self.__missing_next_turn = missing_next_turn
        self.__has_another_go = has_another_go
        self.__name = name
        self.__cookie = cookie

    def move_piece(self, new_position):
        self.__piece.move(new_position)

    def get_cookie(self):
        return self.__cookie

    def get_name(self):
        return self.__name

    def toggle_missing_next_turn(self):
        self.__missing_next_turn = not self.__missing_next_turn

    def is_missing_next_turn(self):
        return self.__missing_next_turn

    def toggle_has_another_go(self):
        self.__missing_next_turn = not self.__missing_next_turn

    def has_another_go(self):
        return self.__missing_next_turn

    def get_position(self):
        return self.__piece.get_piece_position()

    def __str__(self):
        return "Hey! I'm " + self.get_name()

    def marshal(self):
        return {
            "name": self.__name,
            "cookie": self.__cookie,
            "piece": self.__piece.marshal(),
            "missing_next_turn": self.__missing_next_turn,
            "has_another_go": self.has_another_go()
        }


def initialise_players(new_player_list):
    player_objects = []
    for colour, player in enumerate(new_player_list):
        piece = Piece(colour)
        player_objects.append(Player(player.get_name(), player.get_cookie(), piece))

    return player_objects

