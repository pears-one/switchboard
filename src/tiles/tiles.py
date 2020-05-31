from spots.spots import Spot, WinningSpot
from spots.spot_positions import SpotPositionFactory, SpotPosition
from config.constants import DIRECTIONS
from tiles.tile_id import TileID
from config.constants import TOP_SPOT
from spots.spot_positions import Top, Left, Middle, Right, Bottom


class Tile:
    def __init__(self, tile_id: TileID, spot_list: list):
        self.__spot_list = spot_list
        self.__tile_id = tile_id

    def is_accessible_from(self, direction):
        return any([spot.adjacent_tile_direction() == direction for spot in self.__spot_list])

    def get_spot_list(self):
        return self.__spot_list

    def get_tile_id(self):
        return self.__tile_id

    def get_spot_at_position(self, spot_position: SpotPosition):
        for spot in self.__spot_list:
            if spot.get_position() == spot_position:
                return spot

    @classmethod
    def from_config_list(cls, config: list):
        spots = []
        tile_id = TileID(config[0], config[1])
        for position, colour in enumerate(config[2:]):
            if colour == 0:
                continue
            spot_position = SpotPositionFactory.get_by_id(position)
            if tile_id == TileID(4, 3) and position == TOP_SPOT:
                spots.append(WinningSpot(spot_position, colour))
            else:
                spots.append(Spot(spot_position, colour))
        return cls(tile_id, spots)


class RotatedTile(Tile):
    def __init__(self, tile_id, spot_list, rotation):
        super().__init__(tile_id, spot_list)
        self.__rotation = rotation

    def is_accessible_from(self, direction):
        direction_index = DIRECTIONS.index(direction)
        direction = DIRECTIONS[direction_index-self.get_rotation() % 4]
        return super().is_accessible_from(direction)

    def get_rotation(self):
        return self.__rotation

    @classmethod
    def from_tile(cls, tile: Tile, rotation: int):
        return cls(tile.get_tile_id(), tile.get_spot_list(), rotation)

    @staticmethod
    def __get_spot_position_by_rotated_spot_position(position_on_rotated_tile):
        if position_on_rotated_tile == Middle():
            return Middle()
        edge_spots = [Top(), Left(), Bottom(), Right()]
        return edge_spots[edge_spots.index(position_on_rotated_tile)]

    def get_spot_at_position(self, rotated_position: SpotPosition):
        spot_position = self.__get_spot_position_by_rotated_spot_position(rotated_position)
        return super().get_spot_at_position(spot_position)

    def marshal(self):
        return {
            "tile_id": self.get_tile_id().marshal(),
            "spots": [spot.marshal() for spot in self.get_spot_list()],
            "rotation": self.get_rotation()
        }
