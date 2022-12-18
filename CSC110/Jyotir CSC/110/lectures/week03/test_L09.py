"""CSC110 Lecture 9 - Starter file

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.
"""
from hypothesis import given
from hypothesis.strategies import integers

from L09 import is_even


####################################################################################################
# Lecture Demo
####################################################################################################
@given(x = integers())
def test_is_even_2x(x: int) -> None:
    """Test that is_even returns True when given a number of the form 2*x."""
    assert is_even(2 * x)


@given(x = integers())
def test_is_even_2x_plus_1(x: int) -> None:
    """Test that is_even returns False when given a number of the form 2*x + 1."""
    assert not is_even(2 * x + 1)


def test_num_evens_one_more_even(nums: list[int], x: int) -> None:
    """Test num_evens when you add one more even element."""


####################################################################################################
# Exercise 1
####################################################################################################
@given(a=integers(), d=integers())
def test_a(a: int, d: int) -> None:
    """TODO: docstring"""


if __name__ == '__main__':
    import pytest
    pytest.main(['test_L09.py', '-v'])
