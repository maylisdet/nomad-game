from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from client.ihm.game.ihm_game_controller import IHMGameController
from common.interfaces.i_comm_calls_ihm_game import I_CommCallsIHMGame


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
        print("handle_move\n")
        local_game = self.controller.get_my_interface_to_data().get_local_game()
        self.controller.local_game = local_game
        self.controller.update_game_board(local_game.board)
        self.controller.update_tile_number()
        self.controller.define_current_player()
        self.controller.show_game_view()
        if self.controller.get_my_interface_to_data().is_local_game_finished():
            print("game finished detected\n")
            if (
                len(self.controller.get_my_interface_to_data().get_local_game_winner())
                == 2
            ):
                self.controller.pygame_controller.update_component(
                    self.controller.game_view.draw_pop_up.draw_pop_up_component
                )
                # self.controller.show_winner_window()
                self.controller.show_game_view()
                self.controller.show_draw_window()
                print("draw")
            else:
                winner = (
                    self.controller.get_my_interface_to_data()
                    .get_local_game_winner()[0]
                    .convertToPlayer()
                )
                winner_component = (
                    self.controller.game_view.winner_pop_up.winner_pop_up_component
                )
                winner_component.set_winner(winner)
                self.controller.pygame_controller.update_component(winner_component)
                self.controller.show_game_view()
                self.controller.show_winner_window()
                print("winner")

    def notify_new_message(self) -> None:
        # On met à jour la local_game
        local_game = self.controller.get_my_interface_to_data().get_local_game()
        self.controller.local_game = local_game
        html_messages = ""
        for message in local_game.get_chat():
            if message.player is not None:
                if (
                    message.player.uuid
                    == self.controller.get_my_interface_to_data()
                    .get_local_players()[0]
                    .uuid
                ):
                    msg_str = (
                        "<b><font color='#ff0000' size=3.5>"
                        + message.player.nickname
                        + "</font></b>: "
                    )
                else:
                    msg_str = (
                        "<b><font color='#000000' size=3.5>"
                        + message.player.nickname
                        + "</font></b>: "
                    )

                msg_str += message.message
                msg_str += "<br>"
                html_messages += msg_str

        self.controller.game_view.chat_component.set_html_messages_content(
            html_messages
        )
        self.controller.show_game_view()
