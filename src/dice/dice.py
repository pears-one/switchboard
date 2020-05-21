import random


class Die:
    def __init__(self, number_of_sides):
        self.__sides = number_of_sides
        self.__value = None
        self.roll()

    def roll(self):
        self.__value = random.randint(1, self.__sides)

    def get_value(self):
        return self.__value
