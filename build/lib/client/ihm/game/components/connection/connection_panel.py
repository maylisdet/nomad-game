import pygame
import pygame_gui

from config import config
from client.ihm.common.component import Component


class ConnectionPanel(Component):
    def __init__(self, pygame_manager: pygame_gui.UIManager) -> None:
        super().__init__(pygame_manager)

        self.set_width(config.get("monitor")["width"] // 2)
        self.set_height(config.get("monitor")["height"] // 2)
        self.set_pos_x(config.get("monitor")["height"] * 0.25)
        self.set_pos_y(config.get("monitor")["width"] * 0.25)

        self.render()

    def render(self) -> None:
        self.gui_element = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(
                (self.pos_x, self.pos_y), (self.width, self.height)
            ),
            manager=self.manager,
            starting_layer_height=1,
        )
