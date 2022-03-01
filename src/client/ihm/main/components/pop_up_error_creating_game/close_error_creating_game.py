import pygame
import pygame_gui
from common import PlayerType

from pygame_gui.core.ui_element import ObjectID
from client.ihm.common.component import Component
from client.ihm.main.components.form_text_input import FormTextInput
from client.ihm.main.components.pop_up_create_game.color_list import ColorList
from config import config


class CloseErrorCreatingGame(Component):
    def __init__(
        self,
        pygame_manager: pygame_gui.UIManager,
    ) -> None:
        super().__init__(pygame_manager)
        self.pygame_manager = pygame_manager

        self.set_width(150)
        self.set_height(50)

        self.set_pos_x(525)
        self.set_pos_y(375)

        self.text = "Close"

    def render(self) -> None:
        self.gui_element = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (self.pos_x, self.pos_y), (self.width, self.height)
            ),
            text=self.text,
            manager=self.pygame_manager,
            starting_height=20,
            object_id=ObjectID(class_id="@big_red_button"),
        )

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.gui_element:
                    self.controller.handle_close_error_creating_game()
