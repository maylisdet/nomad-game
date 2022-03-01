import typing

import pygame_gui

from client.ihm.common.ui_renderer import UIRenderer
from client.ihm.common.view import View
from client.ihm.main.components.register_view.register_panel import RegisterPanel
from client.ihm.main.components.register_view.return_button import ReturnButton
from client.ihm.main.components.register_view.validate_button_register import (
    ValidateButtonRegister,
)
from client.ihm.main.components.form_text_input import FormTextInput
from client.ihm.main.components.register_view.photo import Photo
from client.ihm.main.components.register_view.modify_photo_button import (
    ModifyPhotoButton,
)
from client.ihm.main.components.register_view.date_input import DateInput


# from client.ihm.main.ihm_main_controller import IHMMainController


class RegisterView(View):
    def __init__(
        self,
        pygame_manager: pygame_gui.UIManager,
        ui: UIRenderer,
        controller: typing.Any,
    ):
        super().__init__(pygame_manager, ui, controller)

        self.register_panel = RegisterPanel(pygame_manager)
        self.return_button = ReturnButton(pygame_manager)
        self.photo = Photo(pygame_manager, self.register_panel.gui_element)
        self.modify_photo = ModifyPhotoButton(
            pygame_manager, self.register_panel.gui_element
        )

        self.last_name_input = FormTextInput(
            pygame_manager,
            75,
            60,
            self.register_panel,
            "Nom",
            True,
            ".",
        )

        self.first_name_input = FormTextInput(
            pygame_manager,
            75,
            140,
            self.register_panel,
            "Prenom",
            True,
            ".",
        )

        # Date

        self.date_input = DateInput(
            pygame_manager,
            75,
            225,
            self.register_panel,
            "Date",
            True,
            ".",
        )

        self.pseudo_input = FormTextInput(
            pygame_manager,
            75,
            300,
            self.register_panel,
            "Pseudo",
            True,
            ".",
        )

        self.password_input = FormTextInput(
            pygame_manager,
            75,
            385,
            self.register_panel,
            "Mot de Passe",
            True,
            "[A-Za-z0-9@#$%^&+=]{8,}",
        )

        self.confirm_password_input = FormTextInput(
            pygame_manager,
            500,
            385,
            self.register_panel,
            "Confirmez mot de Passe",
            True,
            "[A-Za-z0-9@#$%^&+=]{8,}",
        )

        self.validate_button = ValidateButtonRegister(
            pygame_manager,
            self.register_panel.gui_element,
            self.first_name_input,
            self.last_name_input,
            self.date_input,
            self.pseudo_input,
            self.password_input,
            self.confirm_password_input,
        )

        self.add(self.register_panel)
        self.add(self.return_button)
        self.add(self.photo)
        self.add(self.modify_photo)
        self.add(self.validate_button)
        self.add(self.last_name_input)
        self.add(self.first_name_input)
        self.add(self.date_input)
        self.add(self.pseudo_input)
        self.add(self.password_input)
        self.add(self.confirm_password_input)
