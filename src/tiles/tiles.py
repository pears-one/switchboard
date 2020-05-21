from spots.spots import Spot
from spots.spot_positions import SpotPositionFactory
from config.constants import DIRECTIONS
from tiles.tile_id import TileID


class Tile:
    def __init__(self, tile_id, spot_list):
        self.__spot_list = spot_list
        self.__tile_id = tile_id

    def is_accessible_from(self, direction):
        return any([spot.adjacent_tile_direction() == direction for spot in self.__spot_list])

    def get_spot_list(self):
        return self.__spot_list

    def get_tile_id(self):
        return self.__tile_id

    @classmethod
    def from_config_list(cls, config: list):
        spots = []
        tile_id = TileID(config[0], config[1])
        for position, colour in enumerate(config[2:]):
            if colour == 0:
                continue
            spot_position = SpotPositionFactory.get_by_id(position)
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
