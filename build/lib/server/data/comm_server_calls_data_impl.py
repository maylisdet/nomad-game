from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from server.data.data_server_controller import DataServerController
from typing import List, Tuple
import uuid as uuid_lib
from common import (
    LocalGame,
    PublicGame,
    Player,
    Profile,
    Move,
    Message,
    I_CommServerCallsData,
)


class CommServerCallsDataImpl(I_CommServerCallsData):
    def __init__(self, data_server_controller: DataServerController):
        self.data_server_controller = data_server_controller

    def create_game(self, local_game: LocalGame) -> PublicGame:
        # self.data_server_controller.game_list.append(local_game)
        pass

    def get_players(self) -> List:
        return self.data_server_controller.player_list

    def get_available_games(self) -> List:
        available_games_list: List[PublicGame] = []
        for games in self.data_server_controller.game_list:
            if games.status == "available":
                available_games_list.append(games)
        return available_games_list

    def add_user(self, profile: Profile) -> Player:
        new_player = Player(profile.nickname, profile.uuid)
        if new_player not in self.data_server_controller.player_list:
            self.data_server_controller.player_list.append(new_player)
        else:
            pass  # See how to handle errors
        return new_player

    def add_spectator_to_game(
        self, user_id: uuid_lib.UUID, game_id: uuid_lib.UUID
    ) -> LocalGame:
        pass

    def delete_spectator_from_game(
        self, user_id: uuid_lib.UUID, game_id: uuid_lib.UUID
    ) -> None:
        pass

    def get_game_spectators(self, game_id: uuid_lib.UUID) -> List[Player]:
        pass

    def get_game_players(self, game_id: uuid_lib.UUID) -> List[Player]:
        pass

    def delete_game(self, game_id: uuid_lib.UUID) -> None:
        pass

    def add_player_to_game(
        self, game_id: uuid_lib.UUID, user_id: uuid_lib.UUID
    ) -> LocalGame:
        pass

    def get_profile(self, user_id: uuid_lib.UUID) -> Profile:
        pass

    def add_move(self, move: Move) -> None:
        pass

    def is_game_finished(self, game_id: uuid_lib.UUID) -> bool:
        pass

    def apply_result_to_profile(
        self, game_id: uuid_lib.UUID
    ) -> Tuple[Profile, Profile]:
        pass

    def add_message_to_game(self, game_id: uuid_lib.UUID, message: Message) -> None:
        pass

    def update_profile(self, profile: Profile) -> None:
        pass

    def delete_user(self, user_id: uuid_lib.UUID) -> None:
        pass
