from tile_repo import TileRepo
from board import Board
from tile_position import TilePosition
from board_analyser import BoardAnalyser
from tile_tree import TileTree
from spots import TopSpot, BottomSpot


def main():
    tile_config = 'tile_config.json'
    board_config = 'board_config.json'
    tile_repo = TileRepo.get_repo_from_config(tile_config)
    board = Board.from_config(board_config, tile_repo)
    start_position = TilePosition(1, 5)
    end_position = TilePosition(1, 5)
    analyser = BoardAnalyser(board)
    print(TileTree.get_accessible_position_tree(board, start_position))
    print(analyser.calculate_distance_between_spots(start_position, TopSpot(), end_position, BottomSpot()))


if __name__ == "__main__":
    main()
