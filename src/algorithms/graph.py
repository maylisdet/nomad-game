from typing import List, Tuple
from networkx import Graph, connected_components

Position = Tuple[int, int]
Path = Tuple[Position, Position]


def connected_node_groups(l: List[Path]):
    graph = Graph()
    graph.add_edges_from(l)
    return sorted(connected_components(graph), key=len, reverse=True)


def biggest_connected_group(l: List[Path]):
    connected_groups = connected_node_groups(l)
    if len(connected_groups) == 0:
        return 0
    else:
        return connected_groups[0]
