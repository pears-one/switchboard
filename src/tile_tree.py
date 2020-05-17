from tile_position import TilePosition
from constants import MAX_DEPTH, DIRECTIONS, opposite


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
        from_tile = board.get_tile_at(root)
        tree_by_direction = dict()
        for direction in DIRECTIONS:
            to_tile = board.get_tile(direction, root)
            to_pos = root.get_position(direction)
            if from_tile.is_accessible_from(direction) \
                    and to_tile is not None \
                    and to_pos != parent \
                    and to_tile.is_accessible_from(opposite(direction)):
                child_node = cls.get_accessible_position_tree(board, to_pos, max_depth, depth+1, root)
                tree_by_direction[direction] = child_node
        return cls(root, None, tree_by_direction)

    def get_tile_paths_to(self, target):
        return self.__get_paths_to_target(target)

    def __get_paths_to_target(self, target: TilePosition, path_to_here=[], completed_paths=[], depth=0):
        if self.__get_position() == target:
            completed_paths.append(path_to_here)

        for direction, child_tree in self.__get_child_tree_by_direction().items():
            child_tree.__get_paths_to_target(target, path_to_here + [direction], completed_paths, depth+1)

        if depth == 0:
            return completed_paths




