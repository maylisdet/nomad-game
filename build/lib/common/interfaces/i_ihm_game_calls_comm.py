from abc import ABC, abstractmethod
from uuid import UUID
from common import Message
from common import Move


class I_IHMGameCallsComm(ABC):
    @abstractmethod
    def send_message(self, message: Message) -> None:
        pass

    @abstractmethod
    def place_tile(self, move: Move) -> None:
        pass

    @abstractmethod
    def quit_spectator_interface(self, user_id: UUID, game_id: UUID) -> None:
        pass
