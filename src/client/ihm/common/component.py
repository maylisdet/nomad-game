import typing

import pygame.event
import pygame_gui.core


from typing import Any


class Component:
    def __init__(
        self,
        pygame_manager: pygame_gui.UIManager,
        width=None,
        height=None,
        pos_x=None,
        pos_y=None,
    ):
        self.manager = pygame_manager
        self.width = width
        self.height = height
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.container: Any = None
        self.gui_element: Any = None
        self.controller: Any = None

    def set_controller(self, controller: typing.Any):
        self.controller = controller

    def render(self) -> None:
        raise NotImplementedError(
            "The render of this component has not been implemented yet"
        )

    def handle_event(self, event: pygame.event.Event) -> None:
        pass

    def get_gui_element(self) -> pygame_gui.core.UIElement:
        if self.gui_element is not None:
            return self.gui_element
        else:
            raise NotImplementedError(
                "The ui_element of this component has not been implemented yet"
            )

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
