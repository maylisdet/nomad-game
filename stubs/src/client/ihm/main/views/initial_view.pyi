import pygame_gui
import typing
from client.ihm.common.ui_renderer import UIRenderer as UIRenderer
from client.ihm.common.view import View
from typing import Any

class InitialView(View):
    test_component: Any
    def __init__(self, pygame_manager: pygame_gui.UIManager, ui: UIRenderer, controller: typing.Any) -> None: ...
