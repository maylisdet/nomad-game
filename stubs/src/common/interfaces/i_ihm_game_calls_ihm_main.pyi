import abc
from abc import ABC, abstractmethod

class I_IHMGameCallsIHMMain(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def ihm_game_stoped(self) -> None: ...
