import pygame_gui
from client.ihm.common.component import Component
from typing import Any

class SectionTitle(Component):
    pygame_manager: Any
    text: Any
    container: Any
    def __init__(self, pygame_manager: pygame_gui.UIManager, container: Component, text: str, pos_x: int, pos_y: int) -> None: ...
    gui_element: Any
    def render(self) -> None: ...
    def modify_text(self, text: str) -> None: ...
