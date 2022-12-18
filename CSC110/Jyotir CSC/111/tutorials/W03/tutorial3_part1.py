"""CSC111 Tutorial 3: Induction and Recursion

Module Description
==================
This module contains the specifications for various recursive functions on nested lists.
Your task in this part of the tutorial is to implement all of these functions.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2022 Mario Badr, David Liu and Diane Horton.
"""
from typing import Optional, Union


# For your reference, this is the "sum_nested" function from lecture.
def sum_nested(nested_list: Union[int, list]) -> int:
    """Return the sum of the given nested list.
    """
    if isinstance(nested_list, int):
        return nested_list
    else:
        # Version 1: using a loop
        sum_so_far = 0
        for sublist in nested_list:
            sum_so_far += sum_nested(sublist)
        return sum_so_far

        # Version 2: using a comprehension and the built-in sum function
        # return sum(sum_nested(sublist) for sublist in nested_list)


def all_less_than(nested_list: Union[int, list], n: int) -> bool:
    """Return whether every integer in nested_list is less than n.

    >>> all_less_than(10, 3)
    False
    >>> all_less_than([1, 2, [1, 2], 4], 10)
    True
    >>> all_less_than([], 0)
    True
    """
    if isinstance(nested_list, int):
        return nested_list < n
    else:
        # Version 1: using a loop
        lst = []
        for sublist in nested_list:
            lst.append(all_less_than(sublist, n))
        return all(lst)


def add_n(nested_list: Union[int, list], n: int) -> Union[int, list]:
    """Return a new nested list where n is added to every item in nested_list.

    >>> add_n(10, 3)
    13
    >>> add_n([1, 2, [1, 2], 4], 10)
    [11, 12, [11, 12], 14]
    """
    if isinstance(nested_list, int):
        return nested_list + n
    else:
        # Version 1: using a loop
        lst = []
        for sublist in nested_list:
            lst.append(add_n(sublist, n))
        return lst


def first_at_depth(nested_list: Union[int, list], d: int) -> Optional[int]:
    """Return the first (leftmost) integer in nested_list at depth d.

    Return None if there is no integer at depth d in nested_list

    Hint: review items_at_depth from Wednesday's class!

    Preconditions:
        - d >= 0

    >>> first_at_depth(100, 0)
    100
    >>> first_at_depth(100, 3) is None
    True
    >>> first_at_depth([10, [[20]], [30, 40]], 2)
    30
    >>> first_at_depth([10, [[20]], [30, 40]], 3)
    20
    >>> first_at_depth([10, [[20]], [30, 40]], 4) is None
    True
    """
    if isinstance(nested_list, int) and d == 0:
        return nested_list
    elif isinstance(nested_list, int) or d == 0:
        return None
    else:
        for sublist in nested_list:
            rect_value = first_at_depth(sublist, d - 1)

            if rect_value is not None:
                return rect_value

        return None


if __name__ == '__main__':
    import python_ta.contracts
    python_ta.contracts.check_all_contracts()

    import doctest
    doctest.testmod()

    import python_ta
    python_ta.check_all(config={
        'max-line-length': 100,
        'disable': ['E1136']
    })
