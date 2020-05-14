from board import Board

class BoardAnalyser:
    def __init__(self, number_of_players, board, tile_repo):
        self.__number_of_players = number_of_players
        self.__board = board 
        self.__tile_repo = tile_repo
    
    def position_can_connect_to_tiles(self, x, y):
        can_connect = []
        above = self.__board.position_above(x, y)
        left = self.__board.position_to_left(x, y)
        below = self.__board.position_below(x, y)
        right = self.__board.position_to_right(x, y)
        if above in self.__board.get_tile_positions():
            tile = self.__board.get_tile_at_position(*above)
            if self.__tile_repo.get_tile(*tile["tile"]).bottom_is_playable(tile["rotation"]): can_connect.append('above')
        if below in self.__board.get_tile_positions():
            tile = self.__board.get_tile_at_position(*below)
            if self.__tile_repo.get_tile(*tile["tile"]).top_is_playable(tile["rotation"]): can_connect.append('below')
        if left in self.__board.get_tile_positions():
            tile = self.__board.get_tile_at_position(*left)
            if self.__tile_repo.get_tile(*tile["tile"]).right_is_playable(tile["rotation"]): can_connect.append('left')
        if right in self.__board.get_tile_positions():
            tile = self.__board.get_tile_at_position(*right)
            if self.__tile_repo.get_tile(*tile["tile"]).left_is_playable(tile["rotation"]): can_connect.append('right')
        return can_connect 

    def is_move_valid(self, from_x, from_y, to_x, to_y, rotation):
        tile_to_move = self.__tile_repo.get_tile(*self.__board.get_tile_at_position(from_x, from_y)["tile"])
        if self.__board.is_position_taken(to_x, to_y):
            return False
        for direction in self.position_can_connect_to_tiles(to_y, to_x):
            if direction == 'above' and tile_to_move.bottom_is_playable(rotation):
                return True
            if direction == 'below' and tile_to_move.top_is_playable(rotation):
                return True
            if direction == 'left' and tile_to_move.right_is_playable(rotation):
                return True
            if direction == 'right' and tile_to_move.left_is_playable(rotation):
                return True
        return False
        
        