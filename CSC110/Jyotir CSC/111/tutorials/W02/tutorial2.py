"""CSC111 Tutorial 2: More with Linked Lists

Module Description
==================
This module contains the code for a linked list implementation with two classes,
LinkedList and _Node. It contains code from this week's lecture and additional
code for this week's tutorial.

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
from typing import Any, Iterable, Optional


@dataclass
class _Node:
    """A node in a linked list.

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

    def __init__(self, items: Iterable) -> None:
        """Initialize a new linked list containing the given items.
        """
        self._first = None
        curr = None
        for item in items:
            new_node = _Node(item)
            if self._first is None:
                self._first = new_node
                curr = self._first
            else:
                curr.next = new_node
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

    def __len__(self) -> int:
        """Return the number of elements in this list.
        """
        curr = self._first
        len_so_far = 0

        while curr is not None:
            curr = curr.next
            len_so_far += 1
        return len_so_far

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
        # Create the new node to add (this occurs in all cases)
        new_node = _Node(item)

        if i == 0:
            self._first, new_node.next = new_node, self._first
        else:
            # Need to mutate the (i-1)-th node to add new_node
            curr = self._first
            curr_index = 0

            # (Using an "early return" approach)
            while curr is not None:
                if curr_index == i - 1:
                    curr.next, new_node.next = new_node, curr.next
                    return

                curr = curr.next
                curr_index = curr_index + 1

            raise IndexError

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
        """
        if i == 0:
            if self._first is None:
                raise IndexError
            else:
                item = self._first.item
                self._first = self._first.next
                return item
        else:
            curr = self._first
            curr_index = 0

            while not (curr is None or curr_index == i - 1):
                curr = curr.next
                curr_index = curr_index + 1

            if curr is None:
                raise IndexError
            else:
                if curr.next is None:
                    raise IndexError
                else:
                    item = curr.next.item
                    curr.next = curr.next.next
                    return item

    def remove(self, item: Any) -> None:
        """Remove the first occurrence of item from the list.

        Raise ValueError if the item is not found in the list.

        >>> lst = LinkedList([10, 20, 30, 20])
        >>> lst.remove(20)
        >>> lst.to_list()
        [10, 30, 20]
        """
        prev, curr = None, self._first

        while not (curr is None or curr.item == item):
            prev, curr = curr, curr.next

        if curr is None:
            raise ValueError
        else:
            if prev is None:
                self._first = curr.next
            else:
                prev.next = curr.next

    ############################################################################
    # Tutorial Part 1: Linked list mutation practice
    ############################################################################
    def insert_after(self, item: Any, other_item: Any) -> None:
        """Insert other_item after the first occurrence of item in this linked list.

        Raise ValueError if item does not appear in this linked list.

        >>> linky = LinkedList([10, 20, 30, 40])
        >>> linky.insert_after(20, 999)
        >>> linky.to_list()s
        [10, 20, 999, 30, 40]
        """
        new_node = _Node(other_item)
        curr = self._first
        index = -1
        i = 0
        while curr is not None:
            if curr.item == item:
                index = i + 1
            i += 1
            curr = curr.next
        if index == 0:
            self._first, new_node.next = new_node, self._first
        else:
            curr = self._first
            curr_index = 0
            while curr is not None:
                if curr_index == index - 1:
                    curr.next, new_node.next = new_node, curr.next
                    return

                curr = curr.next
                curr_index = curr_index + 1

        if index == -1:
            raise ValueError

    def insert_before(self, item: Any, other_item: Any) -> None:
        """Insert other_item before the first occurrence of item in this linked list.

        Raise ValueError if item does not appear in this linked list.

        >>> linky = LinkedList([10, 20, 30, 40])
        >>> linky.insert_before(20, 999)
        >>> linky.to_list()
        [10, 999, 20, 30, 40]
        >>> linky.insert_before(10, -111)
        >>> linky.to_list()
        [-111, 10, 999, 20, 30, 40]
        """
        new_node = _Node(other_item)
        curr = self._first
        index = -1
        i = 0
        while curr is not None:
            if curr.item == item:
                index = i
            i += 1
            curr = curr.next
        if index == 0:
            self._first, new_node.next = new_node, self._first
        else:
            curr = self._first
            curr_index = 0
            while curr is not None:
                if curr_index == index - 1:
                    curr.next, new_node.next = new_node, curr.next
                    return

                curr = curr.next
                curr_index = curr_index + 1

        if index == -1:
            raise ValueError


################################################################################
# Part 3: Augmenting linked lists
################################################################################
# Write your new subclass here!
class LinkedListTwo(LinkedList):
    _length: int

    def __init__(self, items: Iterable):
        LinkedList.__init__(self, items)
        self._length = len(list(items))

    def __len__(self):
        return self._length


if __name__ == '__main__':
    import python_ta.contracts
    python_ta.contracts.check_all_contracts()

    import doctest
    doctest.testmod()
