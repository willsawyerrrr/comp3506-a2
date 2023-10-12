import decimal
from typing import TypeVar

from structures.m_entry import Destination, Entry
from structures.m_extensible_list import ExtensibleList
from structures.m_graph import Graph
from structures.m_map import Map
from structures.m_pqueue import PriorityQueue
from structures.m_stack import Stack
from structures.m_util import Hashable, TraversalFailure

Datum = TypeVar("Datum")


def has_cycles(graph: Graph[Datum]) -> bool:
    """
    Task 3.1: Cycle detection

    @param: graph
        The general graph to process

    @returns: bool
        Whether or not the graph contains cycles
    """
    graph_size = graph.get_num_nodes()
    visited_nodes = ExtensibleList(graph_size)

    for node in range(graph_size):
        if not visited_nodes[node]:
            if has_cycle_around(
                graph,
                node,
                visited_nodes,
                ExtensibleList(),
            ):
                return True

    return False


def has_cycle_around(
    graph: Graph[Datum],
    node: int,
    visited_nodes: ExtensibleList,
    visited_edges: ExtensibleList,
    previous_node: int = None,
) -> bool:
    visited_nodes[node] = True

    for neighbour in graph.get_neighbours(node):
        neighbour = neighbour.get_id()
        edge = (neighbour, node) if neighbour < node else (node, neighbour)

        if edge not in visited_edges:
            if not visited_nodes[neighbour]:
                visited_edges.append(edge)
                if has_cycle_around(
                    graph, neighbour, visited_nodes, visited_edges, node
                ):
                    return True
            elif neighbour != previous_node:
                return True

    return False


def enumerate_hubs(graph: Graph[Datum], min_degree: int) -> ExtensibleList:
    """
    Task 3.2: Hub enumeration

    @param: graph
        The general graph to process
    @param: min_degree
        the lowest degree a vertex can have to be considered a hub

    @returns: ExtensibleList
        A list of all Node IDs corresponding to the largest subgraph
        where each vertex has a degree of at least min_degree.
    """
    graph_size = graph.get_num_nodes()
    degrees = ExtensibleList(graph_size)
    deleted = ExtensibleList(graph_size)

    for node in range(graph_size):
        degrees[node] = len(graph.get_neighbours(node))

    for node in range(graph_size):
        if not deleted[node] and degrees[node] < min_degree:
            delete_node(graph, min_degree, node, degrees, deleted)

    result = ExtensibleList()
    for node in range(graph_size):
        if not deleted[node]:
            result.append(node)

    return result


def delete_node(
    graph: Graph[Datum],
    min_degree: int,
    node: int,
    degrees: ExtensibleList[int],
    deleted: ExtensibleList[bool],
):
    deleted[node] = True
    degrees[node] = None

    for neighbour in graph.get_neighbours(node):
        neighbour = neighbour.get_id()
        if not deleted[neighbour]:
            degrees[neighbour] -= 1
            if degrees[neighbour] < min_degree:
                delete_node(graph, min_degree, neighbour, degrees, deleted)


def calculate_flight_budget(
    graph: Graph[Datum], origin: int, stopover_budget: int, monetary_budget: int
) -> ExtensibleList:
    """
    Task 3.3: Big Bogan Budget Bonanza

    @param: graph
        The general graph to process
    @param: origin
        The origin from where the passenger wishes to fly
    @param: stopover_budget
        The maximum number of stopovers the passenger is willing to make
    @param: monetary_budget
        The maximum amount of money the passenger is willing to spend

    @returns: ExtensibleList
        The sorted list of viable destinations satisfying stopover and budget constraints.
        Each element of the ExtensibleList should be of type Destination - see
        m_entry.py for the definition of that type.
    """
    graph_size = graph.get_num_nodes()
    queue = PriorityQueue()
    distances = ExtensibleList(graph_size)

    parents = Map()

    queue.insert(0, origin)

    for node in range(graph_size):
        if node == origin:
            distances[node] = Entry(node, 0)
        else:
            distances[node] = Entry(node, decimal.MAX_EMAX)

    while not queue.is_empty():
        node = queue.remove_min()
        for neighbour, weight in graph.get_neighbours(node):
            neighbour = neighbour.get_id()
            monetary_cost = distances[node].get_value() + weight
            if monetary_cost < distances[neighbour].get_value():
                distances[neighbour] = Entry(neighbour, monetary_cost)
                queue.insert(monetary_cost, neighbour)
                parents.insert_kv(neighbour, node)

    results = ExtensibleList()
    for i in range(graph_size):
        if i == origin:
            continue

        monetary_cost = distances[i].get_value()
        stopover_cost = 0

        parent = parents[i]

        while parent != origin:
            stopover_cost += 1
            parent = parents[parent]

        if stopover_cost <= stopover_budget and monetary_cost <= monetary_budget:
            results.append(Destination(i, monetary_cost, monetary_cost, stopover_cost))

    results.sort()

    return results


def maintenance_optimisation(graph: Graph[Datum], origin: int) -> ExtensibleList:
    """
    Task 3.4: BA Field Maintenance Optimisation

    @param: graph
        The general graph to process
    @param: origin
        The origin where the aircraft requiring maintenance is

    @returns: ExtensibleList
        The list of all reachable destinations with the shortest path costs.
        Please use the Entry type here, with the key being the node identifier,
        and the value being the cost.
    """
    graph_size = graph.get_num_nodes()
    queue = PriorityQueue()
    distances = ExtensibleList(graph_size)

    queue.insert(0, origin)

    for node in range(graph_size):
        if node == origin:
            distances[node] = Entry(node, 0)
        else:
            distances[node] = Entry(node, decimal.MAX_EMAX)

    while not queue.is_empty():
        node = queue.remove_min()
        for neighbour, weight in graph.get_neighbours(node):
            neighbour = neighbour.get_id()
            distance = distances[node].get_value() + weight
            if distance < distances[neighbour].get_value():
                distances[neighbour] = Entry(neighbour, distance)
                queue.insert(distance, neighbour)

    return distances


def all_city_logistics(graph: Graph[Datum]) -> Map:
    """
    Task 3.5: All City Logistics

    @param: graph
        The general graph to process

    @returns: Map
        The map containing node pairs as keys and the cost of the shortest path
        between them as values. So, the node pairs should be inserted as keys
        of the form "0_1" where 0 is the origin node and 1 is the target node
      (their type is a string using an underscore as a seperator). The
        value should be an integer (cost of the path), or a TraversalFailure
        enumeration.
    """

    pass
