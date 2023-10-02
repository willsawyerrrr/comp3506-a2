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

    # Warning: This insert() signature changed as of skeleton 1.1, previously
    # the priority and data arguments were switched
    def insert(self, priority: int, data: Datum) -> None:
        """
        Insert some data to the queue with a given priority.
        Hint: FIFO queue can just always have the same priority value, no
        need to implement an extra function.
        """
        # IMPLEMENT ME!
        pass

    def insert_fifo(self, data: Datum) -> None:
        """
        UPDATE in Skeleton v2.2: Allows a user to add data for FIFO queue
        operations. You may assume a user will NOT mix insert() and
        insert_fifo() - they will either use one all of the time, or the
        other all of the time.
        """
        # IMPLEMENT ME!
        pass

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
