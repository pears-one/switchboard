from tile_repo import TileRepo
from board import Board
from tile_tree import TileTree
from tile_position import TilePosition


def main():
    tile_config = 'tile_config.json'
    board_config = 'board_config.json'
    tile_repo = TileRepo.get_repo_from_config(tile_config)
    board = Board.from_config(board_config, tile_repo)
    start_position = TilePosition(1, 1)
    tree = TileTree(start_position)
    tree.get_accessible_position_tree(board, 3)
    print(tree)


if __name__ == "__main__":
    main()
