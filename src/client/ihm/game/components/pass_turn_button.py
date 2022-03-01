import random

import pygame
import pygame_gui

from pygame_gui.core.ui_element import ObjectID

from client.ihm.common.component import Component
from common.data_structures.move import Move


class PassTurnButton(Component):
    def __init__(self, pygame_manager: pygame_gui.UIManager) -> None:
        super().__init__(pygame_manager)
        self.pygame_manager = pygame_manager
        self.text = "Passer son tour"
        self.width = 200
        self.height = 60
        self.pos_x = 235
        self.pos_y = 680

    def render(self) -> None:
        self.gui_element = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (self.pos_x, self.pos_y), (self.width, self.height)
            ),
            text=self.text,
            manager=self.pygame_manager,
            starting_height=1,
            object_id=ObjectID(class_id="@basic_champagne_button_with_border"),
        )

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
            if event.ui_element == self.gui_element:
                print("Pass turn pressed")
                a_move = Move(
                    self.controller.local_game.get_uuid(),
                    self.controller.local_game.get_current_player(),
                    "",
                    "",
                )
                self.controller.get_my_interface_to_comm().place_tile(a_move)
