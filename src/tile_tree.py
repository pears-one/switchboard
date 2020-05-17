from tile_position import TilePosition
import constants


class TileTree:

    def __init__(self, position: TilePosition, parent_position: TilePosition = None):
        self.__position = position
        self.__parent_position = parent_position
        self.__tree_by_direction = dict()

    def get_position(self):
        return self.__position

    def get_child_tree_by_direction(self):
        return self.__tree_by_direction

    def get_child(self, direction):
        return self.__tree_by_direction[direction]

    def number_of_directions(self):
        return len(self.get_child_tree_by_direction())

    def __repr__(self):
        return f"{self.get_position()}:" + str(self.get_accessible_directions())

    def __get_tile_position(self):
        return self.get_position()

    def __add_direction(self, direction, tree):
        self.__tree_by_direction[direction] = tree

    def __get_parent(self):
        return self.__parent_position

    def get_accessible_position_tree(self, board, max_depth: int):
        if max_depth == 0:
            return
        from_tile = board.get_tile_at(self.__get_tile_position())
        for direction in constants.directions:
            to_tile = board.get_tile(direction, self.__get_tile_position())
            to_pos = self.__get_tile_position().get_position(direction)
            if from_tile.is_accessible_from(direction) \
                    and to_tile is not None \
                    and to_pos != self.__get_parent() \
                    and to_tile.is_accessible_from(constants.opposite(direction)):
                child_node = TileTree(to_pos, self.get_position())
                child_node.get_accessible_position_tree(board, max_depth-1)
                self.__add_direction(direction, child_node)

    def can_access(self, pos: TilePosition):
        if self.get_position() == pos:
            return True
        return any([child_tree.can_access(pos) for child_tree in self.get_child_tree_by_direction().values()])

    def get_paths_to(self, target):
        return self.__get_paths_to_target(target)

    def __get_paths_to_target(self, target: TilePosition, path_to_here=[], completed_paths=[], depth=0):
        if self.get_position() == target:
            completed_paths.append(path_to_here)

        for direction, child_tree in self.get_child_tree_by_direction().items():
            if child_tree.can_access(target):
                child_tree.__get_paths_to_target(target, path_to_here + [direction], completed_paths, depth+1)

        if depth == 0:
            return completed_paths

    def calculate_distance_between_spots(self, from_spot, to_position, to_spot):
        pass


