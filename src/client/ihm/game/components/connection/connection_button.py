import pygame
import pygame_gui

from client.ihm.common.component import Component


class ConnectionButton(Component):
    def __init__(
        self, pygame_manager: pygame_gui.UIManager, container: Component
    ) -> None:
        super().__init__(pygame_manager)
        self.container = container

        self.set_width(self.container.get_width() // 2)
        self.set_height(self.container.get_height() // 5)
        self.set_pos_x(int(self.container.get_width() * 0.25))
        self.set_pos_y(int(self.container.get_height() * 0.25))

        self.render()

    def render(self) -> None:
        self.gui_element = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (self.pos_x, self.pos_y), (self.width, self.height)
            ),
            text="Se connecter",
            container=self.container.get_gui_element(),
            manager=self.manager,
        )
