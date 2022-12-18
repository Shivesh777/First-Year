"""CSC110 Fall 2020 Prep 3: Programming Exercises

Instructions (READ THIS FIRST!)
===============================

This Python module contains several function headers and descriptions.
Your task is to complete this module by doing the following for EACH function below:

1. Write precondition expressions in each function docstring, based on the English
   descriptions given. Each precondition expression must be valid Python code,
   and preceded by a "- " (see format in Course Notes Section 3.7).
2. Implement the function (i.e., write the function body so that the function
   does what the description claims).

You do NOT need to add additional doctests.

We have marked each place you need to write preconditions/code with the word "TODO".
As you complete your work in this file, delete each TODO comment---this is a
good habit to get into early!

At the bottom of this file, we've included code in the "main" block for running
doctest example and running python_ta.check_all to check your submission for
this prep. But we've ALSO added the python_ta.contracts part (described in 3.7)
to help you check your precondition expressions. To check a precondition expression:

1. Write the expression under "Preconditions:" in the docstring.
2. Run this file in the Python console. (Right-click -> Run File in Python Console)
3. Try calling the function with arguments that VIOLATE (make False) your precondition.
4. You should see an "AssertionError", indicating that python_ta checked your
   precondition expression and stopped the function call.


Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2020 David Liu and Mario Badr.
"""


def same_at_index(s1: str, s2: str, index: int) -> bool:
    """Return whether s1 and s2 have the same character at the given index.

    This assumes that index is >= 0 and a valid index for both s1 and s2.

    Preconditions:
      index >= 0
      index < len(s1) and index < len(s2)


    >>> same_at_index('Mario', 'David', 1)
    True
    >>> same_at_index('Hi', 'Bye', 0)
    False
    """
    return s1[index] == s2[index]


def bigger_max(nums1: set, nums2: set) -> set:
    """Return the set that has the larger maximum.

    Return nums1 if there is a tie.

    This assumes that both sets are non-empty, and that they only contain integers.

    NOTE: Use the builtin function isinstance to check whether a value has a certain
    type. For example, isinstance(3, int) is True, and isinstance('hi', int) is False.

    Preconditions:
      - nums1 != set()
      - nums2 != set()
      - all([isinstance(x, int) == True for x in nums1])
      - all([isinstance(y, int) == True for y in nums2])

    >>> bigger_max({1, 2, 3}, {4})
    {4}
    >>> bigger_max({1, 2, 3}, {1, 3})
    {1, 2, 3}
    """
    if max(nums2) > max(nums1):
        return nums2
    else:
        return nums1


def lookup_with_backup(mapping: dict, key: object, backup_key: object) -> object:
    """Return the corresponding value of key in mapping.

    If key is not in mapping, then return the corresponding value of of backup_key
    in mapping instead.

    This assumes that at least one of key and backup_key are a key in map.

    NOTE: the type contract here uses "object" for key, backup_key, and the return type.
    We've included this so that you do *not* need to write any preconditions to check
    for the type of the keys or corresponding values in map.

    Preconditions:
      - key in mapping == True or backup_key in mapping == True

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
    import python_ta.contracts
    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest
    doctest.testmod(verbose=True)

    # When you are ready, uncomment the following lines to check
    # your work with PythonTA.
    import python_ta
    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts'],
        'max-line-length': 100,
        'disable': ['R1705']
    })
