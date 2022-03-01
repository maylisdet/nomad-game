import abc
from abc import ABC, abstractmethod
from common.data_structures.local_game import LocalGame as LocalGame
from common.data_structures.profiles import Profile as Profile
from uuid import UUID

class I_IHMMainCallsComm(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def remove_game(self, game_id: UUID) -> None: ...
    @abstractmethod
    def get_profile_info(self, user_id: UUID) -> None: ...
    @abstractmethod
    def create_game(self, local_game: LocalGame) -> None: ...
    @abstractmethod
    def update_profile(self, profil: Profile) -> None: ...
    @abstractmethod
    def spectate_game(self, user_id: UUID, game_id: UUID) -> None: ...
    @abstractmethod
    def join_game(self, user_id: UUID, game_id: UUID) -> None: ...
    @abstractmethod
    def connect_to_server(self, ip: str, port: int) -> None: ...
    @abstractmethod
    def disconnect_server(self) -> None: ...
