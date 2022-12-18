"""CSC111 Tutorial 3: Induction and Recursion

Module Description
==================
This module contains a new *recursive* implementation of the List ADT
called RecursiveList. Study it carefully, and then implement the methods in this class.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2022 Mario Badr, David Liu and Diane Horton.
"""
from __future__ import annotations
from typing import Any, Optional


class RecursiveList:
    """A recursive implementation of the List ADT.

    Representation Invariants:
        - (self._first is None) == (self._rest is None)
    """
    # Private Instance Attributes:
    #   - _first: The first item in the list.
    #   - _rest: A list containing the items that come after the first one.
    _first: Optional[Any]
    _rest: Optional[RecursiveList]

    def __init__(self, first: Optional[Any], rest: Optional[RecursiveList]) -> None:
        """Initialize a new recursive list."""
        self._first = first
        self._rest = rest

    def is_empty(self) -> bool:
        """Return whether this list is empty.

        >>> lst1 = RecursiveList(None, None)
        >>> lst1.is_empty()
        True
        >>> lst2 = RecursiveList(1, RecursiveList(2, RecursiveList(None, None)))
        >>> lst2.is_empty()
        False
        """
        return self._first is None

    def sum(self) -> int:
        """Return the sum of the elements in this list.

        Preconditions:
            - every element in this list is an int

        >>> lst1 = RecursiveList(None, None)
        >>> lst1.sum()
        0
        >>> lst2 = RecursiveList(10, RecursiveList(20, RecursiveList(None, None)))
        >>> lst2.sum()
        30
        """
        if self._first is None:  # Base case: this list is empty
            return 0
        else:
            return self._first + self._rest.sum()

    ############################################################################
    # Part 2: Tutorial exercises start here
    ############################################################################
    def to_list(self) -> list:
        """Return a Python list containing the items stored in this list.

        >>> lst1 = RecursiveList(None, None)
        >>> lst1.to_list()
        []
        >>> lst2 = RecursiveList(10, RecursiveList(20, RecursiveList(None, None)))
        >>> lst2.to_list()
        [10, 20]
        """
        if self.is_empty():
            return []
        else:
            lst = [self._first]
            lst.extend(self._rest.to_list())
            return lst

    def __contains__(self, item: Any) -> bool:
        """Return whether the given item is in this list.

        Use == to compare items.

        >>> lst = RecursiveList(1, RecursiveList(2, RecursiveList(3, RecursiveList(None, None))))
        >>> lst.__contains__(2)  # Or, 2 in lst
        True
        >>> lst.__contains__(4)  # Or, 4 in lst
        False
        """
        if self.is_empty():
            return False
        else:
            if self._first == item:
                return True
            else:
                return self._rest.__contains__(item)

    def index(self, item: Any) -> int:
        """Return the index of the first occurrence of the given item in this list.

        Raise ValueError if the given item is not present.

        Use == to compare items.

        >>> lst = RecursiveList(None, None)
        >>> lst.index(111)
        Traceback (most recent call last):
        ValueError
        >>> lst2 = RecursiveList(9, RecursiveList(4, RecursiveList(7, RecursiveList(None, None))))
        >>> lst2.index(9)
        0
        >>> lst2.index(7)
        2
        """
        if self.is_empty():
            raise ValueError
        else:
            if self._first == item:
                return 0
            else:
                return 1 + self._rest.index(item)

    def insert(self, i: int, item: Any) -> None:
        """Insert the given item in to this list at index i

        Raise an IndexError if i is > the length of the list.
        Note that it is possible to add to the end of the list (when i == len(self)).

        Preconditions:
            - i >= 0
        """
        if self.is_empty():
            if i == 0:
                self._insert_first(item)
            else:
                raise IndexError
        else:
            if i == 0:
                self._insert_first(item)
            else:
                self._rest.insert(i - 1, item)

    def _insert_first(self, item: Any) -> None:
        """Insert item at the front of this list.

        This should work even if this list is empty.
        """
        if self.is_empty():
            self._first = item
        else:
            self._first, self._rest = item, RecursiveList(self._first, self._rest)

    ############################################################################
    # Part 3: Computing subsets
    ############################################################################
    def subsets(self) -> list[set]:
        """Return a set of all subsets of the elements in this list.

        Note: because Python doesn't allow a set to contain other sets,
        the returned value is a list of sets instead.

        Preconditions:
            - this list does not contain any duplicates

        Implementation notes:
            - you can create an empty set with the expression "set()"

        >>> lst = RecursiveList(1, RecursiveList(2, RecursiveList(3, RecursiveList(None, None))))
        >>> subsets = lst.subsets()
        >>> len(subsets)
        8
        """
        if self.is_empty():
            return [set()]
        else:
            subsets = []
            set_1 = {self._first + self._rest.subsets()}


if __name__ == '__main__':
    import python_ta.contracts

    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod()

    # import python_ta
    # python_ta.check_all(config={
    #     'max-line-length': 100,
    #     'disable': ['E1136']
    # })
