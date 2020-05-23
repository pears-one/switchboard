from flask import Flask, request, make_response
from game.game import Game


class Facade:
    def __init__(self, game: Game):
        self.__game = game
        self.app = Flask(__name__)
        self.app.add_url_rule('/', None, self.health_check)
        self.app.add_url_rule('/move_tile', None, self.move_tile)
        self.app.add_url_rule('/player', None, self.get_next_player)

    def health_check(self):
        return "Welcome to Switchboard"

    def move_tile(self):
        response = make_response()
        if self.__game.get_current_player() != request.cookies["player"]:
            response.status_code = 401  # Not this player's turn
            return response
        if self.__game.move_tile():
            response.status_code = 200  # Move Successful
            return response
        response.status_code = 400
        return response  # Move not possible

    def get_next_player(self):
        return str(self.__game.get_current_player())

    def run(self, *args, **kwargs):
        self.app.run(*args, **kwargs)

