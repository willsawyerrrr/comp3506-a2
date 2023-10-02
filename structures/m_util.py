from abc import ABC, abstractmethod
from enum import Enum
from typing import TypeVar

T = TypeVar("T")


class Hashable(ABC):
    """
    A special object that can be inherited to enforce objects to be hashable.
    """

    def __init__(self) -> None:
        """
        You are free to do anything you find suitable to initialise your Hashable class.
        But maybe you don't need to do anything!
        """
        pass

    @abstractmethod
    def get_hash(self) -> int:
        """
        Return an integer hash of the given object. You MUST use this if you wish to
        hash keys of a specific type. See m_entry.py for more help in this direction, as
        well as m_map.py.
        """
        pass


class TraversalFailure(Enum):
    """
    Enums to handle special graph problems we might want to flag.
    """

    DISCONNECTED = 1
    """
    The graph is disconnected and the origin and the target lie in different components.
    """

    NEGATIVE_CYCLE = 2
    """
    The graph contains a cycle of negative weight and the path between the origin and
    the target passes through it.
    """


def binary_search(items: list[T], target: T, low: int, high: int) -> int:
    """
    Returns the index of the smallest element greater than or equal to target in items.
    """
    if low > high:
        return low

    mid = (low + high) // 2

    if items[mid] == target:
        return mid
    elif items[mid] > target:
        return binary_search(items, target, low, mid - 1)
    else:
        return binary_search(items, target, mid + 1, high)
