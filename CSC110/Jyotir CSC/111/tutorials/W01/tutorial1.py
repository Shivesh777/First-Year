"""CSC111 Tutorial 1: Linked Lists

Module Description
==================
This module contains the code for a linked list implementation with two classes,
LinkedList and _Node. It contains code from the course notes/lecture,
and additional exercises for this week's tutorial.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2022 Mario Badr, David Liu.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Optional


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
    """A linked list implementation of the List ADT.
    """
    # Private Instance Attributes:
    #   - _first: The first node in this linked list, or None if this list is empty.
    _first: Optional[_Node]

    def __init__(self) -> None:
        """Initialize an empty linked list.
        """
        self._first = None

    def print_items(self) -> None:
        """Print out each item in this linked list."""
        curr = self._first
        while curr is not None:
            print(curr.item)  # Note: this is the only line we needed to fill in!
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
        # VERSION 1: using an early return.
        curr = self._first
        curr_index = 0

        while curr is not None:
            if curr_index == i:
                return curr.item

            curr = curr.next
            curr_index = curr_index + 1

        # If we've reached the end of the list and no item has been returned,
        # the given index is out of bounds.
        raise IndexError

        # VERSION 2: using a compound loop condition.
        # curr = self._first
        # curr_index = 0
        #
        # while not (curr is None or curr_index == i):
        #     curr = curr.next
        #     curr_index = curr_index + 1
        #
        # assert curr is None or curr_index == i
        # if curr is None:
        #     # index is out of bounds
        #     raise IndexError
        # else:
        #     # curr_index == i, so curr is the node at index i
        #     return curr.item

    def __contains__(self, item: Any) -> bool:
        """Return whether <item> is in this list.

        Use == to compare items.
        """
        curr = self._first
        while curr is not None:
            if curr.item == item:
                return True
            curr = curr.next
        return False

    ############################################################################
    # Tutorial Part 1: Traversing linked lists
    ############################################################################
    def __len__(self) -> int:
        """Return the number of elements in this list.

        >>> lst = LinkedList()
        >>> lst.__len__()
        0
        >>> lst2 = build_sample_linked_list()
        >>> lst2.__len__()
        4
        """
        length = 0
        curr = self._first
        while curr is not None:
            length += 1
            curr = curr.next
        return length

    def count(self, item: Any) -> int:
        """Return the number of times the given item occurs in this list.

        Use == to compare items.

        >>> lst = LinkedList()
        >>> lst.count(111)
        0
        >>> lst2 = build_sample_linked_list()
        >>> lst2.count(111)
        2
        """
        length = 0
        curr = self._first
        while curr is not None:
            if curr.item == item:
                length += 1
            curr = curr.next
        return length


    def index(self, item: Any) -> int:
        """Return the index of the first occurrence of the given item in this list.

        Raise ValueError if the given item is not present.

        Use == to compare items.

        >>> lst = LinkedList()
        >>> lst.index(111)
        Traceback (most recent call last):
        ValueError
        >>> lst2 = build_sample_linked_list()
        >>> lst2.index(111)
        0
        >>> lst2.index(9000)
        2
        """
        index = -1
        curr = self._first
        curr_index = 0
        while curr is not None:
            if curr.item == item:
                index = curr_index
                break
            curr = curr.next
            curr_index += 1
        if index == -1:
            raise ValueError
        return index

    def __setitem__(self, i: int, item: Any) -> None:
        """Store item at index i in this list.

        Raise IndexError if i >= len(self).

        Preconditions:
            - i >= 0

        >>> lst = LinkedList()
        >>> lst.__setitem__(0, 'hello')
        Traceback (most recent call last):
        IndexError
        >>> lst2 = build_sample_linked_list()
        >>> lst2.__setitem__(0, 'hello')
        >>> lst2.to_list()
        ['hello', -5, 9000, 111]
        >>> lst2.__setitem__(2, 10000)
        >>> lst2.to_list()
        ['hello', -5, 10000, 111]
        """
        curr = self._first
        curr_index = 0
        while curr is not None:
            if curr_index == i:
                curr.item = item
            curr = curr.next
            curr_index += 1
        if i >= len(self):
            raise IndexError

    ############################################################################
    # Part 3: How Python does iteration
    ############################################################################
    def __iter__(self) -> LinkedListIterator:
        """Return an iterator for this linked list.
        It should be straightforward to initialize the iterator here
        (see the LinkedListIterator class below). Just remember to initialize
        it using the first node in this linked list.
        """
        return LinkedListIterator(self._first)


class LinkedListIterator:
    """An object responsible for iterating through a linked list.

    This enables linked lists to be used inside for loops!

    >>> lst = build_sample_linked_list()
    >>> for x in lst:
    ...     print(x)
    ...
    111
    -5
    9000
    111
    """
    # Private Instance Attributes:
    #   - _curr: The current node for this iterator. This should start as the first node
    #            in the linked list, and update to the next node every time __next__
    #            is called.
    _curr: Optional[_Node]

    def __init__(self, first_node: Optional[_Node]) -> None:
        """Initialize a new linked list iterator with the given node."""
        self._curr = first_node

    def __next__(self) -> Any:
        """Return the next item in the iteration.

        Raise StopIteration if there are no more items to return.

        Hint: You already have an attribute keeping track of where this iterator
        is currently at in the list. Use this attribute to return the current item,
        and update the attribute to be the next node in the list.

        >>> lst = build_sample_linked_list()
        >>> iterator = lst.__iter__()
        >>> iterator.__next__()
        111
        >>> iterator.__next__()
        -5
        >>> iterator.__next__()
        9000
        >>> iterator.__next__()
        111
        >>> iterator.__next__()
        Traceback (most recent call last):
        StopIteration
        """
        curr = self._curr
        if curr is not None:
            self._curr = curr.next
            return curr.item
        else:
            raise StopIteration


def build_sample_linked_list() -> LinkedList:
    """Build an example linked list with values 111, -5, 999, 111.

    Useful in Tutorial 1 to create tests for LinkedList methods, before introducing a
    more general LinkedList initializer (which will happen in Week 2).
    """
    linky = LinkedList()
    node1 = _Node(111)
    linky._first = node1

    node2 = _Node(-5)
    node1.next = node2

    node3 = _Node(9000)
    node2.next = node3

    node4 = _Node(111)
    node3.next = node4

    return linky


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={
        'max-line-length': 100,
        'allowed-io': ['print_items'],
        'disable': ['E1136']
    })

    import python_ta.contracts
    python_ta.contracts.check_all_contracts()

    import doctest
    doctest.testmod()
