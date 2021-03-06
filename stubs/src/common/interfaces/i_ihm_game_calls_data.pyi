import abc
import uuid as uuid_lib
from abc import ABC, abstractmethod
from common import LocalGame as LocalGame, Message as Message, Move as Move, Player as Player
from typing import Dict, List, Tuple

class I_IHMGameCallsData(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def check_move_in_local_game(self, move: Move) -> None: ...
    @abstractmethod
    def leave_local_game(self) -> uuid_lib.UUID: ...
    @abstractmethod
    def get_local_game(self) -> LocalGame: ...
    @abstractmethod
    def get_local_game_grid(self) -> Dict: ...
    @abstractmethod
    def get_local_players(self) -> Tuple[Player, Player]: ...
    @abstractmethod
    def get_local_game_spectators(self) -> List[Player]: ...
    @abstractmethod
    def get_local_game_messages(self) -> List[Message]: ...
    @abstractmethod
    def is_local_game_finished(self) -> bool: ...
    @abstractmethod
    def get_local_winner(self) -> Player: ...
    @abstractmethod
    def clear_local_game(self) -> None: ...
