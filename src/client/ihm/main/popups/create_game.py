import pygame_gui
import typing

from client.ihm.common.pop_up import PopUp
from client.ihm.main.components.form_text_input import FormTextInput
from client.ihm.main.components.pop_up_create_game.window_create_game import (
    WindowCreateGame,
)
from client.ihm.main.components.pop_up_create_game.validate_game_button import (
    ValidateGame,
)
from client.ihm.main.components.pop_up_create_game.cancel_game_buton import (
    CancelGame,
)
from client.ihm.main.components.pop_up_create_game.color_list import (
    ColorList,
)

from pygame_gui.elements.ui_window import UIWindow


class CreateGame(PopUp):
    def __init__(
        self, pygame_manager: pygame_gui.UIManager, ui, controller: typing.Any
    ):
        super(PopUp, self).__init__(pygame_manager, ui, controller)

        self.window_create_game = WindowCreateGame(pygame_manager)
        self.cancel_game = CancelGame(pygame_manager)
        self.name_game = FormTextInput(
            pygame_manager,
            120,
            50,
            self.window_create_game,
            "NOM",
            True,
            ".*",
        )

        self.number_towers = FormTextInput(
            pygame_manager,
            120,
            130,
            self.window_create_game,
            "Nombre de tours à placer",
            True,
            "^[2-5]$",
        )

        self.color_list = ColorList(pygame_manager)
        self.validate_game = ValidateGame(
            pygame_manager, self.name_game, self.number_towers, self.color_list
        )

        self.add(self.window_create_game)
        self.add(self.validate_game)
        self.add(self.cancel_game)
        self.add(self.name_game)
        self.add(self.number_towers)
        self.add(self.color_list)
