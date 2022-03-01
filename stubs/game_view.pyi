import pygame_gui
import typing
from client.ihm.common.ui_renderer import UIRenderer as UIRenderer
from client.ihm.common.view import View
from typing import Any

class GameView(View):
    pass_turn: Any
    spectator_number: Any
    tile_number: Any
    first_player: Any
    second_player: Any
    chat_component: Any
    grid_panel: Any
    def __init__(self, pygame_manager: pygame_gui.UIManager, ui: UIRenderer, controller: typing.Any) -> None: ...
