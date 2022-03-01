#!/usr/bin/env python3

import unittest

from algorithms import normalize_board, get_all_paths, get_winner
from enum import Enum


class V(Enum):
    E = 0
    R = 1
    W = 2
    T = 3


class TestAStar(unittest.TestCase):
    def test_normalize_board(self):

        result = normalize_board(
            [
                [V.T, V.R, V.R, V.T, V.E],
                [V.W, V.E, V.E, V.R, V.E],
                [V.W, V.E, V.E, V.R, V.E],
                [V.W, V.E, V.E, V.R, V.E],
                [V.T, V.R, V.R, V.T, V.E],
            ],
            [V.T, V.R],
        )

        self.assertEqual(
            result,
            [
                [1, 1, 1, 1, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 1, 0],
                [1, 1, 1, 1, 0],
            ],
        )

        result = normalize_board(
            [
                [V.T, V.R, V.R, V.T, V.E],
                [V.W, V.E, V.E, V.R, V.E],
                [V.W, V.E, V.E, V.R, V.E],
                [V.W, V.E, V.E, V.R, V.E],
                [V.T, V.R, V.R, V.T, V.E],
            ],
            [V.T, V.W],
        )

        self.assertEqual(
            result,
            [
                [1, 0, 0, 1, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 1, 0],
            ],
        )

    def test_get_all_paths(self):
        result = get_all_paths(
            [
                [1, 0, 0, 1, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 0, 0],
                [1, 0, 0, 1, 0],
            ],
            [(0, 0), (4, 0), (0, 3), (4, 3)],
        )

        self.assertEqual(result, [((0, 0), (4, 0))])

        result = get_all_paths(
            [
                [1, 1, 1, 1, 0],
                [1, 0, 0, 1, 0],
                [1, 0, 0, 1, 0],
                [1, 0, 0, 1, 0],
                [1, 0, 0, 1, 0],
            ],
            [(0, 0), (4, 0), (0, 3), (4, 3)],
        )

        self.assertTrue(((0, 0), (4, 0)) in result)
        self.assertTrue(((0, 0), (0, 3)) in result)
        self.assertTrue(((0, 3), (4, 3)) in result)

    def test_get_winner(self):
        result = get_winner(
            [
                [V.T, V.R, V.R, V.T, V.E],
                [V.W, V.E, V.E, V.R, V.E],
                [V.W, V.E, V.E, V.R, V.E],
                [V.W, V.E, V.E, V.R, V.E],
                [V.T, V.R, V.R, V.T, V.E],
            ],
            tower_positions=[(0, 0), (4, 0), (0, 3), (4, 3)],
            tower_value=V.T,
            red_value=V.R,
            white_value=V.W,
        )

        self.assertEqual(result, "red")

    def test_get_winner_draw(self):
        result = get_winner(
            [
                [V.T, V.E, V.E, V.T, V.E],
                [V.W, V.E, V.E, V.R, V.E],
                [V.W, V.E, V.E, V.R, V.E],
                [V.W, V.E, V.E, V.R, V.E],
                [V.T, V.E, V.E, V.T, V.E],
            ],
            tower_positions=[(0, 0), (4, 0), (0, 3), (4, 3)],
            tower_value=V.T,
            red_value=V.R,
            white_value=V.W,
        )

        self.assertEqual(result, "draw")


if __name__ == "__main__":
    unittest.main()
