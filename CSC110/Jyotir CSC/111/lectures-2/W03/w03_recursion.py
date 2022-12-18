"""CSC111 W03 - Starter file

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.
"""
from __future__ import annotations
from typing import Any, Optional, Union


################################################################################################
# From the Notes - 12.2
################################################################################################
def f(n: int) -> int:
    """Return the sum of the numbers between 0 and n, inclusive.

    Preconditions:
        - n >= 0

    >>> f(4)
    10
    """
    if n == 0:
        return 0
    else:
        return f(n - 1) + n


def euclidean_gcd(a: int, b: int) -> int:
    """Return the gcd of a and b.

    Preconditions:
        - a >= 0 and b >= 0
    """
    x = a
    y = b
    while y != 0:
        r = x % y
        x = y
        y = r
    return x


def euclidean_gcd_rec(a: int, b: int) -> int:
    """Return the gcd of a and b (using recursion!).

    Preconditions:
        - a >= 0 and b >= 0
    """
    if b == 0:
        return a
    else:
        return euclidean_gcd_rec(b, a % b)


################################################################################################
# From the Notes - 12.3
################################################################################################
def sum_list(numbers: list[int]) -> int:
    """Return the sum of the numbers in the given list.

    >>> sum_list([1, 2, 3])
    6
    """
    sum_so_far = 0
    for num in numbers:
        sum_so_far += num
    return sum_so_far


def sum_list2(lists_of_numbers: list[list[int]]) -> int:
    """Return the sum of the numbers in the given list of lists.

    >>> sum_list2([[1], [10, 20], [1, 2, 3]])
    37
    """
    sum_so_far = 0
    for numbers in lists_of_numbers:
        for num in numbers:
            sum_so_far += num
    return sum_so_far


def sum_list3(lists_of_lists_of_numbers: list[list[list[int]]]) -> int:
    """Return the sum of the numbers in the given list of lists of lists.

    >>> sum_list3([[[1], [10, 20], [1, 2, 3]], [[2, 3], [4, 5]]])
    51
    """
    sum_so_far = 0
    for lists_of_numbers in lists_of_lists_of_numbers:
        for numbers in lists_of_numbers:
            for num in numbers:
                sum_so_far += num
    return sum_so_far


################################################################################################
# From the Notes - 12.4
################################################################################################
def sum_nested(nested_list: Union[int, list]) -> int:
    """Return the sum of the integers in nested_list.

    nested_list is a nested list of integers (using our definition from lecture).
    """
    if isinstance(nested_list, int):
        return nested_list
    else:
        sum_so_far = 0
        for sublist in nested_list:
            sum_so_far += sum_nested(sublist)
        return sum_so_far

################################################################################################
# Exercise 1
################################################################################################


def flatten(nested_list: Union[int, list]) -> list[int]:
    """Return a (non-nested) list of the integers in nested_list.

    The integers are returned in the left-to-right order they appear in
    nested_list.
    >>> flatten([1, [2, 3], [4, [5]]])
    [1, 2, 3, 4, 5]
    """
    if isinstance(nested_list, int):
        return [nested_list]
    else:
        result_so_far = []
        for sublist in nested_list:
            result_so_far.extend(flatten(sublist))
        return result_so_far

################################################################################################
# Exercise 2
################################################################################################


def nested_list_contains(nested_list: Union[int, list], item: int) -> bool:
    """Return whether the given item appears in nested_list.

    If nested_list is an integer, return whether it is equal to item.
    """

    if isinstance(nested_list, int):
        return nested_list == item

    elif all(isinstance(x, int) for x in nested_list):
        val = False
        for thing in nested_list:
            val = thing == item
            if val is True:
                break
        return val
    else:
        value = False
        for sublist in nested_list:
            value = nested_list_contains(sublist, item)
            if value is True:
                break
        return value


################################################################################################
# Exercise 3
################################################################################################


def items_at_depth(nested_list: Union[int, list], d: int) -> list[int]:
    """Return the list of all integers in nested_list that have depth d.

    Preconditions:
        - d >= 0
    """
    if isinstance(nested_list, int):
        depth = 0
        if depth == d:
            return [nested_list]
        else:
            return []
    else:
        lst = []
        for x in nested_list:
            lst.extend(items_at_depth(x, d - 1))
        return lst

################################################################################################
# From the Notes - 12.5
################################################################################################


class RecursiveList:
    """A recursive implementation of the List ADT.

    Note: this list can't store None values! (Because None is used as a special value
    for its attributes.)

    """
    # Private Instance Attributes:
    #   - _first: The first item in the list, or None if this list is empty.
    #   - _rest: A list containing the items that come after the first one,
    #            or None if this list is empty.
    _first: Optional[Any]
    _rest: Optional[RecursiveList]

    def __init__(self, first: Optional[Any], rest: Optional[RecursiveList]) -> None:
        """Initialize a new recursive list."""
        self._first = first
        self._rest = rest

    def sum(self) -> int:
        """Return the sum of the elements in this list.

        Preconditions:
            - every element in this list is an int

        >>> empty = RecursiveList(None, None)
        >>> empty.sum()
        0
        >>> single = RecursiveList(111, empty)
        >>> single.sum()
        111
        >>> four_items = RecursiveList(1,
        ...                            RecursiveList(2,
        ...                                          RecursiveList(3,
        ...                                                        RecursiveList(4, empty))))
        >>> four_items.sum()
        10
        """
        if self._first is None:  # Base case: this list is empty
            return 0
        else:
            return self._first + self._rest.sum()