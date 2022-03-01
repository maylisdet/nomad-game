import pygame
import pygame_gui
from common import PlayerType

from pygame_gui.core.ui_element import ObjectID
from client.ihm.common.component import Component
from client.ihm.main.components.form_text_input import FormTextInput
from client.ihm.main.components.pop_up_create_game.color_list import ColorList
from config import config


class ValidateGame(Component):
    def __init__(
        self,
        pygame_manager: pygame_gui.UIManager,
        name_game: FormTextInput,
        number_towers: FormTextInput,
        color_list: ColorList,
    ) -> None:
        super().__init__(pygame_manager)
        self.pygame_manager = pygame_manager

        self.set_width(150)
        self.set_height(50)

        self.set_pos_x(650)
        self.set_pos_y(550)

        self.text = "Valider"

        self.name_game = name_game
        self.number_towers = number_towers
        self.color_list = color_list

    def render(self) -> None:
        self.gui_element = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(
                (self.pos_x, self.pos_y), (self.width, self.height)
            ),
            text=self.text,
            manager=self.pygame_manager,
            starting_height=9,
            object_id=ObjectID(class_id="@big_red_button"),
        )

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == self.gui_element:
                    if self.color_list.get_value() != None:
                        if (
                            self.name_game.validate_input()
                            and self.number_towers.validate_input()
                        ):
                            name_game = self.name_game.get_input_text()
                            number_towers = self.number_towers.get_input_text()
                            color = self.color_list.get_value()
                            choice = (
                                PlayerType.RED if color == "Rouge" else PlayerType.WHITE
                            )
                            self.controller.create_game(
                                name_game, number_towers, choice
                            )
