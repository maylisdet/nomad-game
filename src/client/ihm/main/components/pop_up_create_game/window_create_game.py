import pygame
import pygame_gui

from pygame_gui.core.ui_element import ObjectID
from client.ihm.common.component import Component
from pygame_gui.elements.ui_window import UIWindow
from config import config


class WindowCreateGame(Component):
    def __init__(self, pygame_manager: pygame_gui.UIManager) -> None:
        super().__init__(pygame_manager)
        self.pygame_manager = pygame_manager

        # Monitor Size

        window_width = config.get("monitor")["width"]
        window_height = config.get("monitor")["height"]

        self.set_width(500)
        self.set_height(480)

        self.set_pos_x((window_width * 0.25 + 50))
        self.set_pos_y((window_height * 0.25 - 35))

        self.title = "En attente d'un adversaire"

    def render(self) -> None:

        self.gui_element = UIWindow(
            pygame.Rect(
                (self.get_pos_x(), self.get_pos_y()),
                (self.get_width(), self.get_height()),
            ),
            manager=self.manager,
            window_display_title=self.title,
            object_id=ObjectID(class_id="@create_game_page"),
        )

        self.label = pygame_gui.elements.UITextBox(
            html_text="Création d'une partie",
            relative_rect=pygame.Rect((self.get_width() // 2 - 120, 5), (300, 20)),
            manager=self.manager,
            container=self.gui_element,
            wrap_to_height=True,
            object_id=ObjectID(class_id="@panel_title_text"),
        )
        self.label_color = pygame_gui.elements.UITextBox(
            html_text="Votre couleur",
            relative_rect=pygame.Rect((self.get_width() // 2 - 130, 230), (240, 20)),
            manager=self.manager,
            container=self.gui_element,
            wrap_to_height=True,
            object_id=ObjectID(class_id="@form_label"),
        )
