from __future__ import annotations

from typing import Generic, Optional, TypeVar

Datum = TypeVar("Datum")


class ExtensibleList(Generic[Datum]):
    def __init__(self, fixed_size: Optional[int] = None) -> None:
        """
        Construct the list with 4 None elements to begin with.

        @param: fixed_size
            The fixed size of the list. If None, the list is not fixed size.
        """
        if fixed_size:
            self._data = [None] * fixed_size
            self._size = fixed_size
            self._capacity = fixed_size
        else:
            self._data = [None] * 4
            self._size = 0
            self._capacity = 4

    def __str__(self) -> str:
        """
        Print the list as a string
        """
        string_rep = "["

        # Loop over all of the slots
        first = True
        for i in range(self._size):
            if not first:
                string_rep += ", "
            else:
                first = False
            string_rep += str(self._data[i])
        string_rep += "]"
        return string_rep

    def __resize(self) -> None:
        """
        Use a doubling strategy for amortized constant time operations.
        """
        self._capacity *= 2
        new_list = [None] * self._capacity
        # Copy elements
        for i in range(self._size):
            new_list[i] = self._data[i]
        # Update reference
        self._data = new_list

    def reset(self) -> None:
        """
        Kill the list.
        """
        self.__init__()

    def get_at(self, index: int) -> Optional[Datum]:
        """
        Bounds checked access.
        """
        if index >= 0 and index < self._size:
            return self._data[index]
        return None

    def __getitem__(self, index: int) -> Optional[Datum]:
        """
        Alternative for get_at.
        """
        return self.get_at(index)

    def set_at(self, index: int, element: Datum) -> None:
        """
        Allows an item to be overwritten if it is within the current logical "not None"
        part of the list, that is, [0, self._size - 1].
        """
        if index >= 0 and index < self._size:
            self._data[index] = element

    def __setitem__(self, index: int, element: Datum) -> None:
        """
        Alternative for set_at.
        """
        self.set_at(index, element)

    def append(self, element: Datum) -> None:
        """
        Add an element to the end of the list (after the last existing element).
        """
        if self._capacity == self._size:
            self.__resize()
        self._data[self._size] = element
        self._size += 1

    def insert_at(self, index: int, element: Datum) -> None:
        """
        Insert an element at the given index, checking bounds.
        """
        if index < 0 or index > self._size:
            return

        if self._capacity == self._size:
            self.__resize()

        self._size += 1
        for i in range(self._size - 1, index, -1):
            self._data[i] = self._data[i - 1]

        self._data[index] = element

    def remove(self, element: Datum) -> None:
        """
        Find and remove the first instance of element, clean up the list.
        """
        found_idx = -1
        for i in range(self._size):
            # This part is only called if we found a match; it will do the shuffling.
            # Note that to find a match, i>=1, so we can safely access i-1
            if found_idx != -1:
                self._data[i - 1] = self._data[i]
            # This part does the matching; it is only called if we are yet to see
            # a match. Once we find a match, we never enter this block
            if found_idx == -1 and self._data[i] == element:
                found_idx = i

        # Don't forget to clear the last element, and to fix up the size
        if found_idx != -1:
            self._data[self._size - 1] = None
            self._size -= 1

    def remove_at(self, index: int) -> Optional[Datum]:
        """
        Remove and return the element at a given index, checking bounds. Return None if
        bounds are bad.
        """
        elem = None
        # If the index is valid
        if index >= 0 and index < self._size:
            # Get the element
            elem = self._data[index]
            # Now shuffle all items back
            for i in range(index, self._size - 1):
                self._data[i] = self._data[i + 1]
            # Fix the last element
            self._data[self._size - 1] = None
            self._size -= 1
        return elem

    # Boolean helper to tell us if the structure is empty or not
    def is_empty(self) -> bool:
        return self._size == 0

    # Boolean helper to tell us if the structure is full or not
    def is_full(self) -> bool:
        return self._capacity == self._size

    # Return the number of elements in the list
    def get_size(self) -> int:
        return self._size

    # Return the total capacity (the number of slots) of the list
    def get_capacity(self) -> int:
        return self._capacity

    def sort(self) -> None:
        """
        Sort elements inside _data based on < comparisons.
        """
        self.merge_sort(0, self.get_size())

    def merge_sort(self, left: int, right: int):
        """
        Sorts the list between indices left and right.
        """
        if left >= right - 1:
            return

        mid = (left + right) // 2
        self.merge_sort(left, mid)
        self.merge_sort(mid, right)
        self.merge(left, mid, right)

    def merge(self, left: int, mid: int, right: int):
        """
        Given a list which is sorted from indices left to mid and indices mid to right,
        merges into the sorted union from indices left to right.
        """
        left_half = self.copy(left, mid)
        right_half = self.copy(mid, right)
        n_1 = left_half.get_size()
        n_2 = right_half.get_size()

        i, j, k = 0, 0, left

        while i < n_1 and j < n_2:
            if left_half[i] < right_half[j]:
                self[k] = left_half[i]
                i += 1
            else:
                self[k] = right_half[j]
                j += 1
            k += 1

        while i < n_1:
            self[k] = left_half[i]
            i += 1
            k += 1

        while j < n_2:
            self[k] = right_half[j]
            j += 1
            k += 1

    def copy(self, left: int, right: int) -> ExtensibleList[Datum]:
        result = ExtensibleList()
        for i in range(left, right):
            result.append(self[i])
        return result
