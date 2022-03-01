import pygame
import pygame_gui

from pygame_gui.core.ui_element import ObjectID
from client.ihm.common.component import Component
from config import config


class Photo(Component):
    def __init__(
        self,
        pygame_manager: pygame_gui.UIManager,
        container: pygame_gui.elements.UIPanel,
    ) -> None:
        super().__init__(pygame_manager)
        self.pygame_manager = pygame_manager

        self.container = container

        self.set_width(150)
        self.set_height(150)

        self.set_pos_x(725)
        self.set_pos_y(170)

    def render(self) -> None:

        self.gui_element = pygame_gui.elements.UIImage(
            relative_rect=pygame.Rect(
                (self.pos_x, self.pos_y), (self.width, self.height)
            ),
            image_surface=pygame.image.load("./ressources/images/user.png"),
            manager=self.pygame_manager,
            container=self.container,
        )

    def handle_event(self, event: pygame.event.Event) -> None:
        pass
