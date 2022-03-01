import pygame_gui
import typing

from client.ihm.common.pop_up import PopUp
from client.ihm.game.components.draw_popup_component import (
    DrawPopupComponent,
)

from pygame_gui.elements.ui_window import UIWindow


class DrawPopupWindow(PopUp):
    def __init__(
        self, pygame_manager: pygame_gui.UIManager, ui, controller: typing.Any
    ):
        super(PopUp, self).__init__(pygame_manager, ui, controller)

        self.draw_pop_up_component = DrawPopupComponent(pygame_manager)

        self.add(self.draw_pop_up_component)
