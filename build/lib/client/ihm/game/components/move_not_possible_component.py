import pygame
import pygame_gui

from pygame_gui.core.ui_element import ObjectID
from client.ihm.common.component import Component
from pygame_gui.elements.ui_window import UIWindow
from config import config


class MoveNotPossibleComponent(Component):
    def __init__(self, pygame_manager: pygame_gui.UIManager) -> None:
        super().__init__(pygame_manager)
        self.pygame_manager = pygame_manager

        # Monitor Size

        window_width = config.get("monitor")["width"]
        window_height = config.get("monitor")["height"]

        self.set_width(500)
        self.set_height(200)

        self.set_pos_x((window_width * 0.25 + 50))
        self.set_pos_y((window_height * 0.25 + 75))

        self.title = "En attente d'un adversaire"

    def render(self) -> None:

        self.gui_element = UIWindow(
            pygame.Rect(
                (self.get_pos_x(), self.get_pos_y()),
                (self.get_width(), self.get_height()),
            ),
            manager=self.manager,
            window_display_title=self.title,
        )
