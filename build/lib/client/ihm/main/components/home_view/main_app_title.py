import pygame
import pygame_gui

from pygame_gui.core.ui_element import ObjectID

from client.ihm.common.component import Component


class MainAppTitle(Component):
    def __init__(self, pygame_manager: pygame_gui.UIManager) -> None:
        super().__init__(pygame_manager)
        self.pygame_manager = pygame_manager
        self.text = "NOMAD"

    def render(self) -> None:
        self.gui_element = pygame_gui.elements.UITextBox(
            html_text=self.text,
            relative_rect=pygame.Rect((40, 3), (200, 20)),
            manager=self.manager,
            wrap_to_height=True,
            object_id=ObjectID(class_id="@main_app_title"),
        )

    def modify_text(self, text: str) -> None:
        self.text = text
        self.render()
