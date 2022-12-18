"""CSC110 Fall 2022 Prep 3: Programming Exercises

Instructions (READ THIS FIRST!)
===============================

This Python module contains several function headers and descriptions.
Your task is to complete this module by doing the following for EACH function below:

1. Write precondition expressions in each function docstring, based on the English
   descriptions given. Each precondition expression must be valid Python code,
   and preceded by a "- " (see format in Course Notes Section 4.1).
2. Implement the function (i.e., write the function body so that the function
   does what the description claims).

You do NOT need to add additional doctests.

We have marked each place you need to write preconditions/code with the word "TODO".
As you complete your work in this file, delete each TODO comment---this is a
good habit to get into early!

We've added code for PythonTA to automatically check your precondition expressions
for each function (as described in Section 4.3, which we'll cover in lecture).
So to check your precondition expression:

1. Write the expression under "Preconditions:" in the docstring.
2. Run this file in the Python console. (Right-click -> Run File in Python Console)
3. Try calling the function with arguments that VIOLATE (make False) your precondition.
4. You should see an "AssertionError", indicating that python_ta checked your
   precondition expression and stopped the function call.

At the bottom of this file, we've included code in the "main" block for running
doctest example and running python_ta.check_all to check your submission for
this prep. We covered checking code with PythonTA in last week's lecture, and
will again during your tutorial in case you have questions about running it.
(This is also the same as how you'll run PythonTA on Assignment 1, if you have
already been working on that!)

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2022 David Liu, Mario Badr, and Tom Fairgrieve.
"""
from typing import Any
import python_ta.contracts


@python_ta.contracts.check_contracts
def same_at_index(s1: str, s2: str, index: int) -> bool:
    """Return whether s1 and s2 have the same character at the given index.

    This assumes that index is >= 0 and is a valid index for both s1 and s2.

    Preconditions:
      - s1 != ""
      - s2 != ""
      - 0 <= index < len(s1)
      - 0 <= index < len(s2)
      - isinstance(index, int) == True


    >>> same_at_index('Mario', 'David', 1)
    True
    >>> same_at_index('Hi', 'Bye', 0)
    False
    """
    return s1[index] == s2[index]


@python_ta.contracts.check_contracts
def bigger_max(nums1: set, nums2: set) -> set:
    """Return the set that has the larger maximum.

    Return nums1 if there is a tie.

    This assumes that both sets are non-empty, and that they only contain integers.

    NOTE: Use the builtin function isinstance to check whether a value has a certain
    type. For example, isinstance(3, int) is True, and isinstance('hi', int) is False.

    Preconditions:
      - nums1 != set()
      - nums2 != set()
      - all([isinstance(x, int) for x in nums1]) == True
      - all([isinstance(x, int) for x in nums2]) == True

    >>> bigger_max({1, 2, 3}, {4})
    {4}
    >>> bigger_max({1, 2, 3}, {1, 3})
    {1, 2, 3}
    """
    if max(nums1) >= max(nums2):
        return nums1
    else:
        return nums2


@python_ta.contracts.check_contracts
def lookup_with_backup(mapping: dict, key: Any, backup_key: Any) -> Any:
    """Return the corresponding value of key in mapping.

    If key is not in mapping, then return the corresponding value of of backup_key
    in mapping instead.

    This assumes that at least one of key and backup_key is a key in mapping.

    NOTE: the type contract here uses "Any" for key, backup_key, and the return type.
    We've included this so that you do *not* need to write any preconditions to check
    for the type of the keys or corresponding values in map.

    Preconditions:
      - any([key in mapping, backup_key in mapping]) == True
      - mapping != {}
      - isinstance(mapping, dict) == True

    >>> example_dict = {'Burger': 5.0, 'Fries': 3.0}
    >>> lookup_with_backup(example_dict, 'Fries', 'Burger')
    3.0
    >>> lookup_with_backup(example_dict, 'Cheeseburger', 'Burger')
    5.0
    """
    if key in mapping:
        return mapping[key]
    else:
        return mapping[backup_key]


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (In PyCharm, select the lines below and press Ctrl/Cmd + / to toggle comments.)
    import python_ta
    python_ta.check_all(config={
        'max-line-length': 120
    })
