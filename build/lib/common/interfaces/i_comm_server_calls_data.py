from abc import ABC, abstractmethod
from typing import List, Tuple
import uuid as uuid_lib
from common import LocalGame, PublicGame, Player, Profile, Move, Message


class I_CommServerCallsData(ABC):
    @abstractmethod
    def create_game(self, local_game: LocalGame) -> PublicGame:
        pass

    @abstractmethod
    def add_spectator_to_game(
        self, user_id: uuid_lib.UUID, game_id: uuid_lib.UUID
    ) -> LocalGame:
        pass

    @abstractmethod
    def delete_spectator_from_game(
        self, user_id: uuid_lib.UUID, game_id: uuid_lib.UUID
    ) -> None:
        pass

    @abstractmethod
    def get_game_spectators(self, game_id: uuid_lib.UUID) -> List[Player]:
        pass

    @abstractmethod
    def get_game_players(self, game_id: uuid_lib.UUID) -> List[Player]:
        pass

    @abstractmethod
    def delete_game(self, game_id: uuid_lib.UUID) -> None:
        pass

    @abstractmethod
    def add_player_to_game(
        self, game_id: uuid_lib.UUID, user_id: uuid_lib.UUID
    ) -> LocalGame:
        pass

    @abstractmethod
    def get_profile(self, user_id: uuid_lib.UUID) -> Profile:
        pass

    @abstractmethod
    def add_move(self, move: Move) -> None:
        pass

    @abstractmethod
    def is_game_finished(self, game_id: uuid_lib.UUID) -> bool:
        pass

    @abstractmethod
    def apply_result_to_profile(
        self, game_id: uuid_lib.UUID
    ) -> Tuple[Profile, Profile]:
        pass

    @abstractmethod
    def add_message_to_game(self, game_id: uuid_lib.UUID, message: Message) -> None:
        pass

    @abstractmethod
    def update_profile(self, profile: Profile) -> None:
        pass

    @abstractmethod
    def add_user(self, profile: Profile) -> Player:
        pass

    @abstractmethod
    def get_players(self) -> List[Player]:
        pass

    @abstractmethod
    def get_available_games(self) -> List[PublicGame]:
        pass

    @abstractmethod
    def delete_user(self, user_id: uuid_lib.UUID) -> None:
        pass
