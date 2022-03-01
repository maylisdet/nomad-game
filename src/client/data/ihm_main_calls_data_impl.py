from __future__ import annotations

from typing import List
import uuid as uuid_lib
import os
from common import Profile, LocalGame, Player, User, PlayerType

from typing import TYPE_CHECKING
import pickle

from common import GameStatus
from common.utils import USER_PATH


if TYPE_CHECKING:
    from client.data.data_controller import DataController

from common.interfaces.i_ihm_main_calls_data import I_IHMMainCallsData

DEFAULT_TILE_NUMBER = 165
DEFAULT_STATUS = GameStatus.AVAILABLE
DEFAULT_ROUND = 0
EXT_FILE = ".profile"


class IhmMainCallsData_Impl(I_IHMMainCallsData):
    def __init__(self, data_controller: DataController):
        self.data_controller = data_controller

    def get_public_games(self) -> List:
        return self.data_controller.public_games

    def get_connected_players(self) -> List[Player]:
        return self.data_controller.connected_players

    def get_local_game_id(self) -> uuid_lib.UUID:
        pass

    def get_profile(self) -> Profile:
        if self.data_controller.myself is not None:
            return self.data_controller.myself.get_profile()
        else:
            raise Exception("No local user found, no profile can be provided")

    def create_new_profile(self, user: User) -> None:
        """
        Doesnt 'create' anything.
        Saves the user object to a file.
        Does not check if the nickname is already taken.
        """
        os.makedirs(USER_PATH, exist_ok=True)
        profile_path = USER_PATH + user.nickname + EXT_FILE
        with open(profile_path, "wb") as profile_file:
            pickle.dump(user, profile_file)

    def create_game(
        self, name: str, tower_nb: int, player_choice: PlayerType
    ) -> LocalGame:
        profile = self.get_profile()
        player = profile
        red_player = player if player_choice is PlayerType.RED else None
        white_player = player if player_choice is PlayerType.WHITE else None
        self.data_controller.local_game = LocalGame(
            name,
            profile,
            DEFAULT_TILE_NUMBER,
            tower_nb,
            DEFAULT_STATUS,
            red_player,
            white_player,
            DEFAULT_ROUND,
        )
        return self.data_controller.local_game

    def export_current_profile(self, destination_path: str) -> None:
        pass

    def import_profile(self, path: str) -> Profile:
        pass

    def edit_current_profile(self, profile: Profile) -> None:
        pass

    def disconnect_from_app(self) -> None:
        """
        Remove the current user from the attached data_controller
        Could be improved by saving the current myuser to a file, but this leads to mypy errors in the commented way.
        """
        # if backup_current_user_to_disk:
        #     self.create_new_profile()
        self.data_controller.myself = None

    def disconnect_server(self) -> None:
        """
        Remove datacontroller server-related data
        """
        self.data_controller.connected_players = []
        self.data_controller.public_games = []
        self.data_controller.local_game = None

    def connect_to_app(self, nickname: str, password: str) -> None:
        """
        Doesnt connect to the server, just retrieves the user object from a file
        """

        # retrieve the profile from the file
        user_path = USER_PATH + nickname + EXT_FILE  # A uuid would have been safer
        try:
            with open(user_path, "rb") as user_file:
                user = pickle.load(user_file)

                # check if the password is correct
                if user.password == password:
                    self.data_controller.myself = user
                else:
                    raise ValueError("Wrong password")
        except FileNotFoundError:
            raise ValueError(f"User {nickname} not found.")
