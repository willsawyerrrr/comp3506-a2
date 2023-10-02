from typing import Generic, Optional, TypeVar

from structures.m_extensible_list import ExtensibleList

Datum = TypeVar("Datum")


class Stack(Generic[Datum]):
    """
    A simple composition-based stack backed by an ExtensibleList.
    """

    def __init__(self) -> None:
        self._data = ExtensibleList()

    def push(self, elem: Datum) -> None:
        """
        Push some data `elem` onto the stack.
        """
        self._data.append(elem)

    def pop(self) -> Optional[Datum]:
        """
        Remove and return the top element or None if empty.
        """
        if self._data.is_empty():
            return None
        index = self._data.get_size() - 1
        value = self._data.remove_at(index)
        return value

    def peek(self) -> Optional[Datum]:
        """
        Return the top element but do not remove it.
        """
        index = self._data.get_size() - 1
        # get_at handles indexes being out of bounds
        return self._data.get_at(index)

    def is_empty(self) -> bool:
        return self._data.is_empty()

    def get_size(self) -> int:
        return self._data.get_size()
