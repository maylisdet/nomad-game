import pygame
import pygame_gui

from pygame_gui.core.ui_element import ObjectID
from client.ihm.common.component import Component
from client.ihm.main.components.form_text_input import FormTextInput
from config import config


class ColorList(Component):
    def __init__(self, pygame_manager: pygame_gui.UIManager) -> None:
        super().__init__(pygame_manager)
        self.pygame_manager = pygame_manager

        self.set_width(280)
        self.set_height(70)

        self.set_pos_x(470)
        self.set_pos_y(420)

    def render(self) -> None:
        self.gui_element = pygame_gui.elements.ui_selection_list.UISelectionList(
            relative_rect=pygame.Rect(
                (self.pos_x, self.pos_y), (self.width, self.height)
            ),
            item_list=["Rouge", "Blanc"],
            manager=self.pygame_manager,
            starting_height=8,
            object_id=ObjectID(class_id="@color_list"),
        )

    def get_value(self) -> str:
        color = self.gui_element.get_single_selection()
        return color
