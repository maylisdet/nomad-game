#!/usr/bin/env python3

import unittest

from algorithms import a_star


class TestAStar(unittest.TestCase):
    def test_a_star_success(self):
        result = a_star(
            (0, 0),
            (3, 3),
            [
                [1, 0, 1, 1, 1],
                [1, 0, 1, 1, 1],
                [1, 0, 1, 1, 1],
                [1, 0, 0, 1, 1],
                [1, 1, 1, 1, 1],
            ],
        )

        self.assertEqual(
            result,
            [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (4, 3), (3, 3)],
        )

    def test_a_star_fail(self):
        result = a_star(
            (0, 0),
            (3, 3),
            [
                [1, 0, 1, 1, 1],
                [1, 0, 1, 1, 1],
                [1, 0, 1, 1, 1],
                [1, 0, 0, 1, 1],
                [1, 1, 0, 1, 1],
            ],
        )

        self.assertEqual(result, None)


if __name__ == "__main__":
    unittest.main()
