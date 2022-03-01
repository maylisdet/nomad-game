from abc import ABC, abstractmethod
from typing import List
import uuid as uuid_lib
from common import Profile, LocalGame, Player, PublicGame, User, PlayerType


class I_IHMMainCallsData(ABC):
    @abstractmethod
    def get_local_game_id(self) -> uuid_lib.UUID:
        pass

    @abstractmethod
    def get_profile(self) -> Profile:
        pass

    @abstractmethod
    def create_new_profile(self, user: User) -> None:
        pass

    @abstractmethod
    def create_game(
        self, name: str, tiles: int, player_choice: PlayerType
    ) -> LocalGame:
        pass

    @abstractmethod
    def export_current_profile(self, destination_path: str) -> None:
        pass

    @abstractmethod
    def import_profile(self, path: str) -> Profile:
        pass

    @abstractmethod
    def edit_current_profile(self, profile: Profile) -> None:
        pass

    @abstractmethod
    def get_connected_players(self) -> List[Player]:
        pass

    @abstractmethod
    def get_public_games(self) -> List[PublicGame]:
        pass

    @abstractmethod
    def disconnect_from_app(self) -> None:
        pass

    @abstractmethod
    def disconnect_server(self) -> None:
        pass

    @abstractmethod
    def connect_to_app(self, nickname: str, password: str) -> None:
        pass
