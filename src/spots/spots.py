from spots.spot_positions import SpotPosition


class Spot:
    def __init__(self, position: SpotPosition, colour: int = None):
        self.__colour = colour
        self.__position = position

    def get_colour(self):
        return self.__colour

    def adjacent_tile_direction(self):
        return self.__position.adjacent_tile_direction()

    def distance_to_tile(self, tile_direction):
        if tile_direction == self.adjacent_tile_direction():
            return 1
        return 3

    def is_edge_spot(self):
        return self.__position.is_on_edge()

    def distance_to(self, other):
        if self == other:
            return 0
        if self.is_edge_spot() and other.is_on_edge():
            return 2
        return 1

    def __eq__(self, other):
        return type(self) == type(other)
