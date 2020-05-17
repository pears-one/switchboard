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
