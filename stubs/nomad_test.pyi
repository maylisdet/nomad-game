import unittest
from enum import Enum

class V(Enum):
    E: int
    R: int
    W: int
    T: int

class TestAStar(unittest.TestCase):
    def test_normalize_board(self) -> None: ...
    def test_get_all_paths(self) -> None: ...
    def test_get_winner(self) -> None: ...
    def test_get_winner_draw(self) -> None: ...
