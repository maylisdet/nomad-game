from __future__ import annotations

from typing import TYPE_CHECKING, List, Tuple

from common import LocalGame, Player, Profile

if TYPE_CHECKING:
    from client.ihm.common.py_game_controller import PyGameController

from typing import Optional

from client.ihm.game.comm_calls_ihm_game_impl import CommCallsIHMGame_Impl
from client.ihm.game.ihm_main_calls_ihm_game_impl import IHMMainCallsIHMGame_Impl
from client.data.ihm_game_calls_data_impl import IhmGameCallsDataImpl
from client.communication.com_controller import IHMGameCallsComm_Impl

from client.ihm.game.views.game_view import GameView
from common.interfaces.i_ihm_game_calls_comm import I_IHMGameCallsComm
from common.interfaces.i_ihm_main_calls_ihm_game import I_IHMMainCallsIHMGame
from common.interfaces.i_ihm_game_calls_ihm_main import I_IHMGameCallsIHMMain
from common.interfaces.i_comm_calls_ihm_game import I_CommCallsIHMGame
from common.interfaces.i_ihm_game_calls_data import I_IHMGameCallsData


class IHMGameController:
    def __init__(
        self,
        pygame_controller: PyGameController,  # no type because of circular import
    ):
        self.pygame_controller = pygame_controller
        self.my_interface_from_ihm_main = IHMMainCallsIHMGame_Impl(self)
        self.my_interface_from_comm = CommCallsIHMGame_Impl(self)
        self.my_interface_to_ihm_main: Optional[I_IHMGameCallsIHMMain] = None
        self.my_interface_to_data = IhmGameCallsDataImpl()
        self.my_interface_to_comm = IHMGameCallsComm_Impl(I_IHMGameCallsComm)

        # initialize the game view
        self.game_view = GameView(
            pygame_controller.get_ui_manager(),
            pygame_controller.get_ui_renderer(),
            self,
        )

        # Games Variables
        self.local_game: LocalGame
        self.local_players: Tuple[Profile, Profile]
        self.spectators: List[Player]

        # self.my_interface_from_ihm_main.launch_ihm_game()
        # pygame_controller.show_view(self.game_view)

    def set_my_interface_to_ihm_main(self, i: I_IHMGameCallsIHMMain) -> None:
        self.my_interface_to_ihm_main = i

    def set_my_interface_to_data(self, i: IhmGameCallsDataImpl) -> None:
        self.my_interface_to_data = i

    def set_my_interface_to_comm(self, i: IHMGameCallsComm_Impl) -> None:
        self.my_interface_to_comm = i

    def get_my_interface_to_data(self) -> I_IHMGameCallsData:
        if self.my_interface_to_data is not None:
            return self.my_interface_to_data
        else:
            raise Exception(
                "get_my_interface_to_data was called but my_interface_to_data is None"
            )

    def get_my_interface_to_comm(self) -> IHMGameCallsComm_Impl:
        if self.my_interface_to_comm is not None:
            return self.my_interface_to_comm
        else:
            raise Exception(
                "get_my_interface_to_comm was called but my_interface_to_comm is None"
            )

    def get_my_interface_from_ihm_main(self) -> I_IHMMainCallsIHMGame:
        if self.my_interface_from_ihm_main is not None:
            return self.my_interface_from_ihm_main
        else:
            raise Exception(
                "get_my_interface_from_ihm_main was called but my_interface_from_ihm_main is None"
            )

    def get_my_interface_from_comm(self) -> I_CommCallsIHMGame:
        if self.my_interface_from_comm is not None:
            return self.my_interface_from_comm
        else:
            raise Exception(
                "get_my_interface_from_comm was called but my_interface_from_comm is None"
            )
