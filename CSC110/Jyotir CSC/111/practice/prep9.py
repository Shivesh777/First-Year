"""CSC111 Winter 2022 Prep 9: Programming Exercises

Instructions (READ THIS FIRST!)
===============================

This module contains some functions related to sorting and/or Python lists for practice.
In particular, some of these functions give you practice with *index parameters*,
which we commonly use to specify that a function should only operate on a part of a list.
(This is generally more efficient than requiring the user to create a new list. We'll explor
this idea further in lecture this week.)

Do NOT use recursion for any of these functions.

We have marked each place you need to write code with the word "TODO".
As you complete your work in this file, delete each TODO comment.

You may add additional doctests, but they will not be graded. You should test your work
carefully before submitting it!

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2022 Mario Badr and David Liu.
"""


def is_sorted(lst: list) -> bool:
    """Return whether lst is sorted.

    Formally, a list `lst` is sorted when for every index i between 0 and len(lst),
    lst[i] <= lst[i + 1]. Note that empty lists and lists of length 1 are always sorted.

    Do not call `sorted` or `list.sort`, or otherwise sort `lst` in this function.

    >>> is_sorted([2, 7, 3, 4, 5])
    False
    """

    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))


def is_sorted_sublist(lst: list, b: int, e: int) -> bool:
    """Return whether the sublist lst[b:e] is sorted.

    Do not create a new list or call is_sorted. Instead, adapt the definition from
    is_sorted to complete this function.

    Note that if b >= e, then lst[b:e] is an empty list, and so is sorted.

    Preconditions:
        - 0 <= b < len(lst)
        - 0 <= e <= len(lst)

    >>> is_sorted_sublist([2, 7, 3, 4, 5], 0, 5)  # Equivalent to is_sorted([2, 7, 3, 4, 5])
    False
    >>> is_sorted_sublist([2, 7, 3, 4, 5], 2, 5)  # Equivalent to is_sorted([2, 7, 3, 4, 5][2:5])
    True
    """

    return all(lst[i] <= lst[i + 1] for i in range(b, e - 1))


def min_index(lst: list) -> int:
    """Return the index of the smallest element of lst.

    In the case of ties, return the smaller index (i.e., the index that appears first).

    Preconditions:
        - lst != []

    >>> min_index([-10, 7, 3, 5])
    0
    """

    min_so_far = 0
    for i in range(1, len(lst)):
        if lst[i] < lst[min_so_far]:
            min_so_far = i
    return min_so_far


def min_index_sublist(lst: list, b: int, e: int) -> int:
    """Return the index of the smallest item in lst[b:e].

    In the case of ties, return the smaller index (i.e., the index that appears first).

    This is similar to min_index, except we are only considering the elements
    with indexes between b and e - 1, inclusive.

    Preconditions:
        - 0 <= b < e <= len(lst)

    >>> min_index_sublist([-10, 7, 3, 5], 0, 4)
    0
    >>> min_index_sublist([-10, 7, 3, 5], 1, 3)
    2
    """
    min_so_far = b
    for i in range(b + 1, e):
        if lst[i] < lst[min_so_far]:
            min_so_far = i
    return min_so_far


def cycle(lst: list) -> None:
    """Rearrange the elements of lst by shifting every element one spot to the right.

    The last list element moves to the front of the list.

    Preconditions:
        - lst != []

    >>> lst = [10, 3, 5, 7, 9000]
    >>> cycle(lst)
    >>> lst
    [9000, 10, 3, 5, 7]

    Implementation notes:
        - Do NOT call any list methods; instead, move the elements by assigning to indexes
          (e.g., lst[1] = list[0] or lst[i] = lst[i + 1]).
    """
    last_elem = lst[-1]
    for i in range(len(lst) - 1, 0, -1):
        lst[i] = lst[i - 1]
    lst[0] = last_elem


def cycle_sublist(lst: list, b: int, e: int) -> None:
    """Rearrange the elements of lst[b:e] by shifting every element one spot to the right.

    The element lst[e - 1] moves to index b.

    Preconditions:
        - 0 <= b < e <= len(lst)

    >>> lst = [10, 3, 5, 7, 9000]
    >>> cycle_sublist(lst, 0, 5)  # Equivalent to cycle(lst)
    >>> lst
    [9000, 10, 3, 5, 7]
    >>> lst2 = [10, 3, 5, 7, 9000]
    >>> cycle_sublist(lst2, 1, 4)
    >>> lst2
    [10, 7, 3, 5, 9000]
    """
    last_elem = lst[e - 1]
    for i in range(e - 1, b, -1):
        lst[i] = lst[i - 1]
    lst[b] = last_elem


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
