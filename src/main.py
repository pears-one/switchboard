from tile_repo import TileRepo
from board import Board
from board_analyser import BoardAnalyser

def main():
    config_file = 'config.json'
    tile_repo = TileRepo.get_repo_from_config(config_file)
    board = Board.from_config(config_file)
    analyser = BoardAnalyser(1, board, tile_repo)
    print(analyser.is_move_valid(1,1,7,6,0))

if __name__ == "__main__":
    main()