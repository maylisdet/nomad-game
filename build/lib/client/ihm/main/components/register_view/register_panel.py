import pygame
import pygame_gui

from pygame_gui.core.ui_element import ObjectID

from client.ihm.common.component import Component


class RegisterPanel(Component):
    def __init__(self, pygame_manager: pygame_gui.UIManager) -> None:
        super().__init__(pygame_manager)
        self.pygame_manager = pygame_manager

        # here it will be the center and not the topleft corner
        self.set_pos_x(1200 // 2)
        self.set_pos_y(750 // 2)

        self.set_width(round(1200 * 0.7))
        self.set_height(round(750 * 0.75))

    def render(self) -> None:
        relative_rect = pygame.Rect((0, 0), (self.width, self.height))
        relative_rect.center = (self.pos_x, self.pos_y)
        self.gui_element = pygame_gui.elements.UIPanel(
            relative_rect=relative_rect,
            manager=self.pygame_manager,
            starting_layer_height=0,
        )

        self.title = pygame_gui.elements.UITextBox(
            html_text="NOMAD",
            relative_rect=pygame.Rect((40, 5), (150, 20)),
            manager=self.manager,
            wrap_to_height=True,
            object_id=ObjectID(class_id="@accueil_app_title_2"),
        )

        self.register_title = pygame_gui.elements.UITextBox(
            html_text="Inscription",
            relative_rect=pygame.Rect((30, 5), (150, 20)),
            manager=self.manager,
            container=self.gui_element,
            wrap_to_height=True,
            object_id=ObjectID(class_id="@accueil_app_title_3"),
        )
