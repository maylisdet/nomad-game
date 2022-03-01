import abc
from abc import ABC, abstractmethod

class I_IHMServerCallsComm(ABC, metaclass=abc.ABCMeta):
    @abstractmethod
    def start_server(self, ip: str, port: int) -> None: ...
    @abstractmethod
    def quit_server(self) -> None: ...
