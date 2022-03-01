import pygame_gui
from client.ihm.common.component import Component
from typing import Any

class NewGameButton(Component):
    pygame_manager: Any
    container: Any
    text: str
    def __init__(self, pygame_manager: pygame_gui.UIManager, container: Component) -> None: ...
    gui_element: Any
    def render(self) -> None: ...
    def modify_text(self, text: str) -> None: ...
