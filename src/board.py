import json
from exceptions import MoveError

class Board:
    def __init__(self, tile_dictionary):
        self.__tile_dictionary = tile_dictionary

    @staticmethod
    def from_config(filename):
        def config_list_to_dict(conf_list):
            return {
                "tile": (conf_list[0], conf_list[1]),
                "rotation": conf_list[2]
            }
        with open(filename) as config:
            config = json.load(config)
            board_config = config["board"]
        tile_dictionary = dict()
        for y, row in enumerate(board_config):
            for x, tile in enumerate(row):
                tile_dictionary[(x+1,y+1)]=config_list_to_dict(tile) 
        return Board(tile_dictionary)

    def get_tile_at_position(self, x, y):
        return self.__tile_dictionary[(x,y)]

    def get_tile_positions(self):
        return list(self.__tile_dictionary.keys())
        
    def move_tile(self, from_x, from_y, to_x, to_y, rotation): 
        if (from_x, from_y) not in self.get_tile_positions() or (to_x, to_y) in self.get_tile_positions():
            raise MoveError
        new_tile_dict = {(to_x, to_y): self.get_tile_at_position(from_x, from_y)}
        
        for position in self.get_tile_positions():
            if position == (from_x, from_y):
                continue
            new_tile_dict[position] = self.get_tile_at_position(*position)

        return Board(new_tile_dict)

    @staticmethod
    def position_above(x,y):
        return (x, y-1)

    @staticmethod
    def position_below(x,y):
        return (x, y+1)

    @staticmethod
    def position_to_left(x,y):
        return (x-1, y)

    @staticmethod
    def position_to_right(x,y):
        return (x+1, y)

    def adjacent_positions(self, x,y):
        location_functions = [self.position_above, self.position_to_right, self.position_below, self.position_to_left]
        return [loc_func(x, y) for loc_func in location_functions]

    def get_empty_adjacent_positions(self, x, y):
        return [position for position in self.adjacent_positions(x, y) if position not in self.get_tile_positions()]

    def get_adjacent_tiles(self, x, y):
        return [position for position in self.adjacent_positions(x, y) if position in self.get_tile_positions()]

    def get_all_empty_adjacent_positions(self):
        empty_adjacent_positions = set()
        for position in self.get_tile_positions():
            empty_adjacent_positions = empty_adjacent_positions.union(self.get_empty_adjacent_positions(*position))
        return empty_adjacent_positions
    
    def is_position_taken(self, x, y):
        return (x, y) in self.get_tile_positions()