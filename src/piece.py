class Piece:
    def __init__(self, colour):
        self.__colour = colour

    def get_colour(self):
        return self.__colour

    def __str__(self):
        return self.__colour