from board.board import Board
from analysis.tile_repo import TileRepo
from players.player import Player, get_players_from_config
from game.game import Game
from facade.facade import Facade


def main():
    players = get_players_from_config('config/players.json')
    tile_repo = TileRepo.get_repo_from_config('config/tile_config.json')
    board = Board.from_config('config/board_config.json', tile_repo)
    game = Game(board, players, 0)
    facade = Facade(game)
    facade.run(host="127.0.0.1", port="5000")


if __name__ == "__main__":
    main()
