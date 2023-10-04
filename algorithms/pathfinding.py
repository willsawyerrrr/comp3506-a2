from typing import TypeVar

from structures.m_entry import Entry
from structures.m_extensible_list import ExtensibleList
from structures.m_graph import Graph, LatticeGraph
from structures.m_map import Map
from structures.m_pqueue import PriorityQueue
from structures.m_stack import Stack
from structures.m_util import Hashable, TraversalFailure

Datum = TypeVar("Datum")


def dfs_traversal(
    graph: Graph[Datum] | LatticeGraph[Datum], origin: int, goal: int
) -> tuple[ExtensibleList, ExtensibleList] | tuple[TraversalFailure, ExtensibleList]:
    """
    Task 2.1: Depth First Search

    @param: graph
        The general graph or lattice graph to process
    @param: origin
        The ID of the node from which to start traversal
    @param: goal
        The ID of the target node

    @returns: tuple[ExtensibleList, ExtensibleList]
        1. The ordered path between the origin and the goal in node IDs;
        2. The IDs of all nodes in the order they were visited.
    @returns: tuple[TraversalFailure, ExtensibleList]
        1. TraversalFailure signals that the path between the origin and the target can not be found;
        2. The IDs of all nodes in the order they were visited.
    """
    # Stores the keys of the nodes in the order they were visited
    visited_order = ExtensibleList()
    # Stores the path from the origin to the goal
    path = Stack()
    # Stores the nodes that have been visited
    visited = ExtensibleList(graph.get_num_nodes())

    path_or_failure, visited_order = dfs_helper(
        graph, origin, goal, visited, visited_order, path
    )
    if isinstance(path_or_failure, TraversalFailure):
        return (path_or_failure, visited_order)

    reversed_path = ExtensibleList()
    while not path.is_empty():
        reversed_path.append(path.pop())

    return (reversed_path, visited_order)


def dfs_helper(
    graph: Graph[Datum] | LatticeGraph[Datum],
    origin: int,
    goal: int,
    visited: ExtensibleList,
    visited_order: ExtensibleList,
    path: Stack,
) -> tuple[Stack, ExtensibleList] | tuple[TraversalFailure, ExtensibleList]:
    visited.set_at(origin, True)
    visited_order.append(origin)

    if origin == goal:
        path.push(origin)
        return (path, visited_order)

    for neighbour in reversed(graph.get_neighbours(origin)):
        neighbour = neighbour.get_id()
        if not visited.get_at(neighbour):
            path_or_failure, visited_order = dfs_helper(
                graph, neighbour, goal, visited, visited_order, path
            )
            if isinstance(path_or_failure, Stack):
                path.push(origin)
                return (path_or_failure, visited_order)

    return (TraversalFailure.DISCONNECTED, visited_order)


def bfs_traversal(
    graph: Graph[Datum] | LatticeGraph[Datum], origin: int, goal: int
) -> tuple[ExtensibleList, ExtensibleList] | tuple[TraversalFailure, ExtensibleList]:
    """
    Task 2.1: Breadth First Search

    @param: graph
        The general graph or lattice graph to process
    @param: origin
        The ID of the node from which to start traversal
    @param: goal
        The ID of the target node

    @returns: tuple[ExtensibleList, ExtensibleList]
        1. The ordered path between the origin and the goal in node IDs;
        2. The IDs of all nodes in the order they were visited.
    @returns: tuple[TraversalFailure, ExtensibleList]
        1. TraversalFailure signals that the path between the origin and the target can not be found;
        2. The IDs of all nodes in the order they were visited.
    """
    # Stores the keys of the nodes in the order they were visited
    visited_order = ExtensibleList()
    # Stores the path from the origin to the goal
    path = ExtensibleList()

    # If everything worked, you should return like this
    return (path, visited_order)
    # If you couldn't get to the goal, you should return like this
    return (TraversalFailure.DISCONNECTED, visited_order)


def greedy_traversal(
    graph: LatticeGraph[Datum], origin: int, goal: int
) -> tuple[ExtensibleList, ExtensibleList] | tuple[TraversalFailure, ExtensibleList]:
    """
    Task 2.2: Greedy Traversal

    @param: graph
        The lattice graph to process
    @param: origin
        The ID of the node from which to start traversal
    @param: goal
        The ID of the target node

    @returns: tuple[ExtensibleList, ExtensibleList]
        1. The ordered path between the origin and the goal in node IDs;
        2. The IDs of all nodes in the order they were visited.
    @returns: tuple[TraversalFailure, ExtensibleList]
        1. TraversalFailure signals that the path between the origin and the target can not be found;
        2. The IDs of all nodes in the order they were visited.
    """
    pass


def distance(x_1: float, y_1: float, x_2: float, y_2: float) -> float:
    """
    Return the distance between a point at coordinate (x_1, y_1) and a point
    at coordinate (x_2, y_2). You may re-write this method with other
    parameters if you wish. Please comment on your choice of distance function.
    """
    pass


def max_traversal(
    graph: LatticeGraph[Datum], origin: int, goal: int
) -> tuple[ExtensibleList, ExtensibleList] | tuple[TraversalFailure, ExtensibleList]:
    """
    Task 2.3: Maximize vertex visits traversal

    @param: graph
        The lattice graph to process
    @param: origin
        The ID of the node from which to start traversal
    @param: goal
        The ID of the target node

    @returns: tuple[ExtensibleList, ExtensibleList]
        1. The ordered path between the origin and the goal in node IDs;
        2. The IDs of all nodes in the order they were visited.
    @returns: tuple[TraversalFailure, ExtensibleList]
        1. TraversalFailure signals that the path between the origin and the target can not be found;
        2. The IDs of all nodes in the order they were visited.
    """
    pass
