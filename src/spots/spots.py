from spots.spot_positions import SpotPosition


class Spot:
    def __init__(self, position: SpotPosition, colour: int = None):
        self.__colour = colour
        self.__position = position

    @staticmethod
    def is_winning_spot(self):
        return False

    def get_colour(self):
        return self.__colour

    def get_position(self):
        return self.__position

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

    def marshal(self):
        return {
            "position": str(self.get_position()),
            "colour": self.__colour
        }


class WinningSpot(Spot):
    def __init__(self, spot_position: SpotPosition, colour: int):
        super().__init__(spot_position, colour)

    @staticmethod
    def is_winning_spot(self):
        return True


