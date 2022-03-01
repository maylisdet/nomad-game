import typing

import pygame_gui

from client.ihm.common.ui_renderer import UIRenderer
from client.ihm.common.view import View
from client.ihm.main.components.connexion_form_view.connexion_back_button import (
    ConnexionBackButton,
)
from client.ihm.main.components.connexion_form_view.connexion_form_error import (
    ConnexionFormError,
)
from client.ihm.main.components.connexion_form_view.connexion_form_panel import (
    ConnexionFormPanel,
)
from client.ihm.main.components.connexion_form_view.password_input import PasswordInput
from client.ihm.main.components.connexion_form_view.validate_connexion_button import (
    ValidateConnexionButton,
)
from client.ihm.main.components.main_app_title import MainAppTitle
from client.ihm.main.components.section_title import SectionTitle
from client.ihm.main.components.form_text_input import FormTextInput

# from client.ihm.main.ihm_main_controller import IHMMainController


class ConnexionFormView(View):
    def __init__(
        self,
        pygame_manager: pygame_gui.UIManager,
        ui: UIRenderer,
        controller: typing.Any,
    ):
        super().__init__(pygame_manager, ui, controller)

        self.main_app_title = MainAppTitle(pygame_manager)
        self.connexion_form_panel = ConnexionFormPanel(pygame_manager)
        self.section_title = SectionTitle(
            pygame_manager, self.connexion_form_panel, "Connexion", 50, 20
        )
        self.back_button = ConnexionBackButton(pygame_manager)

        self.nickname = FormTextInput(
            pygame_manager,
            170,
            100,
            self.connexion_form_panel,
            "Pseudo",
            True,
            "^.+$",  # this regex avoid empty input
        )
        self.password = PasswordInput(
            pygame_manager,
            170,
            190,
            self.connexion_form_panel,
            "Mot de passe",
            True,
            "^.+$",
        )

        self.validation_button = ValidateConnexionButton(
            pygame_manager, self.connexion_form_panel, self.nickname, self.password
        )

        self.connexion_form_error = ConnexionFormError(pygame_manager)

        self.add(self.main_app_title)
        self.add(self.connexion_form_panel)
        self.add(self.section_title)
        self.add(self.back_button)
        self.add(self.nickname)
        self.add(self.password)
        self.add(self.validation_button)
        self.add(self.connexion_form_error)
