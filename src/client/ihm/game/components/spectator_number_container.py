import pygame
import pygame_gui

from pygame_gui.core.ui_element import ObjectID

from client.ihm.common.component import Component


class SpectatorNumberContainer(Component):
    def __init__(self, pygame_manager: pygame_gui.UIManager) -> None:
        super().__init__(pygame_manager)
        self.pygame_manager = pygame_manager
        self.text = "12"
        self.width = 200
        self.height = 70
        self.pos_x = 850
        self.pos_y = 5

    def render(self) -> None:
        self.gui_element = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(
                (self.pos_x, self.pos_y), (self.width, self.height)
            ),
            manager=self.pygame_manager,
            starting_layer_height=1,
            object_id=ObjectID(class_id="@options_panel"),
        )

        panel_title = pygame_gui.elements.UITextBox(
            relative_rect=pygame.Rect((20, 18), (50, 20)),
            html_text=self.text,
            wrap_to_height=True,
            manager=self.manager,
            container=self.gui_element,
            object_id=ObjectID(class_id="@options_text"),
        )

        image = pygame_gui.elements.UIImage(
            relative_rect=pygame.Rect((60, 10), (60, 50)),
            image_surface=pygame.image.load("./ressources/images/eye.png"),
            manager=self.pygame_manager,
            container=self.gui_element,
        )

    def modify_text(self, text: str) -> None:
        self.text = text
        self.render()
