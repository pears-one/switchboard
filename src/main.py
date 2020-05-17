from tile_repo import TileRepo
from board import Board
from tile_tree import TileTree
from tile_position import TilePosition


def main():
    tile_config = 'tile_config.json'
    board_config = 'board_config.json'
    tile_repo = TileRepo.get_repo_from_config(tile_config)
    board = Board.from_config(board_config, tile_repo)
    start_position = TilePosition(1, 5)
    tree = TileTree(start_position)
    tree.get_accessible_position_tree(board, 5)
    end_position = TilePosition(3, 6)
    print(tree.can_access(end_position))
    print(tree.get_paths_to(end_position))


if __name__ == "__main__":
    main()
