from typing import Container, List
from client.ihm.main.components.home_view.player_item import PlayerItem
import pygame
import pygame_gui

from pygame_gui.core.ui_element import ObjectID

from client.ihm.common.component import Component


class PlayersList(Component):
    def __init__(
        self,
        pygame_manager: pygame_gui.UIManager,
        container: Component,
        players: List[str],
    ) -> None:
        super().__init__(pygame_manager)
        self.pygame_manager = pygame_manager
        self.container = container
        self.set_pos_x(20)
        self.set_pos_y(75)
        self.set_width(350)
        self.set_height(450)
        self.players = players
        self.row_height = 50
        self.rows_list: List[PlayerItem] = []

    def render(self) -> None:
        self.gui_element = pygame_gui.elements.UIScrollingContainer(
            relative_rect=pygame.Rect(
                (self.pos_x, self.pos_y), (self.width, self.height)
            ),
            manager=self.pygame_manager,
            container=self.container.get_gui_element(),
        )
        self.gui_element.set_scrollable_area_dimensions(
            (self.width - 20, len(self.players) * self.row_height)
        )

        for i in range(len(self.players)):
            new_row = PlayerItem(
                self.pygame_manager,
                self,
                self.players[i],
                0,
                self.row_height * i,
                self.row_height,
                self.width - 20,
                i,
            )
            new_row.render()
            self.rows_list.append(new_row)

    def modify_text(self, text: str) -> None:
        self.text = text
        self.render()
