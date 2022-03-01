import typing

import pygame_gui

from client.ihm.common.ui_renderer import UIRenderer
from client.ihm.common.view import View
from client.ihm.main.components.example_component import ExampleComponent

# from client.ihm.main.ihm_main_controller import IHMMainController


class InitialView(View):
    def __init__(
        self,
        pygame_manager: pygame_gui.UIManager,
        ui: UIRenderer,
        controller: typing.Any,
    ):
        super().__init__(pygame_manager, ui, controller)

        self.test_component = ExampleComponent(pygame_manager)

        self.add(self.test_component)
