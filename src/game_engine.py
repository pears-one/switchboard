from board import Board

class GameEngine:
    def __init__(self, number_of_players, board, tile_repo):
        self.__number_of_players = number_of_players
        self.__board = board 
        self.__tile_repo = tile_repo
    
    def position_can_connect_to_board(self, x, y):
        above = self.__board.position_above(x, y)
        left = self.__board.position_to_left(x, y)
        below = self.__board.position_below(x, y)
        right = self.__board.position_to_right(x, y)
        if above in self.__board.get_tile_positions():
            tile = self.__board.get_tile_at_position(*above)
            can_connect = self.__tile_repo.get_tile(*tile["tile"]).bottom_is_playable(tile["rotation"])
            if can_connect: return True
        if below in self.__board.get_tile_positions():
            tile = self.__board.get_tile_at_position(*below)
            can_connect = self.__tile_repo.get_tile(*tile["tile"]).top_is_playable(tile["rotation"])
            if can_connect: return True
        if left in self.__board.get_tile_positions():
            tile = self.__board.get_tile_at_position(*left)
            can_connect = self.__tile_repo.get_tile(*tile["tile"]).right_is_playable(tile["rotation"])
            if can_connect: return True
        if right in self.__board.get_tile_positions():
            tile = self.__board.get_tile_at_position(*right)
            can_connect = self.__tile_repo.get_tile(*tile["tile"]).left_is_playable(tile["rotation"])
            if can_connect: return True
        return False
        
        
    def get_valid_tile_positions(self):
        return [
            position 
            for position 
            in self.__board.get_all_empty_adjacent_positions() 
            if self.position_can_connect_to_board(*position)
        ]      
            

