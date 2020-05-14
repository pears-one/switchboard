from tile_repo import TileRepo
from board import Board
from game_engine import GameEngine

def main():
    config_file = 'config.json'
    tile_repo = TileRepo.get_repo_from_config(config_file)
    board = Board.from_config(config_file)
    engine = GameEngine(1, board, tile_repo)

if __name__ == "__main__":
    main()