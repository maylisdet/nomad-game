from __future__ import annotations

from common.interfaces.i_comm_calls_data import I_CommCallsData

from typing import List, Union
import uuid as uuid_lib
from common import LocalGame, Player, PublicGame, Move, Message, Profile


from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from client.data.data_controller import DataController


class CommCallsDataImpl(I_CommCallsData):
    def __init__(self, data_controller: DataController):
        self.data_controller = data_controller

    def store_connected_user(self, players: List):
        for player in players:
            if player not in self.data_controller.connected_players:
                self.data_controller.connected_players.append(player)

    def store_games(self, games: List):
        for game in games:
            if game not in self.data_controller.public_games:
                self.data_controller.public_games.append(game)

    def add_connected_user(self, player: Player):
        if player not in self.data_controller.connected_players:
            self.data_controller.connected_players.append(player)

    def store_new_game(self, public_game: PublicGame):
        if public_game not in self.data_controller.public_games:
            self.data_controller.public_games.append(public_game)

    def player_join_game(self, player: Union[Player, None]):
        if self.data_controller.local_game is not None:
            if self.data_controller.local_game.red_player is None:
                self.data_controller.local_game.red_player = player
            elif self.data_controller.local_game.white_player is None:
                self.data_controller.local_game.white_player = player

    def update_public_game(self, public_games: PublicGame):
        self.data_controller.public_games.append(public_games)

    def remove_local_game(self) -> None:
        pass

    def store_current_game(self, local_game: LocalGame) -> None:
        pass

    def store_local_game(self, local_game: LocalGame) -> None:
        pass

    def add_spectator_in_game(self, player: Player) -> None:
        pass

    def remove_disconnect_player(self, user_id: uuid_lib.UUID) -> None:
        pass

    def remove_spectator(self, user_id: uuid_lib.UUID) -> None:
        pass

    def add_move_to_local_game(self, move: Move, game_finished: bool) -> None:
        pass

    def add_new_message(self, message: Message) -> None:
        pass

    def remove_pending_game(self, game_id: uuid_lib.UUID) -> None:
        pass

    def update_user_profile(self, profile: Profile) -> None:
        pass

    def get_profile(self) -> Profile:
        return Profile("user", "127.0.0.1", 8080)
