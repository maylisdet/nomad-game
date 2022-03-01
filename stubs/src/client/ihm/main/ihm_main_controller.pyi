import typing
from common.interfaces.i_comm_calls_ihm_main import I_CommCallsIHMMain as I_CommCallsIHMMain
from common.interfaces.i_ihm_game_calls_ihm_main import I_IHMGameCallsIHMMain as I_IHMGameCallsIHMMain
from common.interfaces.i_ihm_main_calls_comm import I_IHMMainCallsComm as I_IHMMainCallsComm
from common.interfaces.i_ihm_main_calls_ihm_game import I_IHMMainCallsIHMGame as I_IHMMainCallsIHMGame
from typing import Any

class IHMMainController:
    pygame_controller: Any
    my_interface_from_ihm_game: Any
    my_interface_from_comm: Any
    my_interface_to_comm: Any
    my_interface_to_ihm_game: Any
    initial_view: Any
    def __init__(self, pygame_controller: typing.Any, my_interface_from_ihm_game: I_IHMGameCallsIHMMain = ..., my_interface_from_comm: I_CommCallsIHMMain = ..., my_interface_to_comm: I_IHMMainCallsComm = ..., my_interface_to_ihm_game: I_IHMMainCallsIHMGame = ...) -> None: ...
    def set_my_interface_to_comm(self, i: I_IHMMainCallsComm) -> None: ...
    def set_my_interface_to_ihm_game(self, i: I_IHMMainCallsIHMGame) -> None: ...
    def get_my_interface_from_ihm_game(self) -> I_IHMGameCallsIHMMain: ...
    def get_my_interface_from_comm(self) -> I_CommCallsIHMMain: ...
