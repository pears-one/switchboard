from constants import LEFT, RIGHT, ABOVE, BELOW


class TilePosition:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @classmethod
    def from_tuple(cls, position_tuple):
        return cls(position_tuple[0], position_tuple[1])

    def left(self):
        return TilePosition(self.__x - 1, self.__y)

    def right(self):
        return TilePosition(self.__x + 1, self.__y)

    def above(self):
        return TilePosition(self.__x, self.__y - 1)

    def below(self):
        return TilePosition(self.__x, self.__y + 1)

    def __iter__(self):
        yield self.__x
        yield self.__y

    def __eq__(self, other):
        return other is not None and self.__x == other.__x and self.__y == other.__y

    def get_position(self, direction):
        check = {ABOVE: self.above, BELOW: self.below, LEFT: self.left, RIGHT: self.right}
        return check[direction]()

    def __str__(self):
        return "Pos(" + str(self.__x) + ", " + str(self.__y) + ")"

    def __repr__(self):
        return "Pos(" + str(self.__x) + ", " + str(self.__y) + ")"
