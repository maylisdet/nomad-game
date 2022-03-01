from abc import ABC, abstractmethod


class I_CommCallsIHMGame(ABC):
    @abstractmethod
    def notify_new_spectator(self) -> None:
        pass

    @abstractmethod
    def spectator_quits_game(self) -> None:
        pass

    @abstractmethod
    def update_game(self) -> None:
        pass

    @abstractmethod
    def notify_new_message(self) -> None:
        pass
