import pygame_gui
import typing

from client.ihm.common.pop_up import PopUp
from client.ihm.game.components.move_not_possible_component import (
    MoveNotPossibleComponent,
)

from pygame_gui.elements.ui_window import UIWindow


class MoveNotPossibleWindow(PopUp):
    def __init__(
        self, pygame_manager: pygame_gui.UIManager, ui, controller: typing.Any
    ):
        super(PopUp, self).__init__(pygame_manager, ui, controller)

        self.move_not_possible_component = MoveNotPossibleComponent(pygame_manager)

        self.add(self.move_not_possible_component)
