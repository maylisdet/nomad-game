import pygame_gui
from client.ihm.common.component import Component
from typing import Any

class ConnectionButtonNext(Component):
    container: Any
    def __init__(self, pygame_manager: pygame_gui.UIManager, container: Component) -> None: ...
    gui_element: Any
    def render(self) -> None: ...
