"""CSC110 Fall 2022 Assignment 2, Part 1: Conditional Execution

Instructions (READ THIS FIRST!)
===============================

This Python module contains the functions you should complete for Part 1, Questions 1 and 2.
We have provided copies of the functions on the assignment handout, as well as incomplete
function definitions where you should complete your work. Remember that for these two
questions, you are writing new function implementations that meet the same specification
as the original functions (i.e., the return values should be equal). To test your work,
we suggest using some of the following strategies:

    1. Run this file in the Python console and call each corresponding pair of functions to
       see if their return values are equal.
    2. Add some doctest examples and run them using doctests.
    3. Write some unit tests in a separate file.
    4. Use hypothesis to write *property-based tests* in a separate file to see whether
       the return values of the two functions are equal on a wide range of inputs.
       (This is a perfect case of when to use property-based testing!!)

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2022 David Liu, Mario Badr, Tom Fairgrieve,
and Angela Zavaleta Bernuy
"""


###############################################################################
# Part 2, Question 1
###############################################################################
def mystery_1a_nested(x: list[int], y: list[int]) -> list[int]:
    """Mystery 1a."""
    if len(x) > 1 and len(y) > 1:
        return x
    else:
        if sum(x) > sum(y):
            return y + x
        else:
            return x + y


def mystery_1a_flat(x: list[int], y: list[int]) -> list[int]:
    """Return the same value as mystery_1a_nested, but using just a single if statement.
    """


def mystery_1b_nested(n: int, nums: set[int]) -> int:
    """Mystery 1b."""
    if n < len(nums):
        if n == 1:
            return 0
        else:
            if n % 2 == 0:
                return sum(nums)
            else:
                return sum(nums) + n
    else:
        return len(nums)


def mystery_1b_flat(n: int, nums: set[int]) -> int:
    """Return the same value as mystery_1b_nested, but using just a single if statement.
    """


###############################################################################
# Part 2, Question 2
###############################################################################
def mystery_2a_if(x: int, y: int) -> bool:
    """Mystery 2a."""
    if x < y:
        if 2 * x < y:
            return True
        elif 2 * x > y:
            return False
        else:
            return False
    else:
        if x == y:
            return False
        elif 2 * y < x:
            return False
        elif 2 * y > x:
            return True
        else:
            return False


def mystery_2a_no_if(x: int, y: int) -> bool:
    """Return the same value as mystery_2a_if, but without using any if statements.
    """


def mystery_2b_if(x: int, y: int) -> bool:
    """Mystery 2b."""
    if x >= 0:
        if y >= 0:
            if x >= y:
                return False
            else:
                return True
        else:
            return True
    else:
        return True


def mystery_2b_no_if(x: int, y: int) -> bool:
    """Return the same value as mystery_2b_if, but without using any if statements.
    """


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (In PyCharm, select the lines below and press Ctrl/Cmd + / to toggle comments.)
    # import python_ta
    # python_ta.check_all(config={
    #     'max-line-length': 120
    # })
