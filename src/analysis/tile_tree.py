from board.tile_position import TilePosition
from config.constants import MAX_DEPTH, DIRECTIONS, opposite


class TileTree:

    def __init__(self, position: TilePosition, parent_position: TilePosition, tree_by_direction):
        self.__position = position
        self.__parent_position = parent_position
        self.__tree_by_direction = tree_by_direction

    def __get_position(self):
        return self.__position

    def __get_child_tree_by_direction(self):
        return self.__tree_by_direction

    def __repr__(self):
        return f"{self.__get_position()}:" + str(self.__get_child_tree_by_direction())

    @classmethod
    def get_accessible_position_tree(cls, board, root: TilePosition, max_depth: int = MAX_DEPTH, depth: int = 0, parent=None):
        if depth == max_depth:
            return cls(root, parent, dict())
        tree_by_direction = dict()
        for direction in DIRECTIONS:
            to_pos = root.get_position_in_direction(direction)
            if to_pos != parent and board.is_connection_from(root, direction):
                child_node = cls.get_accessible_position_tree(board, to_pos, max_depth, depth+1, root)
                tree_by_direction[direction] = child_node
        return cls(root, None, tree_by_direction)

    def get_tile_paths_to(self, target: TilePosition):
        return self.__get_paths_to_target(target)

    def __get_paths_to_target(self, target: TilePosition, path_to_here=[], completed_paths=[], depth=0):
        if self.__get_position() == target:
            completed_paths.append(path_to_here)

        for direction, child_tree in self.__get_child_tree_by_direction().items():
            child_tree.__get_paths_to_target(target, path_to_here + [direction], completed_paths, depth+1)

        if depth == 0:
            return completed_paths

    def get_valid_directions(self):
        return list(self.__tree_by_direction.keys())




