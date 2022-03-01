from abc import ABC, abstractmethod


class I_IHMServerCallsComm(ABC):
    """@abstractmethod
    async def start_server(self, ip: str, port: int) -> None:
        pass"""

    @abstractmethod
    async def start_server(self, server) -> None:
        pass

    @abstractmethod
    def quit_server(self) -> None:
        pass
