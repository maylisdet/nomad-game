#!/usr/bin/env python3

import asyncio
import argparse
import jsonpickle

from typing import Dict, Any, Callable
from common import IO, create_server


def callback1(data: Dict[Any, Any], io):
    print(f"Message of id 'test' called with data: {data} from {io.peername}1.")
    message = {"id": "test", "data": f"hello {io.peername}"}
    io.write(message)


def callback2(data: Dict[Any, Any], io):
    print(f"Message of id 'test' called with data: {data} from {io.peername}2.")


async def main():
    parser = argparse.ArgumentParser(description="Server")
    parser.add_argument("--port", type=int, help="The server's port", default=8888)
    args = parser.parse_args()

    IO.on("test", callback1)
    IO.on("test", callback2)

    server = await create_server("localhost", args.port)
    await server.serve_forever()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
