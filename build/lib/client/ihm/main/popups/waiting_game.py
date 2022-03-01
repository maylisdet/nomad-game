import pygame_gui
import typing

from client.ihm.common.pop_up import PopUp
from client.ihm.main.components.pop_up_waiting_game.window_waiting_game import (
    WindowWaitingGame,
)

from pygame_gui.elements.ui_window import UIWindow


class WaitingGame(PopUp):
    def __init__(
        self, pygame_manager: pygame_gui.UIManager, ui, controller: typing.Any
    ):
        super(PopUp, self).__init__(pygame_manager, ui, controller)

        self.window_waiting_game = WindowWaitingGame(pygame_manager)

        self.add(self.window_waiting_game)
