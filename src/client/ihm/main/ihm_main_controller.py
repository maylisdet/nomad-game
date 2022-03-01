import asyncio
import typing
import sys

from client.ihm.game.views.game_view import GameView
from client.ihm.common.py_game_controller import PyGameController
from client.ihm.main.comm_calls_ihm_main_impl import CommCallsIHMMain_Impl
from client.ihm.main.ihm_game_calls_ihm_main_impl import IHMGameCallsIHMMain_Impl
from client.ihm.main.views.connection_view import ConnectionView
from client.ihm.main.views.connexion_form_view import ConnexionFormView
from client.ihm.main.views.home_view import HomeView
from common import PlayerType
from common import I_IHMGameCallsIHMMain
from common import I_CommCallsIHMMain
from common import I_IHMMainCallsComm
from common import I_IHMMainCallsData
from common import I_IHMMainCallsIHMGame
from client.ihm.main.views.register_view import RegisterView
from client.ihm.main.views.server_infos_view import ServerInfoView
from common.utils import threaded

from common.data_structures.user import User

from config import config


class IHMMainController:
    def __init__(
        self,
        pygame_controller: PyGameController,
    ):
        self.pygame_controller = pygame_controller
        self.my_interface_from_ihm_game = IHMGameCallsIHMMain_Impl(self)
        self.my_interface_from_comm = CommCallsIHMMain_Impl(self)
        self.my_interface_to_comm: typing.Optional[I_IHMMainCallsComm] = None
        self.my_interface_to_ihm_game: typing.Optional[I_IHMMainCallsIHMGame] = None
        self.my_interface_to_data: typing.Optional[I_IHMMainCallsData] = None

        # initialize the first view
        self.connection_view = ConnectionView(
            pygame_controller.get_ui_manager(),
            pygame_controller.get_ui_renderer(),
            self,
        )
        self.server_infos_view = ServerInfoView(
            pygame_controller.get_ui_manager(),
            pygame_controller.get_ui_renderer(),
            self,
        )
        self.connexion_form_view = ConnexionFormView(
            pygame_controller.get_ui_manager(),
            pygame_controller.get_ui_renderer(),
            self,
        )
        self.home_view = HomeView(
            pygame_controller.get_ui_manager(),
            pygame_controller.get_ui_renderer(),
            self,
        )

        self.inscription_view = RegisterView(
            pygame_controller.get_ui_manager(),
            pygame_controller.get_ui_renderer(),
            self,
        )

        self.server_infos_view = ServerInfoView(
            pygame_controller.get_ui_manager(),
            pygame_controller.get_ui_renderer(),
            self,
        )

        pygame_controller.show_view(self.connection_view)

    def set_my_interface_to_comm(self, i: I_IHMMainCallsComm) -> None:
        self.my_interface_to_comm = i

    def set_my_interface_to_ihm_game(self, i: I_IHMMainCallsIHMGame) -> None:
        self.my_interface_to_ihm_game = i

    def set_my_interface_to_data(self, i: I_IHMMainCallsData) -> None:
        self.my_interface_to_data = i

    def get_my_interface_from_ihm_game(self) -> I_IHMGameCallsIHMMain:
        if self.my_interface_from_ihm_game is not None:
            return self.my_interface_from_ihm_game
        else:
            raise Exception(
                "get_my_interface_from_ihm_game was called but my_interface_from_ihm_game is None"
            )

    def get_my_interface_from_comm(self) -> I_CommCallsIHMMain:
        if self.my_interface_from_comm is not None:
            return self.my_interface_from_comm
        else:
            raise Exception(
                "get_my_interface_from_comm was called but my_interface_from_ihm_game is None"
            )

    def get_my_interface_to_comm(self) -> I_IHMMainCallsComm:
        if self.my_interface_to_comm is not None:
            return self.my_interface_to_comm
        else:
            raise Exception(
                "get_my_interface_to_comm was called but my_interface_to_comm is None"
            )

    def get_my_interface_to_data(self) -> I_IHMMainCallsData:
        if self.my_interface_to_data is not None:
            return self.my_interface_to_data
        else:
            raise Exception(
                "get_my_interface_to_data was called but my_interface_to_data is None"
            )

    def get_my_interface_to_ihm_game(self) -> I_IHMMainCallsIHMGame:
        if self.my_interface_to_ihm_game is not None:
            return self.my_interface_to_ihm_game
        else:
            raise Exception(
                "get_my_interface_to_ihm_game was called but my_interface_to_ihm_game is None"
            )

    @threaded
    def handle_server_connection(self, ip_address: str, port_number: str) -> None:
        try:
            asyncio.run(
                self.get_my_interface_to_comm().connect_to_server(
                    ip_address, int(port_number)
                )
            )
        except ConnectionRefusedError:
            self.server_infos_view.serv_connexion_error.show()

    @threaded
    def create_game(self, name: str, tiles: int, side: PlayerType) -> None:

        try:
            local_game = self.get_my_interface_to_data().create_game(name, tiles, side)

            self.get_my_interface_to_comm().create_game(local_game)
            self.home_view.create_game_pop_up.hide()
        except:
            self.home_view.create_game_pop_up.hide()
            self.home_view.error_creating_game_pop_up.show()

    @threaded
    def handle_join_game(self, game_uuid):
        profile = self.get_my_interface_to_data().get_profile()
        self.get_my_interface_to_comm().join_game(profile.uuid, game_uuid)

    def show_create_game_window(self) -> None:
        self.home_view.create_game_pop_up.show()

        # Hide input error labels

        self.home_view.create_game_pop_up.name_game.error_label.hide()
        self.home_view.create_game_pop_up.number_towers.error_label.hide()

    def hide_create_game_window(self) -> None:
        self.home_view.create_game_pop_up.hide()

    def handle_go_back_to_connection_form(self) -> None:
        pass
        # TODO : when the view is created, update here
        # self.pygame_controller.show_view(self.connection_form_view)

    def handle_go_back_to_inscription_form(self) -> None:
        pass
        # TODO : when the view is created, update here
        # self.pygame_controller.show_view(self.inscription_form_view)

    def handle_connexion(self, nickname: str, password: str) -> None:
        try:
            self.get_my_interface_to_data().connect_to_app(nickname, password)
            self.server_infos_view.set_is_last_view_connexion_form(True)
            self.pygame_controller.show_view(self.server_infos_view)
        except ValueError:
            self.connexion_form_view.connexion_form_error.show()

    def handle_go_to_inscription_view(self):
        self.pygame_controller.show_view(self.inscription_view)

    def handle_from_connexion_view_to_connexion_form(self) -> None:
        self.pygame_controller.show_view(self.connexion_form_view)

    def handle_create_account(self, user: User):
        try:
            self.get_my_interface_to_data().create_new_profile(user)
            self.get_my_interface_to_data().connect_to_app(user.nickname, user.password)
            self.server_infos_view.set_is_last_view_connexion_form(False)
            self.pygame_controller.show_view(self.server_infos_view)

        except:
            print("Unexpected error:", sys.exc_info()[0])
            self.inscription_view.register_error.show()

    def handle_go_to_connection_view(self):
        self.pygame_controller.show_view(self.connection_view)

    def handle_cancel_waiting_screen(self):
        self.home_view.waiting_game_pop_up.hide()

    def handle_close_error_creating_game(self):
        self.home_view.error_creating_game_pop_up.hide()

    @threaded
    def handle_disconnect(self):
        # disconnect from server
        self.get_my_interface_to_comm().disconnect_server()
        self.get_my_interface_to_data().disconnect_server()
        # disconnect from profile
        self.get_my_interface_to_data().disconnect_from_app()
        # display connection view
        self.pygame_controller.show_view(self.connection_view)
