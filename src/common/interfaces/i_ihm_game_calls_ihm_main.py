from abc import ABC, abstractmethod


class I_IHMGameCallsIHMMain(ABC):

    """

    Interface IHM Game Calls IHM Main

    """

    @abstractmethod
    def ihm_game_stoped(self) -> None:
        pass
