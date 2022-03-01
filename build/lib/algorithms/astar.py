#!/usr/bin/env python3
#!/usr/bin/env python3

from typing import Tuple, List, Callable, Optional, Dict, Any
import functools
import math

Position = Tuple[int, int]
PositionWithDepth = Tuple[int, int, int]
Board = List[List[int]]
Path = List[Position]
PathWithDepth = List[PositionWithDepth]


def search(
    s0: PositionWithDepth,
    goal: Position,
    succ: Callable[[PositionWithDepth, Any], PathWithDepth],
    remove: Callable[
        [PathWithDepth, Position], Tuple[PositionWithDepth, PathWithDepth]
    ],
    insert: Callable[[PositionWithDepth, PathWithDepth], PathWithDepth],
    grid: Board,
    max: int,
    depth: int = 0,
) -> Tuple[
    Optional[PositionWithDepth], Dict[PositionWithDepth, Optional[PositionWithDepth]]
]:
    l = [s0]
    save: Dict[PositionWithDepth, Optional[PositionWithDepth]] = {s0: None}
    while l:
        s, l = remove(l, goal)
        state_without_depth: Position = (s[0], s[1])
        if state_without_depth == goal:
            return s, save
        elif s[2] > max:
            return None, save
        else:
            for s2 in succ(s, grid):
                if not s2 in save:
                    save[s2] = s
                    insert(s2, l)
    return None, save


def remove_a_star(
    l: PathWithDepth, goal: Position
) -> Tuple[PositionWithDepth, PathWithDepth]:
    l.sort(key=functools.partial(a_star_heuristic, goal=goal))
    return l.pop(0), l


def insert_a_star(s: PositionWithDepth, l: PathWithDepth) -> PathWithDepth:
    l.append(s)
    return l


def manhattan_distance(f: Position, to: Position) -> int:
    return abs(f[0] - to[0]) + abs(f[1] - to[0])


def a_star_heuristic(s: PositionWithDepth, goal: Position) -> int:
    s_without_depth: Position = (s[0], s[1])
    return manhattan_distance(s_without_depth, goal) + s[2]


def is_free(x: int, y: int, grid: Board) -> bool:
    return grid[x][y] == 1


def succ_with_depth(s: PositionWithDepth, grid: Board) -> PathWithDepth:
    successors: PathWithDepth = []
    x = s[0]
    y = s[1]
    depth = s[2]
    n = len(grid)

    if x + 1 < n and is_free(x + 1, y, grid):
        successors.append((x + 1, y, depth + 1))
    if y + 1 < n and is_free(x, y + 1, grid):
        successors.append((x, y + 1, depth + 1))
    if x > 0 and is_free(x - 1, y, grid):
        successors.append((x - 1, y, depth + 1))
    if y > 0 and is_free(x, y - 1, grid):
        successors.append((x, y - 1, depth + 1))
    return successors


def dict2path(s, d):
    l = [s]
    parent = d[s]
    while not parent is None:
        l.append(parent)
        s = parent
        parent = d[s]

    l.reverse()

    l2 = []
    for elem in l:
        l2.append((elem[0], elem[1]))
    return l2


def a_star(s0: Position, goal: Position, grid: Board) -> Optional[Path]:
    n = len(grid)
    limit = n * (math.ceil(n // 2)) + math.ceil(n // 2)

    state0 = (s0[0], s0[1], 0)
    g, save = search(
        state0, goal, succ_with_depth, remove_a_star, insert_a_star, grid, limit
    )

    if g == None:
        return None

    return dict2path(g, save)
