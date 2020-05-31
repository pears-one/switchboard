from config.constants import ABOVE, BELOW, RIGHT, LEFT, TOP_SPOT, LEFT_SPOT, RIGHT_SPOT, BOTTOM_SPOT, MIDDLE_SPOT


class SpotPosition:

    def __init__(self, spot_id):
        self.__id = spot_id

    @staticmethod
    def adjacent_tile_direction():
        return None

    def distance_to_tile(self, tile_direction):
        if tile_direction == self.adjacent_tile_direction():
            return 1
        return 3

    @staticmethod
    def is_on_edge():
        return None

    def distance_to(self, other):
        if self == other:
            return 0
        if self.is_on_edge() and other.is_on_edge():
            return 2
        return 1

    def __eq__(self, other):
        return type(self) == type(other)

    def __str__(self):
        return type(self).__name__

    def get_id(self):
        return self.__id


class Middle(SpotPosition):

    def distance_to_tile(self, tile_direction):
        return 2

    @staticmethod
    def is_on_edge():
        return False


class Bottom(SpotPosition):

    @staticmethod
    def adjacent_tile_direction():
        return BELOW

    @staticmethod
    def is_on_edge():
        return True


class Left(SpotPosition):

    @staticmethod
    def adjacent_tile_direction():
        return LEFT

    @staticmethod
    def is_on_edge():
        return True


class Top(SpotPosition):

    @staticmethod
    def adjacent_tile_direction():
        return ABOVE

    @staticmethod
    def is_on_edge():
        return True


class Right(SpotPosition):

    @staticmethod
    def adjacent_tile_direction():
        return RIGHT

    @staticmethod
    def is_on_edge():
        return True


class SpotPositionFactory:
    @staticmethod
    def get_by_id(spot_id: int):
        spots_by_id = {
            TOP_SPOT: Top,
            LEFT_SPOT: Left,
            MIDDLE_SPOT: Middle,
            RIGHT_SPOT: Right,
            BOTTOM_SPOT: Bottom
        }
        return spots_by_id[spot_id]()
