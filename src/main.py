from facade.facade import Facade
from lobby.manager import LobbyManager
from game.manager import GameManager
from service.service import Service


def main():
    lobby_manager = LobbyManager()
    game_manager = GameManager()
    service = Service(lobby_manager, game_manager)
    facade = Facade(service)
    facade.run(host='0.0.0.0')


if __name__ == "__main__":
    main()
