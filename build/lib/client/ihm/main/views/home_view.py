import typing
import pygame

import pygame_gui

from client.ihm.common.ui_renderer import UIRenderer
from client.ihm.common.view import View
from client.ihm.main.components.main_app_title import MainAppTitle
from client.ihm.main.components.home_view.home_panel import HomePanel
from client.ihm.main.components.section_title import SectionTitle
from client.ihm.main.components.home_view.players_list import PlayersList
from client.ihm.main.components.home_view.games_list import GamesList
from client.ihm.main.components.home_view.new_game_button import NewGameButton
from client.ihm.main.components.home_view.server_infos import ServerInfos
from client.ihm.main.components.home_view.profil_button import ProfilButton
from client.ihm.main.components.home_view.disconnect_button import DisconnectButton
from client.ihm.main.popups.waiting_game import WaitingGame

# from client.ihm.main.ihm_main_controller import IHMMainController


class HomeView(View):
    def __init__(
        self,
        pygame_manager: pygame_gui.UIManager,
        ui: UIRenderer,
        controller: typing.Any,
    ):
        super().__init__(pygame_manager, ui, controller)

        self.main_app_title = MainAppTitle(pygame_manager)
        self.home_panel = HomePanel(pygame_manager)
        self.connected_user_section_title = SectionTitle(
            pygame_manager, self.home_panel, "Utilisateurs connectés", 20, 10
        )
        self.players_list = PlayersList(
            pygame_manager,
            self.home_panel,
            [
                "Michel",
                "Jean",
                "Pierre",
                "Josette",
                "Maurice",
                "Lucien",
                "Géraldine",
                "Monique",
                "Raymond",
                "Jeanne",
                "Louis",
                "Irène",
                "Colette",
                "Ernest",
                "Achille",
            ],
        )
        self.live_games_section_title = SectionTitle(
            pygame_manager, self.home_panel, "Parties en cours", 425, 10
        )
        self.games_list = GamesList(
            pygame_manager,
            self.home_panel,
            [
                ("Michel", "Jean"),
                ("Pierre", "En attente ..."),
                ("Josette", "Maurice"),
                ("Lucien", "Géraldine"),
                ("Monique", "Raymond"),
                ("Louis", "En attente ..."),
                ("Irène", "Colette"),
                ("Ernest", "Achille"),
            ],
        )
        self.new_game_button = NewGameButton(pygame_manager, self.home_panel)
        self.server_infos = ServerInfos(
            pygame_manager, "Connecté au serveur 127.127.127.127 sur le port 5432"
        )
        self.profile_button = ProfilButton(pygame_manager)
        self.disconnect_button = DisconnectButton(pygame_manager)

        self.waiting_game_pop_up = WaitingGame(pygame_manager, ui, controller)

        self.add(self.main_app_title)
        self.add(self.home_panel)
        self.add(self.connected_user_section_title)
        self.add(self.players_list)
        self.add(self.live_games_section_title)
        self.add(self.games_list)
        self.add(self.new_game_button)
        self.add(self.server_infos)
        self.add(self.profile_button)
        self.add(self.disconnect_button)

        self.add_pop_up(self.waiting_game_pop_up)
