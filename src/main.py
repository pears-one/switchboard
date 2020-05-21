from analysis.tile_repo import TileRepo
from board.board import Board
from board.tile_position import TilePosition
from analysis.board_analyser import BoardAnalyser
from analysis.tile_tree import TileTree
from players.piece_position import PiecePosition
from spots.spot_positions import Top, Bottom
from moves.tile_move import TileMove
from dice.dice_roll import DiceRoll
from dice.dice import Die


def main():
    tile_config = 'config/tile_config.json'
    board_config = 'config/board_config.json'
    tile_repo = TileRepo.get_repo_from_config(tile_config)
    board = Board.from_config(board_config, tile_repo)
    start_piece_position = PiecePosition(TilePosition(1, 1), Top())
    end_piece_position = PiecePosition(TilePosition(2, 5), Top())
    tile_move = TileMove(TilePosition(1, 1), TilePosition(6, 7), 0)
    analyser = BoardAnalyser(board)
    print(analyser.tile_move_is_valid(tile_move, DiceRoll([Die(6), Die(6)])))


if __name__ == "__main__":
    main()
