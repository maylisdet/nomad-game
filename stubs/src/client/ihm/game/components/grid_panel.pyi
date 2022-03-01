import pygame_gui
from client.ihm.common.component import Component
from typing import Any

class GridPanel(Component):
    pygame_manager: Any
    def __init__(self, pygame_manager: pygame_gui.UIManager) -> None: ...
    gui_element: Any
    def render(self) -> None: ...
