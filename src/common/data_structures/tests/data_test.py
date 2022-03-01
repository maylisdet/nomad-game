#!/usr/bin/env python3

import unittest
from uuid import uuid4

from common import Message, Player


class TestData(unittest.TestCase):
    def test_message(self):
        u = uuid4()
        player = Player("Jean Michel le parpaing", u)
        message = Message(u, player, "coucou", 234567)
        assert message is not None and player is not None


if __name__ == "__main__":
    unittest.main()
