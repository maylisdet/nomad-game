import pygame_gui
from client.ihm.common.component import Component
from pygame_gui.core.ui_element import ObjectID as ObjectID
from typing import Any

class HomePanel(Component):
    pygame_manager: Any
    def __init__(self, pygame_manager: pygame_gui.UIManager) -> None: ...
    gui_element: Any
    def render(self) -> None: ...
    text: Any
    def modify_text(self, text: str) -> None: ...
