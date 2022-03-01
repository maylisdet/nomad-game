from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from client.ihm.game.ihm_game_controller import IHMGameController
from common.interfaces.i_comm_calls_ihm_game import I_CommCallsIHMGame
from client.ihm.game.views.game_view import GameView


class CommCallsIHMGame_Impl(I_CommCallsIHMGame):

    """

    Interface Comm Calls IHM Game

    """

    def __init__(self, controller: IHMGameController):
        self.controller = controller

    def notify_new_spectator(self) -> None:
        pass

    def spectator_quits_game(self) -> None:
        pass

    def update_game(self) -> None:
        local_game = self.controller.my_interface_to_data.get_local_game()
        if self.controller.my_interface_to_data.is_local_game_finished():
            print("Game finished -> Show POPUP ")
        else:
            self.controller.game_view.grid_panel.set_board(local_game.board)
            self.controller.game_view.tile_number.modify_text(
                str(local_game.tiles_remaining)
            )

            if (
                self.controller.local_game.get_current_player()
                == self.controller.local_game.white_player
            ):
                self.controller.game_view.turn_player.to_white_player()
            else:
                self.controller.game_view.turn_player.to_red_player()

    def notify_new_message(self) -> None:
        pass
