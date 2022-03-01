import typing
import pygame
import pygame_gui
from client.ihm.common.ui_renderer import UIRenderer
from client.ihm.common.view import View
from client.ihm.game.components.pass_turn_button import PassTurnButton
from client.ihm.game.components.spectator_number_container import (
    SpectatorNumberContainer,
)
from client.ihm.game.components.tile_number_container import TileNumberContainer
from client.ihm.game.components.red_player_container import RedPlayerContainer
from client.ihm.game.components.white_player_container import WhitePlayerContainer
from client.ihm.game.components.chat_component import ChatComponent
from client.ihm.game.components.grid_panel import GridPanel
from client.ihm.game.components.turn_player import TurnPlayer
from client.ihm.game.components.popups.move_not_possible_window import (
    MoveNotPossibleWindow,
)

# from client.ihm.main.ihm_main_controller import IHMMainController


class GameView(View):
    def __init__(
        self,
        pygame_manager: pygame_gui.UIManager,
        ui: UIRenderer,
        controller: typing.Any,
    ):
        super().__init__(pygame_manager, ui, controller)

        self.pass_turn = PassTurnButton(pygame_manager)
        self.spectator_number = SpectatorNumberContainer(pygame_manager)
        self.tile_number = TileNumberContainer(pygame_manager)
        self.white_player = RedPlayerContainer(pygame_manager)
        self.red_player = WhitePlayerContainer(pygame_manager)
        self.chat_component = ChatComponent(pygame_manager)
        self.grid_panel = GridPanel(pygame_manager)
        self.turn_player = TurnPlayer(pygame_manager)

        self.move_not_possible_pop_up = MoveNotPossibleWindow(
            pygame_manager, ui, controller
        )

        self.add(self.grid_panel)
        self.add(self.spectator_number)
        self.add(self.tile_number)
        self.add(self.white_player)
        self.add(self.red_player)
        self.add(self.chat_component)
        self.add(self.turn_player)
        self.add(self.pass_turn)

        self.add_pop_up(self.move_not_possible_pop_up)
