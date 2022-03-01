from __future__ import annotations

from typing import *
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from client.ihm.common.py_game_controller import PyGameController

from typing import Optional

from client.ihm.game.comm_calls_ihm_game_impl import CommCallsIHMGame_Impl
from client.ihm.game.ihm_main_calls_ihm_game_impl import IHMMainCallsIHMGame_Impl
from client.communication.com_controller import IHMGameCallsComm_Impl
from client.data.ihm_game_calls_data_impl import IhmGameCallsDataImpl
from client.ihm.game.views.game_view import GameView
from common.interfaces.i_ihm_game_calls_comm import I_IHMGameCallsComm
from common.interfaces.i_ihm_main_calls_ihm_game import I_IHMMainCallsIHMGame
from common.interfaces.i_ihm_game_calls_ihm_main import I_IHMGameCallsIHMMain
from common.interfaces.i_comm_calls_ihm_game import I_CommCallsIHMGame
from common.interfaces.i_ihm_game_calls_data import I_IHMGameCallsData

from common.data_structures.local_game import LocalGame
from common.data_structures.profiles import Profile, Player
from common.data_structures.player_type import PlayerType


class IHMGameController:
    def __init__(
        self,
        pygame_controller: PyGameController,  # no type because of circular import
    ):
        self.pygame_controller = pygame_controller
        self.my_interface_from_ihm_main = IHMMainCallsIHMGame_Impl(self)
        self.my_interface_from_comm = CommCallsIHMGame_Impl(self)
        self.my_interface_to_ihm_main: Optional[I_IHMGameCallsIHMMain] = None
        self.my_interface_to_data: Optional[I_IHMGameCallsData] = None
        self.my_interface_to_comm: Optional[I_IHMGameCallsComm] = None

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

    """
    Show / Hide Methods
    """

    def show_winner_window(self) -> None:
        self.game_view.winner_pop_up.show()

    def hide_winner_window(self) -> None:
        self.game_view.winner_pop_up.hide()

    def show_draw_window(self) -> None:
        self.game_view.draw_pop_up.show()

    def hide_draw_window(self) -> None:
        self.game_view.draw_pop_up.hide()

    def show_game_view(self):
        self.pygame_controller.show_view(self.game_view)

    """
    Set/Update Game View components
    """

    def set_game(self) -> None:
        self.set_game_board()
        self.set_players()
        self.define_current_player()
        self.set_spectators()
        self.game_view.tile_number.modify_text(str(self.local_game.tiles_remaining))

    def set_players(self):
        self.game_view.red_player.set_profile(
            self.get_my_interface_to_data().get_local_players()[0]
        )
        self.game_view.white_player.set_profile(
            self.get_my_interface_to_data().get_local_players()[1]
        )

    def define_current_player(self):
        if self.local_game.get_current_player() == self.local_game.white_player:
            self.game_view.turn_player.to_white_player()
        else:
            self.game_view.turn_player.to_red_player()

    def set_spectators(self):
        self.spectators = self.get_my_interface_to_data().get_local_game_spectators()

        self.game_view.spectator_number.modify_text(str(len(self.spectators)))

    def set_game_board(self):
        self.local_game = self.get_my_interface_to_data().get_local_game()
        self.game_view.grid_panel.set_board(self.local_game.board)

    def update_game_board(self, board: Dict[str, Tuple[str, int]]):
        self.game_view.grid_panel.set_board(board)

    def update_tile_number(self):
        self.game_view.tile_number.modify_text(str(self.local_game.tiles_remaining))

    """
    Interfaces
    """

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

    def get_my_interface_to_comm(self) -> I_IHMGameCallsComm:
        if self.my_interface_to_comm is not None:
            return self.my_interface_to_comm
        else:
            raise Exception(
                "get_my_interface_to_comm was called but my_interface_to_comm is None"
            )

    def get_my_interface_to_ihm_main(self) -> I_IHMGameCallsIHMMain:
        if self.my_interface_to_ihm_main is not None:
            return self.my_interface_to_ihm_main
        else:
            raise Exception(
                "my_interface_to_ihm_main was called but my_interface_to_ihm_main is None"
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
