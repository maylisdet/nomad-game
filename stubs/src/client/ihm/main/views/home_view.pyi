import pygame_gui
import typing
from client.ihm.common.ui_renderer import UIRenderer as UIRenderer
from client.ihm.common.view import View
from typing import Any

class HomeView(View):
    main_app_title: Any
    home_panel: Any
    connected_user_section_title: Any
    players_list: Any
    live_games_section_title: Any
    games_list: Any
    new_game_button: Any
    server_infos: Any
    profile_button: Any
    disconnect_button: Any
    def __init__(self, pygame_manager: pygame_gui.UIManager, ui: UIRenderer, controller: typing.Any) -> None: ...
