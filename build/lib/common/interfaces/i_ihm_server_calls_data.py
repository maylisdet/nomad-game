from abc import ABC, abstractmethod


class I_IHMServerCallsData(ABC):
    @abstractmethod
    def start_server(self) -> None:
        pass

    @abstractmethod
    def quit_server(self) -> None:
        pass
