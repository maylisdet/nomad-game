#!/usr/bin/env python3

import unittest

from algorithms import connected_node_groups, biggest_connected_group


class TestConnectedNodeGroups(unittest.TestCase):
    def test_connected_node_groups(self):
        result = connected_node_groups(
            [((0, 0), (3, 3)), ((3, 3), (1, 1)), ((1, 1), (4, 4)), ((2, 2), (5, 5))]
        )

        self.assertEqual(result, [{(4, 4), (1, 1), (3, 3), (0, 0)}, {(5, 5), (2, 2)}])

    def test_biggest_connected_group(self):
        result = biggest_connected_group(
            [((0, 0), (3, 3)), ((3, 3), (1, 1)), ((1, 1), (4, 4)), ((2, 2), (5, 5))]
        )

        self.assertEqual(result, {(4, 4), (1, 1), (3, 3), (0, 0)})


if __name__ == "__main__":
    unittest.main()
