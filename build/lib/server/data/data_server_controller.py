from typing import List
from common import PublicGame, Player

from server.data.comm_server_calls_data_impl import CommServerCallsDataImpl
from common.interfaces.i_comm_server_calls_data import I_CommServerCallsData


class DataServerController:
    def __init__(self):
        self.my_interface_from_comm_server = CommServerCallsDataImpl(self)

        self.game_list: List[PublicGame] = []
        self.player_list: List[Player] = []

    def get_my_interface_from_comm_server(self) -> I_CommServerCallsData:
        return self.my_interface_from_comm_server
