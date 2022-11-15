"""CSC110 Fall 2022 Assignment 2, Part 3: Wordle!

Module Description
==================
This Python file contains some code for defining various constants related to Wordle
and a helper function for Part 3(c).

You should not modify this file (we will be using our own version for testing purposes).

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2022 David Liu and Tom Fairgrieve.
"""
import itertools

from python_ta.contracts import check_contracts


# Here, we define the characters representing the three different statuses for a single character in Wordle.
# Note that we're using different letters instead of different coloured squares to help better contrast
# between the three statuses (including for those with colour-blindness).
CORRECT = 'Y'
WRONG_POSITION = '?'
INCORRECT = 'N'

ALL_STATUSES = {CORRECT, WRONG_POSITION, INCORRECT}


@check_contracts
def cartesian_product_general(collections: list[list]) -> list[list]:
    """Returns the Cartesian product of the given collections.

    Preconditions:
    - collections != []

    NOTE: you are *not* responsible for understanding the implementation of this function,
    as it uses some Python syntax/features that we haven't covered in this course. However,
    you *are* responsible for reading this docstring carefully to understand how to use this
    function in find_correct_guesses_multiple.

    >>> list0 = [1, 2, 3]
    >>> list1 = [10, 20]
    >>> list2 = [100, 200]
    >>> cartesian_product_general([list0, list1])  # This is the familiar Cartesian product with 2 collections
    [[1, 10], [1, 20], [2, 10], [2, 20], [3, 10], [3, 20]]
    >>> result = cartesian_product_general([list0, list1, list2])  # Now, all combinations across 3 collections
    >>> import pprint
    >>> pprint.pprint(result)  # We didn't have to use this library, but it makes the output a bit more readable
    [[1, 10, 100],
     [1, 10, 200],
     [1, 20, 100],
     [1, 20, 200],
     [2, 10, 100],
     [2, 10, 200],
     [2, 20, 100],
     [2, 20, 200],
     [3, 10, 100],
     [3, 10, 200],
     [3, 20, 100],
     [3, 20, 200]]
    """
    return [list(x) for x in itertools.product(*collections)]


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
