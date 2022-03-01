from __future__ import annotations

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from client.ihm.main.ihm_main_controller import IHMMainController
from common.interfaces.i_comm_calls_ihm_main import I_CommCallsIHMMain
from common import Profile


class CommCallsIHMMain_Impl(I_CommCallsIHMMain):

    """

    Implementation of Communications Calls IHM Main

    """

    def __init__(self, controller: IHMMainController):
        self.controller = controller

    def close_waiting_game(self) -> None:
        pass

    def display_user_profile(self, profile: Profile) -> None:
        pass

    def start_waiting_screen(self) -> None:
        self.controller.home_view.waiting_game_pop_up.show()
        pass

    def launch_spectate_game(self) -> None:
        pass

    def join_game_as_player(self) -> None:
        pass

    def launch_main(self) -> None:
        # connected_users = self.controller.get_my_interface_to_data().get_connected_player()
        # public_games = self.controller.my_interface_to_data.get_public_games()
        # find a way to pass that to the view
        self.controller.pygame_controller.show_view(self.controller.home_view)

    def notify_new_connected_user(self) -> None:
        pass

    def player_join_game(self) -> None:
        pass

    def notify_new_game(self) -> None:
        pass

    def notify_game_deleted(self) -> None:
        pass
