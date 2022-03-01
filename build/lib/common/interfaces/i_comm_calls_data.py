from abc import ABC, abstractmethod
from typing import List
import uuid as uuid_lib
from common import LocalGame, Player, PublicGame, Move, Message, Profile


class I_CommCallsData(ABC):
    @abstractmethod
    def remove_local_game(self) -> None:
        pass

    @abstractmethod
    def store_current_game(self, local_game: LocalGame) -> None:
        pass

    @abstractmethod
    def store_local_game(self, local_game: LocalGame) -> None:
        pass

    @abstractmethod
    def store_connected_user(self, player_list: List[Player]) -> None:
        pass

    @abstractmethod
    def store_games(self, public_game_list: List[PublicGame]) -> None:
        pass

    @abstractmethod
    def add_connected_user(self, player: Player) -> None:
        pass

    @abstractmethod
    def add_spectator_in_game(self, player: Player) -> None:
        pass

    @abstractmethod
    def remove_disconnect_player(self, user_id: uuid_lib.UUID) -> None:
        pass

    @abstractmethod
    def remove_spectator(self, user_id: uuid_lib.UUID) -> None:
        pass

    @abstractmethod
    def player_join_game(self, player: Player) -> None:
        pass

    @abstractmethod
    def update_public_game(self, public_game: PublicGame) -> None:
        pass

    @abstractmethod
    def store_new_game(self, public_game: PublicGame) -> None:
        pass

    @abstractmethod
    def add_move_to_local_game(self, move: Move, game_finished: bool) -> None:
        pass

    @abstractmethod
    def add_new_message(self, message: Message) -> None:
        pass

    @abstractmethod
    def remove_pending_game(self, game_id: uuid_lib.UUID) -> None:
        pass

    @abstractmethod
    def update_user_profile(self, profile: Profile) -> None:
        pass

    @abstractmethod
    def get_profile(self) -> Profile:
        pass
