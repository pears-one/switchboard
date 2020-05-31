from utils.functions import random_string


class NewPlayer:
    def __init__(self, name, cookie):
        self.__name = name
        self.__cookie = cookie

    def get_cookie(self):
        return self.__cookie

    def get_name(self):
        return self.__name

    @classmethod
    def from_name(cls, name):
        cookie = random_string()
        return cls(name, cookie)

    def marshal(self):
        return {"name": self.get_name(), "cookie": self.get_cookie()}

    @classmethod
    def unmarshal(cls, player_dict):
        return cls(player_dict["name"], player_dict["cookie"])

