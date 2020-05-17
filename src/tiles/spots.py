from config.constants import ABOVE, BELOW, RIGHT, LEFT


class Spot:
    def __init__(self, colour: int = None):
        self.__colour = colour

    def get_colour(self):
        return self.__colour

    @staticmethod
    def adjacent_tile_direction():
        return None

    def distance_to_tile(self, tile_direction):
        if tile_direction == self.adjacent_tile_direction():
            return 1
        return 3

    @staticmethod
    def is_edge_spot():
        return None

    def distance_to(self, other):
        if self == other:
            return 0
        if self.is_edge_spot() and other.is_edge_spot():
            return 2
        return 1

    def __eq__(self, other):
        return type(self) == type(other)


class MiddleSpot(Spot):

    def distance_to_tile(self, tile_direction):
        return 2

    @staticmethod
    def is_edge_spot():
        return False


class BottomSpot(Spot):

    @staticmethod
    def adjacent_tile_direction():
        return BELOW

    @staticmethod
    def is_edge_spot():
        return True


class LeftSpot(Spot):

    @staticmethod
    def adjacent_tile_direction():
        return LEFT

    @staticmethod
    def is_edge_spot():
        return True


class TopSpot(Spot):

    @staticmethod
    def adjacent_tile_direction():
        return ABOVE

    @staticmethod
    def is_edge_spot():
        return True


class RightSpot(Spot):

    @staticmethod
    def adjacent_tile_direction():
        return RIGHT

    @staticmethod
    def is_edge_spot():
        return True
