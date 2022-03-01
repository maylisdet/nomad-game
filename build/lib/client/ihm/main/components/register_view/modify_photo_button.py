import pygame
import pygame_gui

from pygame_gui.core.ui_element import ObjectID
from client.ihm.common.component import Component
from config import config


class ModifyPhotoButton(Component):
    def __init__(
        self,
        pygame_manager: pygame_gui.UIManager,
        container: pygame_gui.elements.UIPanel,
    ) -> None:
        super().__init__(pygame_manager)

        self.container = container
        self.pygame_manager = pygame_manager

        self.set_width(150)
        self.set_height(65)

        self.set_pos_x(725)
        self.set_pos_y(330)

        self.text = "Charger une photo ..."

    def render(self) -> None:

        self.gui_element = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                self.get_pos_x(), self.get_pos_y(), self.get_width(), self.get_height()
            ),
            text=self.text,
            manager=self.manager,
            container=self.container,
            starting_height=2,
            object_id=ObjectID(class_id="@upload_photo"),
        )

    def handle_event(self, event: pygame.event.Event) -> None:
        pass
