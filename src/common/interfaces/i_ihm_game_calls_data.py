from abc import ABC, abstractmethod
from typing import Dict, List, Tuple
import uuid as uuid_lib
from common import Move, LocalGame, Player, Message, Profile


class I_IHMGameCallsData(ABC):
    @abstractmethod
    def check_move_in_local_game(self, move: Move) -> bool:
        pass

    @abstractmethod
    def leave_local_game(self) -> uuid_lib.UUID:
        pass

    @abstractmethod
    def get_local_game(self) -> LocalGame:
        pass

    @abstractmethod
    def get_local_game_grid(self) -> Dict:
        pass

    @abstractmethod
    def get_local_players(self) -> Tuple[Profile, Profile]:
        pass

    @abstractmethod
    def get_local_game_spectators(self) -> List[Player]:
        pass

    @abstractmethod
    def get_local_game_messages(self) -> List[Message]:
        pass

    @abstractmethod
    def is_local_game_finished(self) -> bool:
        pass

    @abstractmethod
    def get_local_game_winner(self) -> List[Profile]:
        pass

    @abstractmethod
    def clear_local_game(self) -> None:
        pass

    def get_profile(self) -> Profile:
        pass
