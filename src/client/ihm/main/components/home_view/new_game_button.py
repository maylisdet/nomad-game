import pygame
import pygame_gui

from pygame_gui.core.ui_element import ObjectID

from client.ihm.common.component import Component


class NewGameButton(Component):
    def __init__(
        self, pygame_manager: pygame_gui.UIManager, container: Component
    ) -> None:
        super().__init__(pygame_manager)
        self.pygame_manager = pygame_manager
        self.container = container
        self.text = "Lancer une partie"
        self.set_pos_x(580)
        self.set_pos_y(450)
        self.set_width(250)
        self.set_height(75)

    def render(self) -> None:
        self.gui_element = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (self.pos_x, self.pos_y), (self.width, self.height)
            ),
            text=self.text,
            container=self.container.get_gui_element(),
            manager=self.pygame_manager,
            starting_height=1,
            object_id=ObjectID(class_id="@big_red_button"),
        )

    def modify_text(self, text: str) -> None:
        self.text = text
        self.render()

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.gui_element:
                    self.controller.show_create_game_window()
