#!/usr/bin/env python3

import asyncio
import argparse
import jsonpickle

from typing import Dict, Any, Callable
from common import create_client


def callback(data: Dict[Any, Any], io):
    print(f"Message of id 'test' called with data: {data} from {io.peername}.")
    # message = {"id": "test", "data": f"hello {io.peername}"}
    # transport.write(message)


async def main():
    parser = argparse.ArgumentParser(description="Client")
    parser.add_argument("--ip", type=str, help="The server's IP", default="localhost")
    parser.add_argument("--port", type=int, help="The server's port", default=8888)
    args = parser.parse_args()

    io = await create_client(args.ip, args.port)
    io.on("test", callback)
    io.write({"id": "test", "data": True})
    await io.on_connection_lost


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
