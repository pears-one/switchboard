from tiles.spots import LeftSpot, RightSpot, MiddleSpot, BottomSpot, TopSpot
from config.constants import DIRECTIONS


class Tile:
    def __init__(self, spot_list):
        self.__spot_list = spot_list

    def is_accessible_from(self, direction):
        return any([spot.adjacent_tile_direction() == direction for spot in self.__spot_list])

    def get_spot_list(self):
        return self.__spot_list

    @classmethod
    def from_config_list(cls, config: list):
        spot_by_position = [TopSpot, LeftSpot, MiddleSpot, RightSpot, BottomSpot]
        spots = []
        for position, colour in enumerate(config):
            if colour == 0:
                continue
            spots.append(spot_by_position[position](colour))
        return cls(spots)


class RotatedTile(Tile):
    def __init__(self, spot_list, rotation):
        super().__init__(spot_list)
        self.__rotation = rotation

    def is_accessible_from(self, direction):
        direction_index = DIRECTIONS.index(direction)
        direction = DIRECTIONS[direction_index-self.get_rotation() % 4]
        return super().is_accessible_from(direction)

    def get_rotation(self):
        return self.__rotation
