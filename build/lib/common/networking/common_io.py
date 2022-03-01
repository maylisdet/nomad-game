import asyncio
from asyncio.events import AbstractServer
from uuid import UUID
import jsonpickle
import re

from collections import defaultdict
from typing import Dict, DefaultDict, Callable, Any, Optional, List


class Buffer:
    def __init__(self, io):
        self.buf = ""
        self.io = io

    def feed_data(self, data):
        self.buf += data.decode("utf-8")

    def has_complete_message(self):
        return "!!!" in self.buf

    def read_message(self):
        result = re.findall("(.*?)!!!", self.buf)[0]
        self.buf = self.buf[self.buf.index("!!!") + 3 :]
        return result


class IO(asyncio.Protocol):
    client_map: Dict[int, "IO"] = {}
    socket_id_map: Dict[UUID, int] = {}
    callback_map: DefaultDict[str, List[Callable[[str, "IO"], None]]] = defaultdict(
        list
    )

    def __init__(self, on_connection_lost=None):
        self.on_connection_lost = on_connection_lost
        self.buffer = Buffer(self)

    def __call__(self):
        return self

    def __str__(self):
        return f"{self.ip}:{self.socket_id}"

    def connection_made(self, transport):
        self.transport = transport
        self.peername = transport.get_extra_info("peername")
        self.ip = self.peername[0]
        self.socket_id = self.peername[1]
        self.client_map[self.socket_id] = self

    def message_received(self, data):
        message = jsonpickle.decode(data)
        print(message)
        [fn(message["data"], self) for fn in IO.callback_map[message.get("id")]]

    def data_received(self, data):
        self.buffer.feed_data(data)
        while self.buffer.has_complete_message():
            self.message_received(self.buffer.read_message())

    def connection_lost(self, exc):
        IO.client_map.pop(self.socket_id)

        if self.on_connection_lost is not None:
            self.on_connection_lost.set_result(True)

    @staticmethod
    def on(id_message, fn):
        IO.callback_map[id_message].append(fn)

    @staticmethod
    def broadcast(message):
        for _, client in IO.client_map.items():
            client.write(message)

    @staticmethod
    def write_to(message: Any, client_id: UUID):
        IO.client_map[IO.socket_id_map[client_id]].write(message)

    def broadcast_to_others(self, message):
        for _, client in self.client_map.items():
            if client == self:
                continue
            client.write(message)

    def write(self, message: Any):
        message = f"{jsonpickle.encode(message)}!!!"
        self.transport.write(message.encode())


async def create_server(port: int, ip: str = "localhost") -> AbstractServer:
    loop = asyncio.get_running_loop()
    server = await loop.create_server(lambda: IO(), ip, port)
    return server


async def create_client(ip: str, port: int) -> IO:
    loop = asyncio.get_running_loop()
    on_connection_lost = loop.create_future()
    io = IO(on_connection_lost)
    _, _ = await loop.create_connection(io, ip, port)
    return io
