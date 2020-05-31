class TileID:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def __iter__(self):
        yield self.get_x()
        yield self.get_y()

    def marshal(self):
        return {
            "x": self.get_x(),
            "y": self.get_y()
        }

    def __eq__(self, other):
        return type(self) == type(other) and self.get_x() == other.get_x() and self.get_y() == other.get_y()
