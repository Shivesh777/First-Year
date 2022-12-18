"""CSC111 W01 - Starter file

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

import math


@dataclass
class _Node:
    """A node in a linked list.

    Note that this is considered a "private class", one which is only meant
    to be used in this module by the LinkedList class, but not by client code.

    Instance Attributes:
      - item: The data stored in this node.
      - next: The next node in the list, if any.
    """
    item: Any
    next: Optional[_Node] = None  # By default, this node does not link to any other node


class LinkedList:
    """A linked list implementation of the List ADT."""
    # Private Instance Attributes:
    #   - _first: The first node in this linked list, or None if this list is empty.
    _first: Optional[_Node]

    ################################################################################################
    # From the Notes - 11.1
    ################################################################################################
    def __init__(self) -> None:
        """Initialize an empty linked list."""
        self._first = None

    ################################################################################################
    # From the Notes - 11.2
    ################################################################################################
    def print_items(self) -> None:
        """Print out each item in this linked list."""
        curr = self._first
        while curr is not None:
            print(curr.item)
            curr = curr.next

    def to_list(self) -> list:
        """Return a built-in Python list containing the items of this linked list.

        The items in this linked list appear in the same order in the returned list.
        """
        curr = self._first
        lst_so_far = []
        while curr is not None:
            lst_so_far.append(curr.item)
            curr = curr.next
        return lst_so_far

    ################################################################################################
    # Demo
    ################################################################################################
    def sum(self) -> int:
        """Return the sum of the elements in this linked list.

        Preconditions:
            - all elements in this linked list are integers
        """

    ################################################################################################
    # Exercise 2
    ################################################################################################
    def maximum(self) -> float:
        """Return the maximum element in this linked list.

        Preconditions:
            - every element in this linked list is a float
            - this linked list is not empty

        >>> linky = LinkedList()
        >>> node3 = _Node(30.0)
        >>> node2 = _Node(-20.5, node3)
        >>> node1 = _Node(10.1, node2)
        >>> linky._first = node1
        >>> linky.maximum()
        30.0
        """
        import math
        lst = self.to_list()
        return max(lst)

        # Implementation note: as usual for compute maximums,
        # import the math module and initialize your accumulator
        # to -math.inf (negative infinity).

    def __contains__(self, item: Any) -> bool:
        """Return whether item is in this linked list.

        >>> linky = LinkedList()
        >>> linky.__contains__(10)
        False
        >>> node2 = _Node(20)
        >>> node1 = _Node(10, node2)
        >>> linky._first = node1
        >>> linky.__contains__(20)
        True
        """


    def __getitem__(self, i: int) -> Any:
        """Return the item stored at index i in this linked list.

        Raise an IndexError if index i is out of bounds.

        Preconditions:
            - i >= 0
        """


################################################################################################
# Exercise 1
################################################################################################
node1 = _Node('a')
node2 = _Node('b')
node3 = _Node('c')
linky = LinkedList()  # linky is empty

################################################################################################
# Exercise 1, Question 1
################################################################################################
node1.next = node2
node2.next = node3
linky._first = node1
################################################################################################
# Exercise 1, Question 2
# Run this file in Python console, then type out each line to see the output.
################################################################################################
