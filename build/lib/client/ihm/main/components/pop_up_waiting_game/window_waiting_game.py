import pygame
import pygame_gui

from pygame_gui.core.ui_element import ObjectID
from client.ihm.common.component import Component
from pygame_gui.elements.ui_window import UIWindow
from config import config


class WindowWaitingGame(Component):
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

        self.label = pygame_gui.elements.UITextBox(
            html_text="Partie XX 15 Tours",
            relative_rect=pygame.Rect((self.get_width() // 2 - 100, 5), (200, 20)),
            manager=self.manager,
            container=self.gui_element,
            wrap_to_height=True,
            object_id=ObjectID(class_id="@game_info"),
        )

        self.button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect((125, 50), (225, 75)),
            text="Abandonner",
            container=self.gui_element,
            manager=self.manager,
            object_id=ObjectID(class_id="@left_button"),
        )
