import pygame
import pygame_gui

from client.ihm.common.component import Component


class ExampleComponent(Component):
    def __init__(self, pygame_manager: pygame_gui.UIManager) -> None:
        super().__init__(pygame_manager)
        self.pygame_manager = pygame_manager
        self.text = "this text gets updated after 3 sec"

    def render(self) -> None:
        self.gui_element = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect((0, 0), (300, 50)),
            text=self.text,
            manager=self.manager,
        )

    def modify_text(self, text: str) -> None:
        self.text = text
        self.render()
