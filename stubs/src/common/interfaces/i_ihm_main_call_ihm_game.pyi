import abc
from abc import ABC, abstractmethod

class I_IHMGameCallsIHMMain(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def launch_spectate_game(self) -> None: ...
    @abstractmethod
    def launch_ihm_game(self) -> None: ...
