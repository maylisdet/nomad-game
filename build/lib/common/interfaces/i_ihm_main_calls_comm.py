from abc import ABC, abstractmethod
from uuid import UUID
from common import Profile
from common import LocalGame


class I_IHMMainCallsComm(ABC):
    @abstractmethod
    def remove_game(self, game_id: UUID) -> None:
        pass

    @abstractmethod
    def get_profile_info(self, user_id: UUID) -> None:
        pass

    @abstractmethod
    def create_game(self, local_game: LocalGame) -> None:
        pass

    @abstractmethod
    def update_profile(self, profil: Profile) -> None:
        pass

    @abstractmethod
    def spectate_game(self, user_id: UUID, game_id: UUID) -> None:
        pass

    @abstractmethod
    def join_game(self, user_id: UUID, game_id: UUID) -> None:
        pass

    @abstractmethod
    async def connect_to_server(self, ip: str, port: int) -> None:
        pass

    @abstractmethod
    def disconnect_server(self) -> None:
        pass
