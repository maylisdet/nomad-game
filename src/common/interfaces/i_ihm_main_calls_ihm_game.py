from abc import ABC, abstractmethod


class I_IHMMainCallsIHMGame(ABC):

    """

    Interface IHM Main Calls IHM Game

    """

    @abstractmethod
    def launch_spectate_game(self) -> None:
        pass

    @abstractmethod
    def launch_ihm_game(self) -> None:
        pass
