from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from client.ihm.main.ihm_main_controller import IHMMainController
from common.interfaces.i_ihm_game_calls_ihm_main import I_IHMGameCallsIHMMain


class IHMGameCallsIHMMain_Impl(I_IHMGameCallsIHMMain):

    """

    Interface IHM Game Calls IHM Main

    """

    def __init__(self, controller: IHMMainController):
        self.controller = controller

    def ihm_game_stoped(self) -> None:
        connected_users = (
            self.controller.get_my_interface_to_data().get_connected_players()
        )
        public_games = self.controller.get_my_interface_to_data().get_public_games()
        self.controller.home_view.games_list.set(public_games)
        self.controller.home_view.players_list.set(connected_users)
        self.controller.pygame_controller.show_view(self.controller.home_view)
        pass
