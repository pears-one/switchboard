from tile_position import TilePosition
import constants


class TileTree:

    def __init__(self, position: TilePosition, visited=[]):
        self.__position = position
        self.__visited = visited
        self.__tree_by_direction = dict()

    def get_accessible_directions(self):
        return self.__tree_by_direction

    def get_child(self, direction):
        return self.__tree_by_direction[direction]

    def number_of_directions(self):
        return len(self.get_accessible_directions())

    def __repr__(self):
        return f"{self.__position}:" + str(self.get_accessible_directions())

    def __get_tile_position(self):
        return self.__position

    def __add_direction(self, direction, tree):
        self.__tree_by_direction[direction] = tree

    def __get_visited(self):
        return self.__visited

    def __add_to_visited(self):
        self.__get_visited().append(self.__get_tile_position())

    def get_accessible_position_tree(self, board, max_depth: int):
        self.__add_to_visited()
        if max_depth == 0:
            return
        from_tile = board.get_tile_at(self.__get_tile_position())
        for direction in constants.directions:
            to_tile = board.get_tile(direction, self.__get_tile_position())
            to_pos = self.__get_tile_position().get_position(direction)
            if from_tile.is_accessible_from(direction) \
                    and to_tile is not None \
                    and not(to_pos in self.__get_visited()) \
                    and to_tile.is_accessible_from(constants.opposite(direction)):
                child_node = TileTree(to_pos, self.__get_visited())
                child_node.get_accessible_position_tree(board, max_depth-1)
                self.__add_direction(direction, child_node)
