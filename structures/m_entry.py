from typing import Generic, TypeVar

from structures.m_util import Hashable

Key = TypeVar("Key")
Value = TypeVar("Value")


class Entry(Hashable, Generic[Key, Value]):
    """
    Implements a simple type that holds keys and values. Extends the Hashable type to
    ensure get_hash() is available/used for arbitrary key types.
    """

    def __init__(self, key: Key, value: Value) -> None:
        """
        An entry has a key (used for comparing to other entries or for hashing) and a
        corresponding value which represents some arbitrary data associated with the
        key.
        """
        self._key = key
        self._value = value

    def get_key(self) -> Key:
        return self._key

    def get_value(self) -> Value:
        return self._value

    def update_key(self, nk: Key) -> None:
        self._key = nk

    def update_value(self, nv: Value) -> None:
        self._value = nv

    def __eq__(self, other) -> bool:
        """
        Compares two Entry objects by their keys; returns True if keys are equal, False
        otherwise. Relies on keys having __eq__ implemented.
        """
        return self.get_key() == other.get_key()

    def __lt__(self, other) -> bool:
        """
        Compares two Entry objects by their keys; returns True if self is less than
        other. Relies on keys having __lt__ implemented.
        """
        return self.get_key() < other.get_key()

    def get_hash(self) -> int:
        """
        Returns a hash of self._key - this hash function MUST be implemented if you need
        to hash Entry types. In other words, do not use Python's magic __hash__()
        function, but rather, you need to make your own. You are welcome to use existing
        functions, but you need to implement it here (and cite it in your
        report/statement file).
        """
        # TODO: Implement this
        return 7

    def __str__(self) -> str:
        return f"({self._key} -> {self._value})"


class Destination(Entry[Key, Value]):
    """
    A special type of entry that tracks the monetary and stopover costs of a trip from
    some origin to a destination. You can use _value however you like, or ignore it
    completely.
    """

    def __init__(
        self, key: Key, value: Value, cost_money: int, cost_stopover: int
    ) -> None:
        super().__init__(key, value)
        self._cost_m = cost_money
        self._cost_s = cost_stopover

    def get_cost_money(self) -> int:
        return self._cost_m

    def get_cost_stopover(self) -> int:
        return self._cost_s

    def update_cost_money(self, ncm: int) -> None:
        self._cost_m = ncm

    def update_cost_stopover(self, ncs: int) -> None:
        self._cost_s = ncs

    # You may add helpers/additional functionality below if you wish, and
    # you may override inherited methods here if you wish
