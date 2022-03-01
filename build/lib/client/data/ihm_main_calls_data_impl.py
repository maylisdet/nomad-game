from __future__ import annotations

from typing import List
import uuid as uuid_lib
from common import Profile, LocalGame, Player, User

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from client.data.data_controller import DataController

from common.interfaces.i_ihm_main_calls_data import I_IHMMainCallsData


class IhmMainCallsDataImpl(I_IHMMainCallsData):
    def __init__(self, data_controller: DataController):
        self.data_controller = data_controller

    def get_public_games(self) -> List:
        return self.data_controller.public_games

    def get_connected_players(self) -> List[Player]:
        return self.data_controller.connected_players

    def get_local_game_id(self) -> uuid_lib.UUID:
        pass

    def get_profile(self) -> Profile:
        pass

    def create_new_profile(self, user: User) -> None:
        pass

    def create_game(self, name: str, tiles: int) -> LocalGame:
        pass

    def export_current_profile(self, destination_path: str) -> None:
        pass

    def import_profile(self, path: str) -> Profile:
        pass

    def edit_current_profile(self, profile: Profile) -> None:
        pass

    def disconnect_from_app(self) -> None:
        pass

    def disconnect_server(self) -> None:
        pass

    def connect_to_app(self, nickname: str, password: str) -> None:
        pass
