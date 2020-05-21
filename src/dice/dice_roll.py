class DiceRoll:
    def __init__(self, die_list):
        self.__die_list = die_list

    def roll_dice(self):
        [die.roll() for die in self.__die_list]

    def get_dice_values(self):
        return [die.get_value() for die in self.__die_list]

    def get_dice_total(self):
        return sum([die.get_value() for die in self.__die_list])
