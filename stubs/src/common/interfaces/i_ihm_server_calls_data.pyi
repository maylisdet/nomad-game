import abc
from abc import ABC, abstractmethod

class I_IHMServerCallsData(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def start_server(self) -> None: ...
    @abstractmethod
    def quit_server(self) -> None: ...
