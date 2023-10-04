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
    # Stores the keys of the nodes that have been visited
    visited = ExtensibleList(graph.get_num_nodes())
    # Stores the parent of each node
    parents = Map()

    queue = PriorityQueue()
    queue.insert_fifo(origin)

    while not queue.is_empty():
        node = queue.remove_min()
        visited.set_at(node, True)
        visited_order.append(node)

        if node == goal:
            break

        for neighbour in graph.get_neighbours(node):
            neighbour = neighbour.get_id()
            if not visited.get_at(neighbour):
                queue.insert_fifo(neighbour)
                parents.insert_kv(neighbour, node)
    else:
        return (TraversalFailure.DISCONNECTED, visited_order)

    stack = Stack()
    while node != origin:
        stack.push(node)
        node = parents.find(node)

    path = ExtensibleList()
    path.append(origin)
    while not stack.is_empty():
        path.append(stack.pop())

    return (path, visited_order)


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
    # Stores the keys of the nodes in the order they were visited
    visited_order = ExtensibleList()
    # Stores the keys of the nodes that have been visited
    visited = ExtensibleList(graph.get_num_nodes())
    # Stores the parent of each node
    parents = Map()

    queue = PriorityQueue()
    queue.insert(0, origin)

    while not queue.is_empty():
        node = queue.remove_min()
        visited.set_at(node, True)
        visited_order.append(node)

        if node == goal:
            break

        for neighbour in graph.get_neighbours(node):
            neighbour = neighbour.get_id()
            if not visited.get_at(neighbour):
                queue.insert(
                    distance(
                        graph.get_node(node).get_coordinates(),
                        graph.get_node(neighbour).get_coordinates(),
                    ),
                    neighbour,
                )
                parents.insert_kv(neighbour, node)
    else:
        return (TraversalFailure.DISCONNECTED, visited_order)

    stack = Stack()
    while node != origin:
        stack.push(node)
        node = parents.find(node)

    path = ExtensibleList()
    path.append(origin)
    while not stack.is_empty():
        path.append(stack.pop())

    return (path, visited_order)


def distance(p: tuple[int, int], q: tuple[int, int]) -> float:
    """
    Return the distance between a point a and a point q.
    """
    # Manhattan distance as it is the most appropriate for a lattice graph
    return abs(p[0] - q[0]) + abs(p[1] - q[1])


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
