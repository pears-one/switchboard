from flask import Flask, request
from game.game import Game


class Facade:
    def __init__(self, game: Game):
        self.__game = game
        self.app = Flask(__name__)
        self.app.add_url_rule('/', None, self.health_check)
        self.app.add_url_rule('/move', None, self.make_move)
        self.app.add_url_rule('/player', None, self.get_next_player)

    def health_check(self):
        return "Welcome to Switchboard"

    def make_move(self):
        return "you moved!"

    def get_next_player(self):
        return str(self.__game.get_next_player())

    def run(self, *args, **kwargs):
        self.app.run(*args, **kwargs)

