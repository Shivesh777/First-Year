"""CSC110 Fall 2022 Assignment 2, Part 1: Conditional Execution

Instructions (READ THIS FIRST!)
===============================

This Python module contains the function mystery_3 described on the assignment handout,
and the start of various test cases to either complete or delete, according to the
instructions found below.

We have provided code in the main block of this file to run your test cases using pytest.

NOTE: We will *NOT* be checking this file with PythonTA.

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
from hypothesis import given
from hypothesis.strategies import text


###############################################################################
# The function you are analyzing (do not change this!)
###############################################################################
def mystery_3(s1: str, s2: str, s3: str) -> int:
    """Mystery 3."""
    if len(s1) != len(s2) or len(s1) != len(s3):  # Branch 1
        return 1
    elif s1 == '':                                # Branch 2
        return 2
    elif s1 == s2 + s3:                           # Branch 3
        return 3
    else:                                         # Branch 4
        return 4


###############################################################################
# 3a. (unit tests)
###############################################################################
# INSTRUCTIONS: below, there are four (incomplete) unit test functions, one for
# each branch of mystery_3. For each of the tests, you should either:
# 1. Complete it by giving an example input to the function that causes it
#    to execute that branch and return the corresponding value, OR
# 2. Delete or comment out the test, if that branch is unreachable.


def test_branch_1_reachable() -> None:
    """A test demonstrating that branch 1 of mystery_3 is reachable.

    DELETE/COMMENT OUT THIS TEST IF BRANCH 1 IS UNREACHABLE.
    """
    s1 = 'Shiva'
    s2 = 'Vishnu'
    s3 = 'Brahma'
    assert mystery_3(s1, s2, s3) == 1


def test_branch_2_reachable() -> None:
    """A test demonstrating that branch 2 of mystery_3 is reachable.

    DELETE/COMMENT OUT THIS TEST IF BRANCH 2 IS UNREACHABLE.
    """
    s1 = ''
    s2 = ''
    s3 = ''
    assert mystery_3(s1, s2, s3) == 2


# def test_branch_3_reachable() -> None:
#     """A test demonstrating that branch 3 of mystery_3 is reachable.
#
#     DELETE/COMMENT OUT THIS TEST IF BRANCH 3 IS UNREACHABLE.
#     """
#     s1 = ...
#     s2 = ...
#     s3 = ...
#     assert mystery_3(s1, s2, s3) == 3


def test_branch_4_reachable() -> None:
    """A test demonstrating that branch 4 of mystery_3 is reachable.

    DELETE/COMMENT OUT THIS TEST IF BRANCH 4 IS UNREACHABLE.
    """
    s1 = 'Shivesh'
    s2 = 'Aryaman'
    s3 = 'Pranjal'
    assert mystery_3(s1, s2, s3) == 4


###############################################################################
# 3b. (property-based tests)
###############################################################################
# INSTRUCTIONS: below, there are four (incomplete) property-based test functions,
# one for each branch of mystery_3. For each of the tests, you should either:
# 1. Complete it by replacing the ... with an assert statement which says that
#    mystery_3 never returns the value in that branch's return statement, OR
# 2. Delete or comment out the test, if that branch is reachable.
#
# NOTE: These tests use a new hypothesis strategy function, text, which (as
# you might have guessed) is a strategy for generating "random" string values.


# @given(s1=text(), s2=text(), s3=text())
# def test_branch_1_unreachable(s1: str, s2: str, s3: str) -> None:
#     """A test demonstrating that branch 1 of mystery_3 is unreachable.
#
#     DELETE/COMMENT OUT THIS TEST IF BRANCH 1 IS REACHABLE.
#     """
#     ...


# @given(s1=text(), s2=text(), s3=text())
# def test_branch_2_unreachable(s1: str, s2: str, s3: str) -> None:
#     """A test demonstrating that branch 2 of mystery_3 is unreachable.
#
#     DELETE/COMMENT OUT THIS TEST IF BRANCH 2 IS REACHABLE.
#     """
#     ...


@given(s1=text(), s2=text(), s3=text())
def test_branch_3_unreachable(s1: str, s2: str, s3: str) -> None:
    """A test demonstrating that branch 3 of mystery_3 is unreachable.

    DELETE/COMMENT OUT THIS TEST IF BRANCH 3 IS REACHABLE.
    """
    assert mystery_3(s1, s2, s3) != 3


# @given(s1=text(), s2=text(), s3=text())
# def test_branch_4_unreachable(s1: str, s2: str, s3: str) -> None:
#     """A test demonstrating that branch 4 of mystery_3 is unreachable.
#
#     DELETE/COMMENT OUT THIS TEST IF BRANCH 4 IS REACHABLE.
#     """
#     ...


if __name__ == '__main__':
    import pytest
    pytest.main(['a2_part1_q3.py', '-v'])
