"""CSC111 W02 - Starter file

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
from typing import Any, Iterable, Optional


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
    # From the Notes - 11.3
    ################################################################################################
    def __init__(self, items: Iterable) -> None:
        """Initialize the list with the elements in items."""
        self._first = None
        for item in items:
            self.append(item)

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
        items_so_far = []

        curr = self._first
        while curr is not None:
            items_so_far.append(curr.item)
            curr = curr.next

        return items_so_far

    def __getitem__(self, i: int) -> Any:
        """Return the item stored at index i in this linked list.

        Raise an IndexError if index i is out of bounds.

        Preconditions:
            - i >= 0
        """
        # Version 2
        curr = self._first
        curr_index = 0

        while not (curr is None or curr_index == i):
            curr = curr.next
            curr_index = curr_index + 1

        assert curr is None or curr_index == i
        if curr is None:
            # index is out of bounds
            raise IndexError
        else:
            # curr_index == i, so curr is the node at index i
            return curr.item

    ################################################################################################
    # From the Notes - 11.3
    ################################################################################################
    def append(self, item: Any) -> None:
        """Append item to the end of this list.

        >>> lst = LinkedList([1, 2, 3])
        >>> lst.append(4)
        >>> lst.to_list()
        [1, 2, 3, 4]
        """
        new_node = _Node(item)
        if self._first is None:
            self._first = new_node
        else:
            curr = self._first
            while curr.next is not None:
                curr = curr.next

            # After the loop, curr is the last node in the LinkedList.
            assert curr is not None and curr.next is None
            curr.next = new_node

    ################################################################################################
    # Exercise 1
    ################################################################################################
    def insert(self, i: int, item: Any) -> None:
        """Insert the given item at index i in this list.

        Raise IndexError if i > len(self).
        Note that adding to the end of the list (i == len(self)) is okay.

        Preconditions:
            - i >= 0

        >>> lst = LinkedList([1, 2, 10, 200])
        >>> lst.insert(2, 300)
        >>> lst.to_list()
        [1, 2, 300, 10, 200]
        """
        new_node = _Node(item)
        if i == 0:
            new_node.next, self._first = self._first, new_node
        else:
            curr = self._first
            curr_index = 0
            while not (curr is None or curr_index == i - 1):
                curr = curr.next
                curr_index = curr_index + 1
            if curr is None:
                raise IndexError
            else:
                curr.next, new_node.next = new_node, curr.next

            ################################################################################################

    # Exercise 2
    ################################################################################################
    def pop(self, i: int) -> Any:
        """Remove and return the item at index i.

        Raise IndexError if i >= len(self).

        Preconditions:
            - i >= 0

        >>> lst = LinkedList([1, 2, 10, 200])
        >>> lst.pop(1)
        2
        >>> lst.to_list()
        [1, 10, 200]
        >>> lst.pop(2)
        200
        >>> lst.pop(0)
        1
        >>> lst.to_list()
        [10]
        """
        if i == 0:
            lst = []
            if self._first is not None:
                lst.append(self._first.item)
                self._first = self._first.next
            else:
                raise IndexError
            return lst[0]
        else:
            curr = self._first
            curr_index = 0
            while not (curr is None or curr_index == i - 1):
                curr = curr.next
                curr_index = curr_index + 1
            lst = []
            assert curr is None or curr_index == i - 1
            if curr is not None and curr.next is not None:
                lst.append(curr.next.item)
                curr.next = curr.next.next
            else:
                raise IndexError
            return lst[0]

    ################################################################################################
    # Exercise 3
    ################################################################################################

    def remove(self, item: Any) -> None:
        """Remove the first occurence of item from the list.

        Raise ValueError if the item is not found in the list.

        >>> lst = LinkedList([10, 20, 30, 20])
        >>> lst.remove(20)
        >>> lst.to_list()
        [10, 30, 20]
        """
        curr = self._first
        prev = None
        while not (curr is None or curr.item == item):
            prev, curr = curr, curr.next
        if prev is not None and curr is not None:
            prev.next = curr.next
        else:
            raise ValueError

    def swap(self, i: int, j: int) -> None:
        """Remove the first occurence of item from the list.

        Raise IndexError if the item is not found in the list.

       >>> linky = LinkedList([10, 20, 30, 40, 50])
       >>> linky.swap(0, 3)
       >>> linky.to_list()
       [40, 20, 30, 10, 50]
        """
        curr = self._first
        curr_2 = self._first
        curr_index = 0
        curr_2_index = 0
        while not (curr is None or curr_index == i):
            curr = curr.next
            curr_index += 1
        if curr is None:
            raise IndexError
        else:
            while not (curr_2 is None or curr_2_index == j):
                curr_2 = curr_2.next
                curr_2_index += 1
            if curr_2 is None:
                raise IndexError
            else:
                curr_2.item, curr.item = curr.item, curr_2.item

    def keep_biggest(self, other: LinkedList[int]) -> None:
        """
        >>> lst1 = LinkedList([0, 5, 10, 12, 0])
        >>> lst2 = LinkedList([1, 20, 10, 99])
        >>> lst1.keep_biggest(lst2)
        >>> lst1.to_list()
        [10, 0]
        """
        curr1 = self._first
        curr2 = other._first
        prev = None

        while not(curr2 is None or curr1 is None):
            if curr2.item > curr1.item:
                if prev is None:
                    self._first = curr1.next
                    print(curr1.item)
                    return

                else:
                    prev.next = curr1.next
                    prev = curr1
                print(curr1.item)
                curr1 = curr1.next
                curr2 = curr2.next

            else:
                prev = curr1
                curr1 = curr1.next
                curr2 = curr2.next


