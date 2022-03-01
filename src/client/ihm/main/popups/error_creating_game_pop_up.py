import pygame_gui
import typing

from client.ihm.common.pop_up import PopUp
from client.ihm.main.components.pop_up_error_creating_game.window_error_creating_game import (
    WindowErrorCreatingGame,
)
from client.ihm.main.components.pop_up_error_creating_game.close_error_creating_game import (
    CloseErrorCreatingGame,
)

from pygame_gui.elements.ui_window import UIWindow


class ErrorCreatingGamePopUp(PopUp):
    def __init__(
        self, pygame_manager: pygame_gui.UIManager, ui, controller: typing.Any
    ):
        super(PopUp, self).__init__(pygame_manager, ui, controller)

        self.window_waiting_game = WindowErrorCreatingGame(pygame_manager)
        self.close_button = CloseErrorCreatingGame(pygame_manager)

        self.add(self.window_waiting_game)
        self.add(self.close_button)
