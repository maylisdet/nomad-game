import pygame_gui
import typing
from client.ihm.common.component import Component as Component
from typing import Any

class View:
    pygame_manager: Any
    components: Any
    ui: Any
    controller: Any
    def __init__(self, pygame_manager: pygame_gui.UIManager, ui, controller: typing.Any) -> None: ...
    def render(self) -> None: ...
    def handle_event(self, event) -> None: ...
    def add(self, component: Component): ...
