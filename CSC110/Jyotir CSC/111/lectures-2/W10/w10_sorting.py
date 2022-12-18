"""CSC111 W10 - Starter File (Recursive Sorting)

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.
"""
from typing import Any


###################################################################################################
# Demo
###################################################################################################
def quicksort(lst: list) -> list:
    """Return a sorted list with the same elements as lst.

    This is a *non-mutating* version of quicksort; it does not mutate the
    input list.

    >>> quicksort([10, 2, 5, -6, 17, 10])
    [-6, 2, 5, 10, 10, 17]
    """
    if len(lst) < 2:
        return lst.copy()
    else:
        # 1. Divide the list into two parts
        pivot = lst[0]
        smaller, bigger = _partition(lst[1:], pivot)
        # 2. Sort each part recursively
        smaller_sorted = quicksort(smaller)
        bigger_sorted = quicksort(bigger)

        # 3. Combine the sorted parts
        return smaller_sorted + pivot + bigger_sorted


def _partition(lst: list, pivot: Any) -> tuple[list, list]:
    """Return a partition of lst with the chosen pivot.

    Return two lists, where the first contains the items in lst
    that are <= pivot, and the second contains the items in lst that are > pivot.
    """
    lst1 = []
    lst2 = []
    for x in lst:
        if x <= pivot:
            lst2.append(x)
        else:
            lst1.append(x)
    return lst2, lst1


###################################################################################################
# Exercise 1 - Question 2
###################################################################################################
def _in_place_partition(lst: list, b: int, e: int) -> Any:
    """Mutate lst so that it is partitioned with pivot lst[0].

    Let pivot = lst[0]. The elements of lst are moved around so that lst looks like

        [x1, x2, ... x_m, pivot, y1, y2, ... y_n],

    where each of the x's is <= pivot, and each of the y's is > pivot.

    >>> example_list = [10, 3, 20, 5, 16, 30, 7, 100]
    >>> _in_place_partition(example_list)  # pivot is 10
    >>> example_list[3]  # the 10 is now at index 3
    10
    >>> set(example_list[:3]) == {3, 5, 7}
    True
    >>> set(example_list[4:]) == {16, 20, 30, 100}
    True
    """
    pivot = lst[b]
    smalli = b + 1
    bigi = e
    while smalli != bigi:
        if lst[smalli] > pivot:
            bigi -= 1
            lst[smalli], lst[bigi] = lst[bigi], lst[smalli]
        else:
            smalli += 1
    lst[b], lst[smalli - 1] = lst[smalli - 1], lst[b]
    return smalli - 1


################################################################################
# Exercise 1 - Question 3
################################################################################
# def in_place_quicksort(lst: list,  b: int, e: int) -> None:
#     """Sort the given list using the quicksort algorithm."""
#     if len(lst) < 2:
#         return
#     else:
#         pivot = _in_place_partition(lst, 0, len(lst))
#         in_place_quicksort(lst[:pivot])
#         in_place_quicksort(lst[pivot + 1:])


def in_place_quicksort_sub(lst: list,  b: int, e: int) -> None:
    """Sort the given list using the quicksort algorithm."""
    if e - b < 2:
        pass
    else:
        pivot = _in_place_partition(lst, b, e)
        in_place_quicksort_sub(lst, b, pivot)
        in_place_quicksort_sub(lst, pivot + 1, e)

