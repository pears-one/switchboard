class Tile:
    def __init__(self, top, left, middle, right, bottom):
        self.__top = top
        self.__left = left
        self.__middle = middle
        self.__right = right
        self.__bottom = bottom

    def __get_edge_list(self):
        return [self.__top, self.__left, self.__bottom, self.__right]

    def get_top(self, rotation=0):
        return self.__get_edge_list()[rotation%4]

    def get_left(self, rotation=0):
        return self.__get_edge_list()[(rotation+1)%4]

    def get_middle(self):
        return self.__middle

    def get_bottom(self, rotation=0):
        return self.__get_edge_list()[(rotation+2)%4]

    def get_right(self, rotation=0):
        return self.__get_edge_list()[(rotation+3)%4]

    def top_is_playable(self, rotation=0):
        return self.get_top(rotation) > 0
    
    def left_is_playable(self, rotation=0):
        return self.get_left(rotation) > 0

    def bottom_is_playable(self, rotation=0):
        return self.get_bottom(rotation) > 0

    def right_is_playable(self, rotation=0):
        return self.get_right(rotation) > 0

    