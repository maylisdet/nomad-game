import pygame
import pygame_gui

from pygame_gui.core.ui_element import ObjectID

from client.ihm.common.component import Component


class ProfilButton(Component):
    def __init__(self, pygame_manager: pygame_gui.UIManager) -> None:
        super().__init__(pygame_manager)
        self.pygame_manager = pygame_manager
        self.text = "Mon profil"
        self.set_pos_x(800)
        self.set_pos_y(35)
        self.set_width(200)
        self.set_height(50)

    def render(self) -> None:
        self.gui_element = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(
                (self.pos_x, self.pos_y), (self.width, self.height)
            ),
            manager=self.pygame_manager,
            starting_layer_height=1,
            object_id=ObjectID(class_id="@options_panel"),
        )

        image = pygame_gui.elements.UIImage(
            relative_rect=pygame.Rect((0, 7), (20, 20)),
            image_surface=pygame.image.load("./ressources/images/user.png"),
            manager=self.pygame_manager,
            container=self.gui_element,
        )

        panel_title = pygame_gui.elements.UITextBox(
            relative_rect=pygame.Rect((25, 0), (100, 20)),
            html_text=self.text,
            wrap_to_height=True,
            manager=self.manager,
            container=self.gui_element,
            object_id=ObjectID(class_id="@options_text"),
        )

    def modify_text(self, text: str) -> None:
        self.text = text
        self.render()
