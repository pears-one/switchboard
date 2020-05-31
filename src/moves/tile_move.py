from board.tile_position import TilePosition


class TileMove:
    def __init__(self, from_pos: TilePosition, to_pos: TilePosition, rotation):
        self.__from_pos = from_pos
        self.__to_pos = to_pos
        self.__rotation = rotation

    def get_rotation(self):
        return self.__rotation

    def get_to_pos(self):
        return self.__to_pos

    def get_from_pos(self):
        return self.__from_pos

    @classmethod
    def unmarshal(cls, move_dict):
        return cls(
            TilePosition.unmarshal(move_dict["from"]),
            TilePosition.unmarshal(move_dict["to"]),
            move_dict["rotation"]
        )
