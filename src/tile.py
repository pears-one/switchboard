from constants import above, left, right, below


class Tile:
    def __init__(self, top_spot, left_spot, middle_spot, right_spot, bottom_spot):
        self.__top = top_spot
        self.__left = left_spot
        self.__middle = middle_spot
        self.__right = right_spot
        self.__bottom = bottom_spot

    def __get_edge_list(self):
        return [self.__top, self.__left, self.__bottom, self.__right]

    def get_top(self, rotation=0):
        return self.__get_edge_list()[rotation % 4]

    def get_left(self, rotation=0):
        return self.__get_edge_list()[(rotation+1) % 4]

    def get_middle(self):
        return self.__middle

    def get_bottom(self, rotation=0):
        return self.__get_edge_list()[(rotation+2) % 4]

    def get_right(self, rotation=0):
        return self.__get_edge_list()[(rotation+3) % 4]

    def is_accessible_from(self, direction, rotation):
        check = {above: self.get_top, below: self.get_bottom, left: self.get_left, right: self.get_right}
        return check[direction](rotation)

