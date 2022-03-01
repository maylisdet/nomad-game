from typing import List, Union
from uuid import *
from common import LocalGame, Player
from common.data_structures.profiles import Profile

from server.data.comm_server_calls_data_impl import CommServerCallsDataImpl
from common.interfaces.i_comm_server_calls_data import I_CommServerCallsData


class DataServerController:
    def __init__(self):
        self.my_interface_from_comm_server = CommServerCallsDataImpl(self)

        self.game_list: List[LocalGame] = []
        self.profile_list: List[Profile] = []

    def get_my_interface_from_comm_server(self) -> I_CommServerCallsData:
        return self.my_interface_from_comm_server

    def get_game(self, game_uuid: UUID) -> LocalGame:
        for game in self.game_list:
            if game_uuid == game.uuid:
                return game
        raise Exception("game not found in list")

    def get_player(self, profile_uuid: UUID) -> Profile:
        for profile in self.profile_list:
            if profile_uuid == profile.uuid:
                return profile
        raise Exception("player not found in list")

    def find_game_with_uuid(self, game_uuid: UUID) -> Union[LocalGame, None]:
        for game in self.game_list:
            if game.uuid == game_uuid:
                return game
        return None

    def find_player_with_uuid(self, player_id: UUID) -> Union[Profile, None]:
        for player in self.profile_list:
            if player.uuid == player_id:
                return player
        return None
