import abc
from abc import ABC, abstractmethod
from common.data_structures.message import Message as Message
from common.data_structures.move import Move as Move
from uuid import UUID

class I_IHMGameCallsComm(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def send_message(self, message: Message) -> None: ...
    @abstractmethod
    def place_tile(self, move: Move) -> None: ...
    @abstractmethod
    def quit_spectator_interface(self, user_id: UUID, game_id: UUID) -> None: ...
