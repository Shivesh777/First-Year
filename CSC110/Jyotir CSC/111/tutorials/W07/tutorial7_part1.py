from typing import Callable, Optional


# Version that returns a new list
def selection_sort_simple(lst: list) -> list:
    """Return a sorted version of lst.

    >>> selection_sort_simple([5, 3, 10, 7])
    [3, 5, 7, 10]
    """
    sorted_so_far = []

    while lst != []:
        smallest = min(lst)
        lst.remove(smallest)
        sorted_so_far.append(smallest)

    return sorted_so_far


################################################################################################
# Demo
################################################################################################
def selection_sort(lst: list) -> None:
    """Sort the given list using the selection sort algorithm.

    Note that this is a *mutating* function.

    >>> lst = [3, 7, 2, 5]
    >>> selection_sort(lst)
    >>> lst
    [2, 3, 5, 7]
    """
    for i in range(0, len(lst)):
        # Loop invariants
        #   - lst[:i] is sorted
        #   - if i > 0, lst[i - 1] is less than or equal to all items in lst[i:len(lst)]
        ...


################################################################################################
# Exercise 1
################################################################################################
def _min_index(lst: list, i: int) -> int:
    """Return the index of the smallest item in lst[i:].

    In the case of ties, return the smaller index (i.e., the index that appears first).

    Preconditions:
        - 0 <= i <= len(lst) - 1

    >>> _min_index([2, 7, 3, 5], 1)
    2
    """
    minima = i
    for j in range(i + 1, len(lst)):
        if lst[j] < lst[minima]:
            minima = j
    return minima


################################################################################################
# Exercise 3
################################################################################################
def insertion_sort(lst: list) -> None:
    """Sort the given list using the selection sort algorithm.

    Note that this is a *mutating* function.

    >>> lst = [7, 3, 5, 2]
    >>> insertion_sort(lst)
    >>> lst
    [2, 3, 5, 7]
    """
    for i in range(0, len(lst)):
        # Loop invariant
        #   - lst[:i] is sorted
        _insert(lst, i)


# def _insert(lst: list, i: int) -> None:
#     """Move lst[i] so that lst[:i + 1] is sorted.
#
#     Preconditions:
#         - 0 <= i < len(lst)
#         - is_sorted(lst[:i])
#
#     >>> lst = [7, 3, 5, 2]
#     >>> _insert(lst, 1)
#     >>> lst
#     [3, 7, 5, 2]
#     """    for j in range(i, 0, -1):
#         if lst[j] < lst[j - 1]:
#             lst[j], lst[j - 1] = lst[j - 1], lst[j]
#
#

################################################################################################
# Demo
################################################################################################
def insertion_sort_by_key(lst: list, key: Optional[Callable] = None) -> None:
    """Sort the given list using the selection sort algorithm.

    If key is not None, sort the items by their corresponding return value when passed to key.

    Note that this is a *mutating* function.

    >>> lst = ['octopus', 'cat', 'david', 'hi']
    >>> insertion_sort_by_key(lst, key=len)
    >>> lst
    ['hi', 'cat', 'david', 'octopus']
    >>> lst2 = ['octopus', 'cat', 'david', 'hi']
    >>> insertion_sort_by_key(lst2)
    >>> lst2
    ['cat', 'david', 'hi', 'octopus']

    Preconditions:
        - if key is not None, then it can be called without error on every item in lst
    """
    for i in range(0, len(lst)):
        _insert_by_key(lst, i, key)


def _insert_by_key(lst: list, i: int, key: Optional[Callable] = None) -> None:
    """Move lst[i] so that lst[:i + 1] is sorted.

    If key is not None, sort items based on their return value when passed to key.

    Preconditions:
        - 0 <= i < len(lst)
    """
    for j in range(i, 0, -1):
        if key is None:
            if lst[j - 1] <= lst[j]:
                return
            else:
                # Swap lst[j - 1] and lst[j]
                lst[j - 1], lst[j] = lst[j], lst[j - 1]
        else:
            if key(lst[j - 1]) <= key(lst[j]):
                return
            else:
                lst[j - 1], lst[j] = lst[j], lst[j - 1]

################################################################################################
# Exercise 5
################################################################################################
def insertion_sort_memoized(lst: list,
                            key: Optional[Callable] = None) -> None:
    # Initialize a dictionary to store the results of calling `key`
    key_values = {}

    # for i in range(0, len(lst)):
    # _insert_memoized(lst, i, key, key_values)
