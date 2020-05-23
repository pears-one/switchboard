from analysis.tile_tree import TileTree
from spots.spots import Spot
from config.constants import opposite
from moves.piece_move import PieceMove
from moves.tile_move import TileMove
from board.board import Board
from dice.dice_roll import DiceRoll
from tiles.tile_id import TileID
from players.piece_position import PiecePosition


class BoardAnalyser:
    def __init__(self, board: Board):
        self.__board = board

    def calculate_move_distance(self, move: PieceMove):
        source_position, target_position = move.get_from_position(), move.get_to_position()
        tree = TileTree.get_accessible_position_tree(self.__board, source_position.get_tile_position())
        direction_paths = tree.get_tile_paths_to(target_position.get_tile_position())
        return [self.get_path_distance(path, source_position.get_spot(), target_position.get_spot()) for path in direction_paths]

    @staticmethod
    def get_path_distance(direction_path, from_spot: Spot, to_spot: Spot):
        if len(direction_path) == 0:
            return from_spot.distance_to(to_spot)
        distance_to_second_tile = from_spot.distance_to_tile(direction_path[0])
        distance_from_penultimate_tile = to_spot.distance_to_tile(opposite(direction_path[-1]))
        return (len(direction_path) - 1) * 3 + distance_from_penultimate_tile + distance_to_second_tile - 1

    def is_piece_move_valid(self, move: PieceMove, dice_roll: DiceRoll):
        return dice_roll.get_dice_total() in self.calculate_move_distance(move)

    def is_tile_move_valid(self, tile_move: TileMove, dice_roll: DiceRoll):
        valid_tile_ids = [TileID(dice_roll.get_dice_values()[i], dice_roll.get_dice_values()[(i+1) % 2]) for i in range(2)]
        if self.__board.get_tile_at(tile_move.get_from_pos()).get_tile_id() not in valid_tile_ids:
            return False
        new_board = self.__board.move_tile(tile_move)
        if new_board.get_tile_count() != self.__board.get_tile_count():
            return False
        tree = TileTree.get_accessible_position_tree(new_board, tile_move.get_to_pos(), 1)
        if len(tree.get_valid_directions()) == 0:
            return False
        return True

    def is_winning_position(self, piece_position: PiecePosition):
        spot = self.__board.get_spot_at_piece_position(piece_position)
        return spot.is_winning_spot()


