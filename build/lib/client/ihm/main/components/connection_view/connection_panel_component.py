import pygame
import pygame_gui

from pygame_gui.core.ui_element import ObjectID
from client.ihm.common.component import Component
from config import config


class ConnectionPanelComponent(Component):
    def __init__(self, pygame_manager: pygame_gui.UIManager) -> None:
        super().__init__(pygame_manager)
        self.pygame_manager = pygame_manager

        # Monitor Size

        window_width = config.get("monitor")["width"]
        window_height = config.get("monitor")["height"]

        self.set_width(600)
        self.set_height(450)

        self.set_pos_x(window_width * 0.25)
        self.set_pos_y((window_height * 0.25) - 50)

    def render(self) -> None:

        self.gui_element = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(
                self.get_pos_x(), self.get_pos_y(), self.get_width(), self.get_height()
            ),
            manager=self.manager,
            starting_layer_height=1,
        )

        self.title = pygame_gui.elements.UITextBox(
            html_text="NOMAD",
            relative_rect=pygame.Rect((self.get_width() // 3 + 35, 5), (150, 20)),
            manager=self.manager,
            container=self.gui_element,
            wrap_to_height=True,
            object_id=ObjectID(class_id="@accueil_app_title"),
        )
