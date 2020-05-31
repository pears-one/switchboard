from spots.spot_positions import SpotPosition
from board.tile_position import TilePosition


class PiecePosition:
    def __init__(self, tile_position: TilePosition, spot_position: SpotPosition):
        self.__tile_position = tile_position
        self.__spot_position = spot_position

    def get_tile_position(self):
        return self.__tile_position

    def get_spot_position(self):
        return self.__spot_position

    def marshal(self):
        return {
            "tile_position": self.__tile_position.marshal(),
            "spot_position": str(self.__spot_position)
        }
