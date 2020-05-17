from analysis.tile_tree import TileTree
from tiles.spots import Spot
from config.constants import opposite


class BoardAnalyser:
    def __init__(self, board):
        self.__board = board

    def calculate_distance_between_spots(self, source_tile_position, from_spot, target_tile_position, to_spot):
        tree = TileTree.get_accessible_position_tree(self.__board, source_tile_position)
        direction_paths = tree.get_tile_paths_to(target_tile_position)
        return [self.get_path_distance(path, from_spot, to_spot) for path in direction_paths]

    @staticmethod
    def get_path_distance(direction_path, from_spot: Spot, to_spot: Spot):
        if len(direction_path) == 0:
            return from_spot.distance_to(to_spot)
        distance_to_second_tile = from_spot.distance_to_tile(direction_path[0])
        distance_from_penultimate_tile = to_spot.distance_to_tile(opposite(direction_path[-1]))
        return (len(direction_path) - 1) * 3 + distance_from_penultimate_tile + distance_to_second_tile - 1
