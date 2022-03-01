import typing

import pygame_gui

from client.ihm.common.ui_renderer import UIRenderer
from client.ihm.common.view import View
from client.ihm.main.components.form_text_input import FormTextInput
from client.ihm.main.components.main_app_title import MainAppTitle
from client.ihm.main.components.section_title import SectionTitle
from client.ihm.main.components.server_infos_view.back_button import BackButton
from client.ihm.main.components.server_infos_view.server_infos_panel import (
    ServerInfosPanel,
)
from client.ihm.main.components.server_infos_view.validate_button import ValidateButton

from client.ihm.main.components.server_infos_view.serv_connexion_error_message import (
    ServConnexionError,
)

# from client.ihm.main.ihm_main_controller import IHMMainController


class ServerInfoView(View):
    def __init__(
        self,
        pygame_manager: pygame_gui.UIManager,
        ui: UIRenderer,
        controller: typing.Any,
    ):
        super().__init__(pygame_manager, ui, controller)

        self.main_app_title = MainAppTitle(pygame_manager)
        self.server_infos_panel = ServerInfosPanel(pygame_manager)
        self.section_title = SectionTitle(
            pygame_manager, self.server_infos_panel, "Informations serveur", 50, 20
        )
        self.back_button = BackButton(pygame_manager)
        self.server_address = FormTextInput(
            pygame_manager,
            170,
            100,
            self.server_infos_panel,
            "Adresse IP",
            True,
            "^(\d{1,3}\.){3}\d{1,3}$",
        )
        self.port_number = FormTextInput(
            pygame_manager, 170, 190, self.server_infos_panel, "Port", True, "^\d{1,4}$"
        )
        self.validate_button = ValidateButton(
            pygame_manager,
            self.server_infos_panel,
            self.server_address,
            self.port_number,
        )
        self.serv_connexion_error = ServConnexionError(pygame_manager)

        self.add(self.main_app_title)
        self.add(self.server_infos_panel)
        self.add(self.section_title)
        self.add(self.back_button)
        self.add(self.server_address)
        self.add(self.port_number)
        self.add(self.validate_button)
        self.add(self.serv_connexion_error)

    def set_is_last_view_connexion_form(
        self, is_last_view_connexion_form: bool
    ) -> None:
        self.back_button.set_is_last_view_connexion_form(is_last_view_connexion_form)
