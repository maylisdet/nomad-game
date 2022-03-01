import typing

import pygame_gui

from client.ihm.common.ui_renderer import UIRenderer
from client.ihm.common.view import View
from client.ihm.main.components.connection_view.connection_panel_component import (
    ConnectionPanelComponent,
)
from client.ihm.main.components.connection_view.connection_button_component import (
    ConnectionButtonComponent,
)
from client.ihm.main.components.connection_view.inscription_button_component import (
    InscriptionButtonComponent,
)
from client.ihm.main.components.connection_view.import_button_component import (
    ImportButtonComponent,
)

# from client.ihm.main.ihm_main_controller import IHMMainController


class ConnectionView(View):
    def __init__(
        self,
        pygame_manager: pygame_gui.UIManager,
        ui: UIRenderer,
        controller: typing.Any,
    ):
        super().__init__(pygame_manager, ui, controller)

        self.connection_panel = ConnectionPanelComponent(pygame_manager)
        self.connection_button = ConnectionButtonComponent(
            pygame_manager, self.connection_panel.gui_element
        )
        self.inscription_button = InscriptionButtonComponent(
            pygame_manager, self.connection_panel.gui_element
        )
        self.import_button = ImportButtonComponent(
            pygame_manager, self.connection_panel.gui_element
        )

        self.add(self.connection_panel)
        self.add(self.connection_button)
        self.add(self.inscription_button)
        self.add(self.import_button)
