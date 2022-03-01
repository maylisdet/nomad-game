import typing
from common.interfaces.i_comm_calls_ihm_game import I_CommCallsIHMGame as I_CommCallsIHMGame
from common.interfaces.i_ihm_game_calls_comm import I_IHMGameCallsComm as I_IHMGameCallsComm
from common.interfaces.i_ihm_game_calls_ihm_main import I_IHMGameCallsIHMMain as I_IHMGameCallsIHMMain
from common.interfaces.i_ihm_main_calls_ihm_game import I_IHMMainCallsIHMGame as I_IHMMainCallsIHMGame
from typing import Any

class IHMGameController:
    pygame_controller: Any
    my_interface_from_ihm_main: Any
    my_interface_from_comm: Any
    my_interface_to_comm: Any
    my_interface_to_ihm_main: Any
    game_view: Any
    def __init__(self, pygame_controller: typing.Any, my_interface_from_ihm_main: I_IHMMainCallsIHMGame = ..., my_interface_from_comm: I_CommCallsIHMGame = ..., my_interface_to_comm: I_IHMGameCallsComm = ..., my_interface_to_ihm_main: I_IHMGameCallsIHMMain = ...) -> None: ...
    def set_my_interface_to_comm(self, i: I_IHMGameCallsComm) -> None: ...
    def set_my_interface_to_ihm_main(self, i: I_IHMGameCallsIHMMain) -> None: ...
    def get_my_interface_from_ihm_main(self) -> I_IHMMainCallsIHMGame: ...
    def get_my_interface_from_comm(self) -> I_CommCallsIHMGame: ...
