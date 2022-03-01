import pygame
import pygame_gui

from pygame_gui.core.ui_element import ObjectID
from client.ihm.common.component import Component
from config import config


class CancelGame(Component):
    def __init__(self, pygame_manager: pygame_gui.UIManager) -> None:
        super().__init__(pygame_manager)
        self.pygame_manager = pygame_manager

        self.set_width(150)
        self.set_height(50)

        self.set_pos_x(400)
        self.set_pos_y(550)

        self.text = "Annuler"

    def render(self) -> None:
        self.gui_element = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (self.pos_x, self.pos_y), (self.width, self.height)
            ),
            text=self.text,
            manager=self.pygame_manager,
            starting_height=9,
            # object_id=ObjectID(class_id="@basic_champagne_button"),
            object_id=ObjectID(class_id="@basic_linen_button"),
        )

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.gui_element:
                    self.controller.hide_create_game_window()
