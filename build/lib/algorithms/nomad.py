#!/usr/bin/env python3

from typing import List, Tuple, Any

from algorithms import a_star
from algorithms import biggest_connected_group
from functools import partial
from itertools import combinations

Position = Tuple[int, int]
Board = List[List[int]]


def normalize_board(board: Board, values_from):
    return [[0 if v not in values_from else 1 for v in row] for row in board]


def get_all_paths(board: Board, tower_positions: List[Position]):
    paths = []
    for start, end in combinations(tower_positions, 2):
        path = a_star(start, end, board)
        if path is not None:
            paths.append((start, end))
    return paths


def get_winner(
    board: Board,
    tower_positions: List[Position],
    tower_value: Any,
    red_value: Any,
    white_value: Any,
):
    red_board = normalize_board(board, [red_value, tower_value])
    white_board = normalize_board(board, [white_value, tower_value])

    red_paths = get_all_paths(red_board, tower_positions)
    white_paths = get_all_paths(white_board, tower_positions)

    red_score = biggest_connected_group(red_paths)
    white_score = biggest_connected_group(white_paths)

    if red_score > white_score:
        return "red"
    elif red_score < white_score:
        return "white"
    else:
        return "draw"
