import typing
from typing import List

import pygame_gui

from client.ihm.common.component import Component


class Window:
    def __init__(
        self, pygame_manager: pygame_gui.UIManager, ui, controller: typing.Any
    ):
        self.pygame_manager = pygame_manager
        self.components: List[Component] = []
        self.ui = ui
        self.controller = controller

    def render(self):
        for component in self.components:
            component.render()

    def handle_event(self, event):
        for component in self.components:
            component.handle_event(event)

    def add(self, component: Component):
        self.components.append(component)
        component.set_controller(self.controller)
