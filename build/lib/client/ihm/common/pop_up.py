import typing
from typing import List

import pygame_gui

from client.ihm.common.window import Window
from client.ihm.common.component import Component


class PopUp(Window):
    def __init__(
        self,
        pygame_manager: pygame_gui.UIManager,
        ui,
        controller: typing.Any,
        width=None,
        height=None,
        pos_x=None,
        pos_y=None,
    ):
        super(PopUp, self).__init__(pygame_manager, ui, controller)

        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.isVisible = False
        self.window: pygame_gui.elements.UIWindow = None

    def render(self):
        super(PopUp, self).render()

        self.hide()

    def show(self):
        self.isVisible = True

        for component in self.components:
            component.gui_element.show()

    def hide(self):

        self.isVisible = False

        for component in self.components:
            component.gui_element.hide()

    def get_width(self) -> int:
        if self.width is not None:
            return self.width
        else:
            raise NotImplementedError(
                "The width of this component has not been implemented yet"
            )

    def get_height(self) -> int:
        if self.height is not None:
            return self.height
        else:
            raise NotImplementedError(
                "The height of this component has not been implemented yet"
            )

    def get_pos_x(self) -> int:
        if self.pos_x is not None:
            return self.pos_x
        else:
            raise NotImplementedError(
                "The pos_x of this component has not been implemented yet"
            )

    def get_pos_y(self) -> int:
        if self.pos_y is not None:
            return self.pos_y
        else:
            raise NotImplementedError(
                "The pos_y of this component has not been implemented yet"
            )

    def set_width(self, value: int) -> None:
        self.width = value

    def set_height(self, value: int) -> None:
        self.height = value

    def set_pos_x(self, value: int) -> None:
        self.pos_x = value

    def set_pos_y(self, value: int) -> None:
        self.pos_y = value

    def set_window(self, window: pygame_gui.elements.UIWindow) -> None:
        self.window = window
        print(self.window)
