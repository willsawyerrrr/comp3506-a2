from typing import Generic, TypeVar

from structures.m_entry import Entry
from structures.m_extensible_list import ExtensibleList
from structures.m_util import binary_search

Datum = TypeVar("Datum")


class PriorityQueue(Generic[Datum]):
    """
    An implementation of the PriorityQueue ADT. The provided methods consume keys and
    values. Keys are called "priorities" and should be integers in the range [0, n] with
    0 being the highest priority. Values are called "data" and store the payload data of
    interest. For convenience, you may wish to also implement the functionality provided
    in terms of the Entry type, but this is up to you.
    """

    def __init__(self):
        """
        Construct the priority queue.
        """
        self._entries: ExtensibleList[Entry[int, Datum]] = ExtensibleList()
        self._fifo_priority = 0

    def insert(self, priority: int, data: Datum) -> None:
        """
        Insert some data to the queue with a given priority.
        """
        index = binary_search(
            self._entries, Entry(priority, data), 0, self._entries.get_size() - 1
        )
        self._entries.insert_at(index, Entry(priority, data))

    def insert_fifo(self, data: Datum) -> None:
        """
        Allows a user to add data for FIFO queue operations.
        """
        self._entries.append(Entry(self._fifo_priority, data))
        self._fifo_priority += 1

    def get_min(self) -> Datum:
        """
        Return the highest priority value from the queue, but do not remove it.
        """
        return self._entries.get_at(0).get_value()

    def remove_min(self) -> Datum:
        """
        Remove and return the highest priority value from the queue.
        """
        return self._entries.remove_at(0).get_value()

    def get_size(self) -> int:
        return self._entries.get_size()

    def is_empty(self) -> bool:
        return self._entries.is_empty()
