from typing import Container
import pygame
import pygame_gui

from pygame_gui.core.ui_element import ObjectID

from client.ihm.common.component import Component
from common import Player


class PlayerItem(Component):
    def __init__(
        self,
        pygame_manager: pygame_gui.UIManager,
        container: Component,
        player: Player,
        pos_x: int,
        pos_y: int,
        height: int,
        width: int,
        pos: int,
    ) -> None:
        super().__init__(pygame_manager)
        self.pygame_manager = pygame_manager
        self.container = container
        self.set_pos_x(pos_x)
        self.set_pos_y(pos_y)
        self.set_height(height)
        self.set_width(width)
        self.player = player
        self.pos = pos

    def render(self) -> None:
        self.gui_element = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(
                (self.pos_x, self.pos_y), (self.width, self.height)
            ),
            manager=self.pygame_manager,
            starting_layer_height=1,
            container=self.container.get_gui_element(),
            object_id=ObjectID(
                class_id="@list_panel_even" if self.pos % 2 == 0 else "@list_panel_odd"
            ),
        )

        image = pygame_gui.elements.UIImage(
            relative_rect=pygame.Rect((10, 5), (40, 40)),
            image_surface=pygame.image.load("./ressources/images/hen.png"),
            manager=self.pygame_manager,
            container=self.gui_element,
        )

        text_rect = pygame.Rect((0, 0), (150, 0))
        text_rect.center = (130, 10)

        text = pygame_gui.elements.UITextBox(
            relative_rect=text_rect,
            html_text=self.player.nickname,
            wrap_to_height=True,
            manager=self.manager,
            container=self.gui_element,
            object_id=ObjectID(
                class_id="@list_panel_even_text"
                if self.pos % 2 == 0
                else "@list_panel_odd_text"
            ),
        )

    def modify_text(self, text: str) -> None:
        self.text = text
        self.render()
