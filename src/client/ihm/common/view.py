from typing import List, Any

import pygame_gui

from client.ihm.common.window import Window
from client.ihm.common.pop_up import PopUp


class View(Window):
    def __init__(self, pygame_manager: pygame_gui.UIManager, ui, controller: Any):
        super(View, self).__init__(pygame_manager, ui, controller)
        self.pop_ups: List[PopUp] = []

    def render(self):
        super(View, self).render()

        for pop_up in self.pop_ups:
            pop_up.render()

    def handle_event(self, event):
        super(View, self).handle_event(event)

        for pop_up in self.pop_ups:
            pop_up.handle_event(event)

    def add_pop_up(self, pop_up: PopUp) -> None:
        self.pop_ups.append(pop_up)
