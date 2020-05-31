from flask import Flask, request, make_response
from players.new_player import NewPlayer
from service.service import Service
from moves.tile_move import TileMove
from players.piece_position import PiecePosition


class Facade:
    def __init__(self, service: Service):
        self.__service = service
        self.app = Flask(__name__)
        self.app.add_url_rule('/', None, self.health_check, methods=["GET"])
        self.app.add_url_rule('/lobby', None, self.new_lobby, methods=["POST"])
        self.app.add_url_rule('/lobby/<group_code>', None, self.manage_lobby, methods=["PUT", "GET"])
        self.app.add_url_rule('/game/<group_code>', None, self.manage_game, methods=["GET", "POST"])
        self.app.add_url_rule('/game/<group_code>/tile-move', None, self.move_tile, methods=["POST"])
        self.app.add_url_rule('/game/<group_code>/piece-move', None, self.move_piece, methods=["POST"])
        self.app.add_url_rule('/game/<group_code>/roll-dice', None, self.roll, methods=["POST"])

    @staticmethod
    def health_check():
        return "Welcome to Switchboard"

    def move_tile(self, group_code):
        response = make_response()
        tile_move = TileMove.unmarshal(request.get_json())
        if not self.__service.game_exists(group_code):
            response.status_code = 404  # Game doesn't exist
        elif self.__service.get_current_player_cookie(group_code) != request.cookies["player"]:
            response.status_code = 401  # Not this player's turn
        elif self.__service.move_tile(group_code, tile_move):
            response.status_code = 200  # Move Successful
        else:
            response.status_code = 400  # invalid move
        return response

    def roll(self, group_code):
        response = make_response()
        if not self.__service.game_exists(group_code):
            response.status_code = 404  # Game doesn't exist
        elif self.__service.get_current_player_cookie(group_code) != request.cookies["player"]:
            response.status_code = 401  # Not this player's turn
        elif self.__service.roll(group_code):
            response.status_code = 200  # Roll successful
        else:
            response.status_code = 400  # Not this move phase
        return response

    def move_piece(self, group_code):
        response = make_response()
        to_position = PiecePosition.unmarshal(request.get_json())
        if not self.__service.game_exists(group_code):
            response.status_code = 404  # Game doesn't exist
        elif self.__service.get_current_player_cookie(group_code) != request.cookies["player"]:
            response.status_code = 401  # Not this player's turn
        elif self.__service.move_piece(group_code, to_position):
            response.status_code = 200  # Move Successful
        else:
            response.status_code = 400  # invalid move
        return response

    def new_lobby(self):
        request_body = request.get_json()
        first_player = NewPlayer.from_name(request_body["name"])
        group_code = self.__service.new_lobby(first_player)
        response = make_response({"code": group_code})
        response.status_code = 200
        response.set_cookie("player", first_player.get_cookie())
        return response

    def manage_game(self, group_code):
        if request.method == "POST":
            self.__service.start_game(group_code)
            response = make_response({"code": group_code})
            response.status_code = 200
            return response
        else:
            if not self.__service.game_exists(group_code):
                response = make_response()
                response.status_code = 404  # Game doesn't exist
            response = make_response(self.__service.get_game_data(group_code))
            response.status_code = 200
            return response

    def manage_lobby(self, group_code):
        if request.method == "PUT":
            request_body = request.get_json()
            new_player = NewPlayer.from_name(request_body["name"])
            self.__service.add_player_to_lobby(group_code, new_player)
            response = make_response({"code": group_code})
            response.status_code = 200
            response.set_cookie("player", new_player.get_cookie())
            return response
        else:
            player_list = [player.marshal() for player in self.__service.get_players_in_lobby(group_code)]
            response = make_response({"players": player_list})
            response.status_code = 200
            return response

    def run(self, *args, **kwargs):
        self.app.run(*args, **kwargs)


