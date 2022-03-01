import pygame
import pygame_gui

from pygame_gui.core.ui_element import ObjectID

from client.ihm.common.component import Component


class ServerInfos(Component):
    def __init__(self, pygame_manager: pygame_gui.UIManager, text: str) -> None:
        super().__init__(pygame_manager)
        self.pygame_manager = pygame_manager

        self.text = text

        self.set_width(600)
        self.set_height(0)
        self.set_pos_x(40)
        self.set_pos_y(700)

    def render(self) -> None:
        self.gui_element = pygame_gui.elements.UITextBox(
            html_text=self.text,
            relative_rect=pygame.Rect(
                (self.pos_x, self.pos_y), (self.width, self.height)
            ),
            manager=self.manager,
            wrap_to_height=True,
            object_id=ObjectID(class_id="@server_infos"),
        )

    def modify_text(self, text: str) -> None:
        self.text = text
        self.render()
