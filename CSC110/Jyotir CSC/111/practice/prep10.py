"""CSC111 Winter 2022 Prep 10: Programming Exercises

Instructions (READ THIS FIRST!)
===============================

This module contains the mergesort algorithm from the prep readings, as well as a few
additional functions for you to implement.

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


def mergesort(lst: list) -> list:
    """Return a new sorted list with the same elements as lst.

    This is a *non-mutating* version of mergesort; it does not mutate the
    input list.

    >>> mergesort([10, 2, 5, -6, 17, 10])
    [-6, 2, 5, 10, 10, 17]
    """
    if len(lst) < 2:
        return lst.copy()  # Use the list.copy method to return a new list object
    else:
        # Divide the list into two parts, and sort them recursively.
        mid = len(lst) // 2
        left_sorted = mergesort(lst[:mid])
        right_sorted = mergesort(lst[mid:])

        # Merge the two sorted halves. Using a helper here!
        return _merge(left_sorted, right_sorted)


def _merge(lst1: list, lst2: list) -> list:
    """Return a sorted list with the elements in lst1 and lst2.

    Preconditions:
        - is_sorted(lst1)
        - is_sorted(lst2)

    >>> _merge([-1, 3, 7, 10], [-3, 0, 2, 6])
    [-3, -1, 0, 2, 3, 6, 7, 10]
    """
    i1, i2 = 0, 0
    sorted_so_far = []

    while i1 < len(lst1) and i2 < len(lst2):
        # Loop invariant:
        # sorted_so_far is a merged version of lst1[:i1] and lst2[:i2]
        assert sorted_so_far == sorted(lst1[:i1] + lst2[:i2])

        if lst1[i1] <= lst2[i2]:
            sorted_so_far.append(lst1[i1])
            i1 += 1
        else:
            sorted_so_far.append(lst2[i2])
            i2 += 1

    # When the loop is over, either i1 == len(lst1) or i2 == len(lst2)
    assert i1 == len(lst1) or i2 == len(lst2)

    # In either case, the remaining unmerged elements can be concatenated to sorted_so_far.
    if i1 == len(lst1):
        return sorted_so_far + lst2[i2:]
    else:
        return sorted_so_far + lst1[i1:]


################################################################################
# Prep exercises
################################################################################
def merge_indexed(lst: list, m: int) -> list:
    """Return a sorted list containing the items in lst.

    This function should use the same algorithm as the _merge helper function,
    with the two "sorted lists" being lst[:m] and lst[m:].
    Don't use built-in sorting functions or other list operations; follow the
    implementation of _merge as closely as possible. You don't need to copy over
    the loop invariant, although you may find it helpful to do so.

    Note that this function is public, as we are importing and testing it directly.

    Preconditions:
        - 0 <= m < len(lst)
        - is_sorted_sublist(lst, 0, m)
        - is_sorted_sublist(lst, m, len(lst))

    (You're welcome to copy over your implementation of is_sorted_sublist from last week's
    prep; if you don't, PythonTA will just ignore the last two preconditions.)

    >>> lst = [10, 20, 30, 4, 15, 16, 99]
    >>> merge_indexed(lst, 3)  # sorted sublists are lst[:3] and lst[3:]
    [4, 10, 15, 16, 20, 30, 99]
    """
    i1, i2 = 0, 0
    sorted_so_far = []
    lst1 = lst[:m]
    lst2 = lst[m:]
    while i1 < len(lst1) and i2 < len(lst2):
        # Loop invariant:
        # sorted_so_far is a merged version of lst1[:i1] and lst2[:i2]
        assert sorted_so_far == sorted(lst1[:i1] + lst2[:i2])

        if lst1[i1] <= lst2[i2]:
            sorted_so_far.append(lst1[i1])
            i1 += 1
        else:
            sorted_so_far.append(lst2[i2])
            i2 += 1

    # When the loop is over, either i1 == len(lst1) or i2 == len(lst2)
    assert i1 == len(lst1) or i2 == len(lst2)

    # In either case, the remaining unmerged elements can be concatenated to sorted_so_far.
    if i1 == len(lst1):
        return sorted_so_far + lst2[i2:]
    else:
        return sorted_so_far + lst1[i1:]


def merge_sublists(lst: list, b: int, m: int, e: int) -> None:
    """Merge two sorted sublists in lst into one sorted sublist.

    This is similar to merge_indexed, except:
        - The two sublists are now lst[b:m] and lst[m:e]
        - Rather than returning a new list, this function mutates lst so that
          lst[b:e] is a sorted version of the two previous sublists.

    Preconditions:
        - 0 <= b <= m <= e < len(lst)
        - is_sorted_sublist(lst, b, m)
        - is_sorted_sublist(lst, m, e)

    >>> lst = [100, 3, 10, 16, 2, 11, 20, 30, -1]
    >>> merge_sublists(lst, 1, 4, 8)  # sorted sublists are lst[1:4] and lst[4:8]
    >>> lst  # Note that the 100 and -1 aren't affected.
    [100, 2, 3, 10, 11, 16, 20, 30, -1]
    >>> merge_sublists(lst, 3, 3, 3)
    >>> lst  # No change
    [100, 2, 3, 10, 11, 16, 20, 30, -1]


    IMPORTANT implementation note: even though this function doesn't return a new list,
    you can still create a new local list object to do the merging, and then copy the
    contents back to lst[b:e] when you're done. This means that this algorithm won't be
    in-place (since it creates a list object of non-constant size), but that's okay.
    It's actually very complex to try to implement this function in an in-place way,
    just like it's hard to implement an in-place mergesort.

    As with merge_indexed, you should not use built-in sorting functions or other list
    methods, but instead follow the implementation of _merge as closely as possible.
    You may, but are not required to, assign to a list slice, e.g. lst[0:10] = ...
    """
    lst1 = lst[b:m]
    lst2 = lst[m:e]
    i1, i2 = 0, 0
    sorted_so_far = []
    while i1 < len(lst1) and i2 < len(lst2):
        # Loop invariant:
        # sorted_so_far is a merged version of lst1[:i1] and lst2[:i2]
        assert sorted_so_far == sorted(lst1[:i1] + lst2[:i2])

        if lst1[i1] <= lst2[i2]:
            sorted_so_far.append(lst1[i1])
            i1 += 1
        else:
            sorted_so_far.append(lst2[i2])
            i2 += 1

    # When the loop is over, either i1 == len(lst1) or i2 == len(lst2)
    assert i1 == len(lst1) or i2 == len(lst2)

    # In either case, the remaining unmerged elements can be concatenated to sorted_so_far.
    if i1 == len(lst1):
        sorted_so_far = sorted_so_far + lst2[i2:]
    else:
        sorted_so_far = sorted_so_far + lst1[i1:]

    lst[b: e] = sorted_so_far


def mergesort_2(lst: list) -> None:
    """MUTATE lst so that it is sorted.
    """
    if len(lst) < 2:
        # Do nothing
        pass
    else:
        # Divide the list into two parts, and sort them recursively.
        mid = len(lst) // 2
        left = lst[:mid]
        right = lst[mid:]
        mergesort(left)
        mergesort(right)

        # Merge the two sorted halves.
        # Assume _merge has the exact same behaviour as before.
        lst = _merge(left, right)


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
