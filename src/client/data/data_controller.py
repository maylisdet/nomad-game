from typing import List, Optional
from common import PublicGame, Player, LocalGame, User

from client.data.comm_calls_data_impl import CommCallsDataImpl
from client.data.ihm_game_calls_data_impl import IhmGameCallsDataImpl
from client.data.ihm_main_calls_data_impl import IhmMainCallsData_Impl

from common.interfaces.i_ihm_main_calls_data import I_IHMMainCallsData
from common.interfaces.i_ihm_game_calls_data import I_IHMGameCallsData
from common.interfaces.i_comm_calls_data import I_CommCallsData


class DataController:
    def __init__(self):
        self.my_interface_from_ihm_game = IhmGameCallsDataImpl(self)
        self.my_interface_from_ihm_main = IhmMainCallsData_Impl(self)
        self.my_interface_from_comm = CommCallsDataImpl(self)

        self.connected_players: List[Player] = []
        self.public_games: List[PublicGame] = []
        self.local_game: Optional[LocalGame] = None
        self.myself: Optional[User] = None

    def get_my_interface_from_ihm_game(self) -> I_IHMGameCallsData:
        return self.my_interface_from_ihm_game

    def get_my_interface_from_ihm_main(self) -> I_IHMMainCallsData:
        return self.my_interface_from_ihm_main

    def get_my_interface_from_comm(self) -> I_CommCallsData:
        return self.my_interface_from_comm
