import pygame
import pygame_gui
from typing import *

from pygame_gui.core.ui_element import ObjectID

from client.ihm.common.component import Component


class TurnPlayer(Component):
    def __init__(self, pygame_manager: pygame_gui.UIManager) -> None:
        super().__init__(pygame_manager)
        self.pygame_manager = pygame_manager
        self.class_id = "@turn_player_panel"
        self.width = 40
        self.height = 100
        self.pos_x = 665
        self.pos_y = 80

    def render(self) -> None:
        self.gui_element = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(
                (self.pos_x, self.pos_y), (self.width, self.height)
            ),
            manager=self.pygame_manager,
            starting_layer_height=1,
            object_id=ObjectID(class_id=self.class_id),
        )

        first_player_pp = pygame_gui.elements.UIImage(
            relative_rect=pygame.Rect((0, 40), (40, 40)),
            manager=self.pygame_manager,
            container=self.gui_element,
            image_surface=pygame.image.load("./ressources/images/right-chevron.png"),
        )

    def modify_player_class_id(self, class_id: str) -> None:
        self.class_id = class_id

    def to_red_player(self):
        self.pos_x = 665
        self.pos_y = 80

    def to_white_player(self):
        self.pos_x = 665
        self.pos_y = 220
