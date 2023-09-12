from structures.m_entry import *
from structures.m_extensible_list import *
from structures.m_graph import *
from structures.m_map import *
from structures.m_pqueue import *
from structures.m_stack import *
from structures.m_util import *


def has_cycles(graph: Graph) -> bool:
    """
    Task 3.1: Cycle detection

    @param: graph
      The general graph to process

    @returns: bool
      Whether or not the graph contains cycles
    """

    pass


def enumerate_hubs(graph: Graph, min_degree: int) -> ExtensibleList:
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

    pass


def calculate_flight_budget(
    graph: Graph, origin: int, stopover_budget: int, monetary_budget: int
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
    pass


def maintenance_optimisation(graph: Graph, origin: int) -> ExtensibleList:
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
    pass


def all_city_logistics(graph: Graph) -> Map:
    """
    Task 3.5: All City Logistics

    @param: graph
      The general graph to process

    @returns: Map
      The map containing node pairs as keys and the shortest path between them as values.
    """

    pass
