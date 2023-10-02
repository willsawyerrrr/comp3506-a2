from typing import Generic, TypeVar

from structures.m_entry import Destination, Entry
from structures.m_extensible_list import ExtensibleList

Datum = TypeVar("Datum")


class PriorityQueue(Generic[Datum]):
    """
    An implementation of the PriorityQueue ADT.
    The provided methods consume keys and values. Keys are called "priorities"
    and should be integers in the range [0, n] with 0 being the highest priority.
    Values are called "data" and store the payload data of interest.
    For convenience, you may wish to also implement the functionality provided in
    terms of the Entry type, but this is up to you.
    """

    def __init__(self):
        """
        Construct the priority queue.
        """
        self.entries: ExtensibleList[Entry[int, Datum]] = ExtensibleList()
        self.fifo_priority = 0

    def insert(self, priority: int, data: Datum) -> None:
        """
        Insert some data to the queue with a given priority.
        Hint: FIFO queue can just always have the same priority value, no
        need to implement an extra function.
        """
        for i in range(self.entries.get_size()):
            if self.entries[i].priority > priority:
                self.entries.insert_at(i, Entry(priority, data))
                return

        self.entries.append(Entry(priority, data))

    def insert_fifo(self, data: Datum) -> None:
        """
        Allows a user to add data for FIFO queue operations.
        """
        self.entries.append(Entry(self.fifo_priority, data))
        self.fifo_priority += 1

    def get_min(self) -> Datum:
        """
        Return the highest priority value from the queue, but do not remove it
        """
        # IMPLEMENT ME!
        pass

    def remove_min(self) -> Datum:
        """
        Extract (remove) the highest priority value from the queue.
        You must then maintain the queue to ensure priority order.
        """
        # IMPLEMENT ME!
        pass

    def get_size(self) -> int:
        return self.entries.get_size()

    def is_empty(self) -> bool:
        return self.entries.is_empty()
