import pygame_gui
from client.ihm.common.component import Component
from typing import Any

class FirstPlayerContainer(Component):
    pygame_manager: Any
    class_id: str
    def __init__(self, pygame_manager: pygame_gui.UIManager) -> None: ...
    gui_element: Any
    def render(self) -> None: ...
    def modify_player_class_id(self, class_id: str) -> None: ...
