import pygame
import pygame_gui

from pygame_gui.core.ui_element import ObjectID

from client.ihm.common.component import Component


class TileNumberContainer(Component):
    def __init__(self, pygame_manager: pygame_gui.UIManager) -> None:
        super().__init__(pygame_manager)
        self.pygame_manager = pygame_manager
        self.text = "120"
        self.width = 200
        self.height = 60
        self.pos_x = 820
        self.pos_y = 675

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
            relative_rect=pygame.Rect((100, 5), (90, 100)),
            html_text=self.text,
            wrap_to_height=True,
            manager=self.manager,
            container=self.gui_element,
            object_id=ObjectID(class_id="@tile_number_text"),
        )

        image = pygame_gui.elements.UIImage(
            relative_rect=pygame.Rect((40, 10), (45, 45)),
            image_surface=pygame.image.load("./ressources/images/black_piece.png"),
            manager=self.pygame_manager,
            container=self.gui_element,
        )

    def modify_text(self, text: str) -> None:
        self.text = text
