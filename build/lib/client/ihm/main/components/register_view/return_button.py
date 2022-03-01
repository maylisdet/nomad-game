import pygame
import pygame_gui

from pygame_gui.core.ui_element import ObjectID
from client.ihm.common.component import Component
from config import config


class ReturnButton(Component):
    def __init__(
        self,
        pygame_manager: pygame_gui.UIManager,
    ) -> None:
        super().__init__(pygame_manager)
        self.pygame_manager = pygame_manager

        self.set_width(200)
        self.set_height(60)

        self.set_pos_x(10)
        self.set_pos_y(665)

        self.text = "Retour"

    def render(self) -> None:

        self.gui_element = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(
                (self.get_pos_x(), self.get_pos_y()),
                (self.get_width(), self.get_height()),
            ),
            manager=self.pygame_manager,
            starting_layer_height=1,
        )

        self.button = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(0, 0, self.get_width(), self.get_height()),
            text=self.text,
            manager=self.manager,
            container=self.gui_element,
            starting_height=1,
            object_id=ObjectID(class_id="@return_button"),
        )

        image = pygame_gui.elements.UIImage(
            relative_rect=pygame.Rect((35, 12), (25, 25)),
            image_surface=pygame.image.load("./ressources/images/return.png"),
            manager=self.pygame_manager,
            container=self.gui_element,
        )

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.button:
                    print("Before Calls")
                    self.controller.handle_go_to_connection_view()
