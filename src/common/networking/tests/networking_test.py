#!/usr/bin/env python3

import unittest
from common import IO


def callback():
    return True


class Transport:
    def get_extra_info(self, s):
        return ("localhost", 0)


class TestIO(unittest.TestCase):
    def test_on(self):
        IO.on("id1", callback)
        self.assertEqual(IO.callback_map["id1"], [callback])

        IO.on("id2", callback)
        IO.on("id2", callback)
        self.assertEqual(IO.callback_map["id2"], [callback, callback])

    def test_connection_made(self):
        io = IO()
        io.connection_made(Transport())
        self.assertEqual(IO.client_map[0], io)
        self.assertEqual(io.socket_id, 0)

    def test_connection_lost(self):
        io = IO()
        io.connection_made(Transport())
        io.connection_lost(None)
        self.assertEqual(len(IO.client_map), 0)


if __name__ == "__main__":
    unittest.main()
