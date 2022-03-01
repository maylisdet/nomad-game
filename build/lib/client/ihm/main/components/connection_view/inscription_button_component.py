import pygame
import pygame_gui

from pygame_gui.core.ui_element import ObjectID
from client.ihm.common.component import Component
from config import config


class InscriptionButtonComponent(Component):
    def __init__(
        self,
        pygame_manager: pygame_gui.UIManager,
        container: pygame_gui.elements.UIPanel,
    ) -> None:
        super().__init__(pygame_manager)
        self.pygame_manager = pygame_manager
        self.container = container

        self.set_width(300)
        self.set_height(75)

        self.set_pos_x(450)
        self.set_pos_y(375)

        self.text = "S'inscrire"

    def render(self) -> None:
        width = config.get("monitor")["width"]
        height = config.get("monitor")["height"]
        self.gui_element = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (self.get_pos_x(), self.get_pos_y()),
                (self.get_width(), self.get_height()),
            ),
            text=self.text,
            container=self.container,
            manager=self.manager,
            starting_height=2,
            object_id=ObjectID(class_id="@connection_button"),
        )

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.gui_element:
                    self.controller.handle_inscription()
