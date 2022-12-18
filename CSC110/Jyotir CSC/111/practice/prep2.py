"""CSC111 Winter 2022 Prep 2: Programming Exercises

Instructions (READ THIS FIRST!)
===============================

This Python module contains the implementation of linked lists we studied in lecture
last week, including the append method and updated initializer from the prep reading.

There are two additional methods at the bottom of the class that we have started.
Your first task is to implement EACH method based on the method header and description.

Your second task is to write a set of tests for each of the methods, as described at the bottom
of this file. This is good review of how to write unit tests in Python from CSC110, which you'll
need to do throughout this course.

We have marked each place you need to write code with the word "TODO".
As you complete your work in this file, delete each TODO comment.

You do not need to add additional doctests. However, you should test your work carefully
before submitting it!

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2022 Mario Badr and David Liu.
"""
from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Iterable, Optional

import pytest  # You'll need to use pytest.raises in your tests (see below)


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

    def __init__(self, items: Iterable) -> None:
        """Initialize a new linked list containing the given items.
        """
        self._first = None
        for item in items:
            self.append(item)

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

    ############################################################################
    # Prep exercises start here
    ############################################################################
    def remove_first(self) -> Any:
        """Remove and return the first element of this list.

        Raise an IndexError if this list is empty.

        >>> lst = LinkedList([1, 2, 3])
        >>> lst.remove_first()
        1
        >>> lst.to_list()
        [2, 3]
        >>> lst.remove_first()
        2
        >>> lst.remove_first()
        3
        """
        lst = []
        if self._first is not None:
            lst.append(self._first.item)
            self._first = self._first.next
        else:
            raise IndexError
        return lst[0]

    def remove_last(self) -> Any:
        """Remove and return the last element of this list.

        Raise an IndexError if this list is empty.

        >>> lst = LinkedList([1, 2, 3])
        >>> lst.remove_last()
        3
        >>> lst.to_list()
        [1, 2]
        >>> lst.remove_last()
        2
        >>> lst.remove_last()
        1

        IMPLEMENTATION HINTS:
            1. You'll need to modify the linked list traversal pattern to reach
               the *second-last node*.
            2. It's okay to have separate cases (using if statements) for size-0
               and size-1 linked lists.
        """
        lst = []
        if self._first is not None:
            if self._first.next is None:
                lst.append(self._first.item)
                self._first = None
            else:
                curr = self._first
                while curr.next.next is not None:
                    curr = curr.next
                lst.append(curr.next.item)
                curr.next = None
        else:
            raise IndexError
        return lst[0]


################################################################################
# Test cases
################################################################################
# Write unit tests for each of the two LinkedList methods you implemented above.
# Your tests should cover various cases for possible linked list lengths, and
# should check both for mutation and the correct return value.
# You can use the LinkedList.to_list method to check the values in the linked list.
# Each unit test should have a docstring containing a brief description of the test.
#
# To review how to write unit tests using pytest (including testing for errors being raised),
# please consult
# https://www.teach.cs.toronto.edu/~csc110y/fall/notes/B-python-libraries/02-pytest.html.
#
# WARNING: your test function names MUST start with "test_", otherwise they won't
# be detected as unit tests by pytest, and therefore won't be run.


def test_remove_first_1() -> None:
    """Test for removing first element when list length is 4"""
    lst = LinkedList(["a"])
    assert lst.remove_first() == "a"


def test_remove_last_1() -> None:
    """Test for removing last element when list length is 4"""
    lst = LinkedList([4])
    assert lst.remove_last() == 4


def test_remove_first_multiple() -> None:
    """Test for removing first element when list length is 5"""
    lst = LinkedList(["b", 2, 3, "a", "c"])
    assert lst.remove_first() == "b"


def test_remove_first_mutate() -> None:
    """Test for removing first element when list length is 5"""
    lst = LinkedList(["b", 2, 3, "a", "c"])
    lst.remove_first()
    assert lst.to_list() == [2, 3, "a", "c"]


def test_remove_last_multiple() -> None:
    """Test for removing last element when list length is 5"""
    lst = LinkedList(["a", 2, "c", "d", 4])
    assert lst.remove_last() == 4


def test_remove_last_mutate() -> None:
    """Test for removing last element when list length is 5"""
    lst = LinkedList(["a", 2, "c", "d", 4])
    lst.remove_last()
    assert lst.to_list() == ["a", 2, "c", "d"]


def test_remove_first_empty() -> None:
    """
    Test remove_first on an empty linked list
    """
    lst = LinkedList([])
    with pytest.raises(IndexError):
        lst.remove_first()


def test_remove_last_empty() -> None:
    """
    Test remove_last on an empty linked list
    """
    lst = LinkedList([])
    with pytest.raises(IndexError):
        lst.remove_last()


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={
        'max-line-length': 100,
        'disable': ['E1136']
    })

    import python_ta.contracts
    python_ta.contracts.check_all_contracts()

    import doctest
    doctest.testmod()

    pytest.main(['prep2.py', '-v'])
