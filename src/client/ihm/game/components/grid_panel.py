import math
from typing import *
import pygame
import pygame_gui

from pygame_gui.core.ui_element import ObjectID

from client.ihm.common.component import Component
from client.ihm.game.components.grid_button import GridButton


class GridPanel(Component):
    def __init__(self, pygame_manager: pygame_gui.UIManager) -> None:
        super().__init__(pygame_manager)
        self.pygame_manager = pygame_manager
        self.width = 670
        self.height = 670
        self.pos_x = 30
        self.pos_y = 30
        # Todo : Replace this fake board
        self.board: Dict[str, Tuple[str, int]] = dict()
        self.dict_buttons: Dict[str, pygame_gui.elements.UIButton] = dict()

    def init_grid_button(self) -> None:

        button_size = math.floor(self.width / 14)
        for key in self.board:
            class_name, tile_number_str, i, j = self.get_grid_button_info(key)
            self.dict_buttons[key] = GridButton(
                self.pygame_manager,
                i * button_size,
                j * button_size,
                button_size,
                button_size,
                tile_number_str,
                class_name,
                key,
                self,
            )
            self.dict_buttons[key].set_controller(self.controller)

    def render(self) -> None:
        self.gui_element = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(
                (self.pos_x, self.pos_y), (self.width, self.height)
            ),
            manager=self.pygame_manager,
            starting_layer_height=1,
            object_id=ObjectID(class_id="@grid_panel"),
        )
        self.init_grid_button()

    def set_board(self, board: Dict[str, Tuple[str, int]]):
        self.board = board

    def get_dico_alpha_to_x(self):
        return {
            "A": 0,
            "B": 1,
            "C": 2,
            "D": 3,
            "E": 4,
            "F": 5,
            "G": 6,
            "H": 7,
            "I": 8,
            "J": 9,
            "K": 10,
            "L": 11,
            "M": 12,
        }

    def get_grid_button_info(self, position_str: str):
        class_name_dico = {
            "Red": "@grid_button_panel_red_piece",
            "White": "@grid_button_panel_white_piece",
            "None": "@grid_button_panel",
            "Tower": "@grid_button_panel_tower",
        }
        class_name = class_name_dico[self.board[position_str][0]]

        tile_number_str = (
            str(self.board[position_str][1])
            if self.board[position_str][1] > 0
            and self.board[position_str][0] != "Tower"
            else ""
        )
        i = int(position_str[1:])
        j = self.get_dico_alpha_to_x()[position_str[0:1]]
        return class_name, tile_number_str, i, j

    def handle_event(self, event: pygame.event.Event) -> None:
        for key in self.dict_buttons:
            self.dict_buttons[key].handle_event(event)
