from spots.spot_positions import SpotPosition, SpotPositionFactory
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
            "spot_position": self.__spot_position.get_id()
        }

    @classmethod
    def unmarshal(cls, pos_dict):
        return cls(
            TilePosition.unmarshal(pos_dict["tile_position"]),
            SpotPositionFactory.get_by_id(pos_dict["spot_position"])
        )
