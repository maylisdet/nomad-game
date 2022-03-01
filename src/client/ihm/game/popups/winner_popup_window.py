import pygame_gui
import typing

from client.ihm.common.pop_up import PopUp
from client.ihm.game.components.winner_popup_container import (
    WinnerPopupComponent,
)

from pygame_gui.elements.ui_window import UIWindow


class WinnerPopupWindow(PopUp):
    def __init__(
        self, pygame_manager: pygame_gui.UIManager, ui, controller: typing.Any
    ):
        super(PopUp, self).__init__(pygame_manager, ui, controller)

        self.winner_pop_up_component = WinnerPopupComponent(pygame_manager)

        self.add(self.winner_pop_up_component)
