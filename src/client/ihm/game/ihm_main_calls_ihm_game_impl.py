from __future__ import annotations

from random import *
from typing import TYPE_CHECKING

from common import Move

if TYPE_CHECKING:
    from client.ihm.game.ihm_game_controller import IHMGameController
from common.interfaces.i_ihm_main_calls_ihm_game import I_IHMMainCallsIHMGame


class IHMMainCallsIHMGame_Impl(I_IHMMainCallsIHMGame):
    """

    Interface IHM Main Calls IHM Game

    """

    def __init__(self, controller: IHMGameController):
        self.controller = controller

    def launch_ihm_game(self) -> None:
        self.controller.set_game()
        self.controller.show_game_view()

    def launch_spectate_game(self) -> None:
        pass
