from __future__ import annotations

from typing import Any


class SingleNode:
    """
    A simple type to hold data and a next pointer
    """

    def __init__(self, data: Any) -> None:
        self._data = data  # This is the payload data of the node
        self._next = None  # This is the "next" pointer to the next SingleNode

    def set_data(self, data: Any) -> None:
        self._data = data

    def get_data(self) -> Any:
        return self._data

    def set_next(self, node: SingleNode) -> None:
        self._next = node

    def get_next(self) -> SingleNode | None:
        return self._next


class SingleLinkedList:

    """
    HIDDEN UNTIL ALL A1 SUBMISSIONS COME IN
    """

    def __init__(self) -> None:
        self._head = None
        self._size = 0
