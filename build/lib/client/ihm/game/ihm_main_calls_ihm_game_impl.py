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
        self.controller.local_game = (
            self.controller.get_my_interface_to_data().get_local_game()
        )
        self.controller.local_players = (
            self.controller.get_my_interface_to_data().get_local_players()
        )
        self.controller.game_view.red_player.set_profile(
            self.controller.local_players[0]
        )
        self.controller.game_view.white_player.set_profile(
            self.controller.local_players[1]
        )

        self.controller.spectators = (
            self.controller.get_my_interface_to_data().get_local_game_spectators()
        )

        self.controller.game_view.spectator_number.modify_text(
            str(len(self.controller.spectators))
        )

        if (
            self.controller.local_game.get_current_player()
            == self.controller.local_game.white_player
        ):
            self.controller.game_view.turn_player.to_white_player()
        else:
            self.controller.game_view.turn_player.to_red_player()

        ##### TESTS ########
        a_move: Move

        for i in range(5):
            keys = [i for i in self.controller.local_game.valid_moves_tower()]
            a_move = Move(
                self.controller.local_game.get_uuid(),
                self.controller.local_game.get_current_player(),
                keys[randint(0, len(keys) - 1)],
                "Tower",
            )
            if self.controller.local_game.check_move_in_local_game(a_move):
                self.controller.local_game.add_move(a_move)

        for i in range(120):
            keys = [i for i in self.controller.local_game.valid_moves_pown()]
            a_move = Move(
                self.controller.local_game.get_uuid(),
                self.controller.local_game.get_current_player(),
                keys[randint(0, len(keys) - 1)],
                "Pown",
            )
            if self.controller.local_game.check_move_in_local_game(a_move):
                self.controller.local_game.add_move(a_move)

        print(self.controller.local_game)
        self.controller.game_view.tile_number.modify_text(
            str(self.controller.local_game.tiles_remaining)
        )

        self.controller.game_view.grid_panel.set_board(self.controller.local_game.board)

    def launch_spectate_game(self) -> None:
        pass
