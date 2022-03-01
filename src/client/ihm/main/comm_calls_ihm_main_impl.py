from __future__ import annotations

from typing import TYPE_CHECKING

from common.utils import threaded

if TYPE_CHECKING:
    from client.ihm.main.ihm_main_controller import IHMMainController
from common.interfaces.i_comm_calls_ihm_main import I_CommCallsIHMMain
from common import Profile
from common import LocalGame
from typing import List
from common.data_structures.profiles import Player


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

    def start_waiting_screen(self, local_game: LocalGame) -> None:
        self.controller.home_view.waiting_game_pop_up.window_waiting_game.set_game_info(
            local_game
        )
        self.controller.home_view.waiting_game_pop_up.show()

    def launch_spectate_game(self) -> None:
        pass

    def join_game_as_player(self) -> None:
        self.controller.get_my_interface_to_ihm_game().launch_ihm_game()

    def launch_main(self) -> None:
        connected_users = (
            self.controller.get_my_interface_to_data().get_connected_players()
        )
        public_games = self.controller.get_my_interface_to_data().get_public_games()
        self.controller.home_view.games_list.set(public_games)
        self.controller.home_view.players_list.set(connected_users)
        self.controller.pygame_controller.show_view(self.controller.home_view)

    def notify_new_connected_user(self) -> None:
        if (
            self.controller.pygame_controller.get_current_view()
            != self.controller.home_view
        ):
            return
        connected_users = (
            self.controller.get_my_interface_to_data().get_connected_players()
        )
        self.controller.home_view.players_list.set(connected_users)
        self.controller.pygame_controller.update_component(
            self.controller.home_view.players_list
        )

    def player_join_game(self) -> None:
        self.controller.get_my_interface_to_ihm_game().launch_ihm_game()

    def notify_new_game(self) -> None:
        if (
            self.controller.pygame_controller.get_current_view()
            != self.controller.home_view
        ):
            return
        public_games = self.controller.get_my_interface_to_data().get_public_games()
        games_list = self.controller.home_view.games_list
        games_list.set(public_games)
        self.controller.pygame_controller.update_component(games_list)

    def notify_game_deleted(self) -> None:
        if (
            self.controller.pygame_controller.get_current_view()
            != self.controller.home_view
        ):
            return
        public_games = self.controller.get_my_interface_to_data().get_public_games()
        games_list = self.controller.home_view.games_list
        games_list.set(public_games)
        self.controller.pygame_controller.update_component(games_list)

    def notify_list_player_changed(self) -> None:

        players = self.controller.get_my_interface_to_data().get_connected_players()

        # Render New Users

        player_list = self.controller.home_view.players_list
        player_list.set(players)

        self.controller.pygame_controller.update_component(player_list)

        return
