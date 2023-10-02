"""
There is an Entry type defined in m_entry.py which *must* be used in your
map interface. The Entry is a very simple class that stores keys and values.
The special reason we make you use Entry types is because Entry extends the
Hashable class in m_util.py - by extending Hashable, you must implement
and use the `get_hash()` method inside Entry if you wish to use hashing to
implement your map. We *will* be assuming Entry types are used in your Map
implementation. Sorry for any inconvenience this causes (hopefully none!).
Note that if you opt to not use hashing, then you can simply override the
get_hash function to return -1 for example.
"""

from typing import Callable, Generic, Optional, TypeVar

from structures.m_entry import Entry
from structures.m_single_linked_list import SingleLinkedList
from structures.m_util import Hashable

Key = TypeVar("Key", Hashable)
Value = TypeVar("Value")

NUM_BUCKETS: int = 10
"""Number of buckets in the underlying hash table."""


class Map(Generic[Key, Value]):
    """
    An implementation of the Map ADT.
    The provided methods consume keys and values via the Entry type.
    """

    def __init__(self) -> None:
        """
        Construct the map.
        You are free to make any changes you find suitable in this function
        to initialise your map.
        """
        self.buckets: list[Optional[SingleLinkedList[Entry[Key, Value]]]] = [
            None
        ] * NUM_BUCKETS
        self.compression_function: Callable[[int], int] = lambda x: x % NUM_BUCKETS

    def insert(self, entry: Entry[Key, Value]) -> Optional[Value]:
        """
        Associate value v with key k for efficient lookups. You may wish
        to return the old value if k is already inside the map after updating
        to the new value v.
        """
        bucket = self.compression_function(entry.get_hash())

        if self.buckets[bucket] is None:
            self.buckets[bucket] = SingleLinkedList()

        cur = self.buckets[bucket].get_head()
        while cur is not None:
            if cur.get_value().get_key() == entry.get_key():
                old_value = cur.get_value().get_value()
                cur.set_value(entry)
                return old_value
            cur = cur.get_next()

        self.buckets[bucket].insert_at_head(entry)

    def insert_kv(self, key: Key, value: Value) -> Optional[Value]:
        """
        A version of insert which wraps a given key/value in an Entry type.
        Handy if you wish to provide keys and values directly to the insert
        function. It will return the value returned by insert, so keep this
        in mind.
        """
        entry = Entry(key, value)
        return self.insert(entry)

    def __setitem__(self, key: Key, value: Value) -> None:
        """
        For convenience, you may wish to use this as an alternative
        for insert as well. However, this version does _not_ return
        anything. Can be used like: my_map[some_key] = some_value
        """
        entry = Entry(key, value)
        self.insert(entry)

    def remove(self, key: Key) -> None:
        """
        Remove the key/value pair corresponding to key k from the
        data structure. Don't return anything.
        """
        if (value := self.find(key)) is None:
            return

        bucket = self.compression_function(key.get_hash())
        self.buckets[bucket].find_and_remove_element(Entry(key, value))

    def find(self, key: Key) -> Optional[Value]:
        """
        Find and return the value v corresponding to key k if it
        exists; return None otherwise.
        """
        bucket = self.compression_function(key.get_hash())

        if self.buckets[bucket] is None:
            return

        cur = self.buckets[bucket].get_head()
        while cur is not None:
            if cur.get_value().get_key() == key:
                return cur.get_data().get_value()
            cur = cur.get_next()

    def __getitem__(self, key: Key) -> Optional[Value]:
        """
        For convenience, you may wish to use this as an alternative
        for find()
        """
        return self.find(key)

    def get_size(self) -> int:
        # IMPLEMENT ME!
        pass

    def is_empty(self) -> bool:
        for i in range(NUM_BUCKETS):
            bucket = self.buckets[i]
            if bucket is not None and bucket.get_size() != 0:
                return False
