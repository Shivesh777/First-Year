"""CSC110 Fall 2022 Prep 5: Programming Exercises

Instructions (READ THIS FIRST!)
===============================

This Python module contains several function headers and descriptions.
Your task is to complete this module by doing the following for EACH function below:

1. Implement the function so that it does what its description claims,
   using a for loop. You may NOT use comprehensions for any part of this exercise.

    - You *may* use augmented assignment operations like "x += y" as a short form for
      "x = x + y". This will be covered in Chapter 6 of the Course Notes (and in lecture
      next week).

You do *not* need to add new doctests or preconditions (and in fact
you should *not* add any preconditions!). However, you may add doctests
to test your code---we certainly encourage you to test your code carefully
before making your final submission!

We have marked each place you need to write code with the word "TODO".
As you complete your work in this file, delete each TODO comment---this is a
good habit to get into early!

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2022 David Liu, Mario Badr, and Tom Fairgrieve.
"""
from dataclasses import dataclass
from python_ta.contracts import check_contracts


###############################################################################
# This data class is the same one we used last week. Do NOT modify this part.
###############################################################################
@check_contracts
@dataclass
class Person:
    """A person with some basic demographic information.
    """
    given_name: str
    family_name: str
    age: int
    address: str


###############################################################################
# Exercises start here
###############################################################################
@check_contracts
def total_age(people: list[Person]) -> int:
    """Return the sum of the ages of the given people.

    Return 0 if people is an empty list.

    Note: you must implement this function using a for loop. As a hint,
    the equivalent comprehension expression is:

        sum([person.age for person in people])
    """
    ages = 0
    for person in people:
        ages += person.age
    return ages


@check_contracts
def any_has_name(people: list[Person], name: str) -> bool:
    """Return whether at least one given person has a given_name equal to name OR
    a family_name equal to name.

    Note: you must implement this function using a for loop, using the early return pattern.
    As a hint, the equivalent comprehension expression is:

        any({person.given_name == name or person.family_name == name for person in people})
    """
    list_bools = []
    for person in people:
        if person.given_name == name or person.family_name == name:
            return True
    return False


@check_contracts
def at_least_n_adults(people: list[Person], n: int) -> bool:
    """Return whether there are at least n given people with an age of at least 18.

    Preconditions:
    - n >= 1

    Note: you must implement this function using a for loop with the accumulator pattern.
    We also strong recommend combining the accumulator with the *early return* pattern:
    think about in what cases the loop can "stop early" because it is certain what the
    function should return.
    """
    number = 0
    for person in people:
        if person.age >= 18:
            number += 1
        if number >= n:
            return True
    return False


@check_contracts
def count_matching_ages(group1: list[Person], group2: list[Person]) -> int:
    """Return the number of *corresponding pairs of people*, one from group1 and one from group2,
    that have the same age.

    By "corresponding pair of people", we mean a person from group1 and a person from group1 with
    the same index. For example, group1[0] is compared with group2[0], group1[1] is compared with
    group2[1], etc.

    Preconditions:
    - len(group1) == len(group2)

    Note: you must implement this function using an INDEX-BASED for loop. This function is
    similar to the "Two lists, one loop" example in Section 5.6 of the Course Notes.
    """
    number = 0
    for i in range(len(group1)):
        number += int(group1[i].age == group2[i].age)
    return number


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (In PyCharm, select the lines below and press Ctrl/Cmd + / to toggle comments.)
    import python_ta
    python_ta.check_all(config={
        'max-line-length': 120,
        'disable': ['R1714']
    })
