"""CSC110 Fall 2021 Prep 6: Programming Exercises

Instructions (READ THIS FIRST!)
===============================

This Python module contains several function headers and descriptions.
We have marked each place you need to fill in with the word "TODO".
As you complete your work in this file, delete each TODO comment---this is a
good habit to get into early!

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 David Liu, Mario Badr, and Tom Fairgrieve.
"""
import math
from hypothesis import given
from hypothesis.strategies import integers

####################################################################################################
# Mutation practice (from Week 5)
####################################################################################################
def only_evens(lst: list[list[int]]) -> list[list[int]]:
    """Return a new list of the lists in lst that contain only even integers.

    Use a for loop with a list accumulator, and use mutating operations to update
    the accumulator in the loop body.

    >>> only_evens([[1, 2, 4], [4, 0, 6], [22, 4, 3], [2]])
    [[4, 0, 6], [2]]
    """
    #ACCUMULATOR even_so_far: keep list of lists with all even numbers so far
    even_so_far = []
    for lst2 in lst:
        if all(num % 2 == 0 for num in lst2):
            list.append(even_so_far, lst2)
    return even_so_far


def get_order_quantities(table_orders: dict[str, list[str]]) -> dict[str, int]:
    """Return a mapping from food item to the number of that item ordered.

    In the input dictionary table_orders:
        - Each key is the name of a person.
        - Each corresponding value is a list of the food items that person has ordered.
          Duplicates are allowed!

    In the returned dictionary:
        - Each key a a food item.
        - Each corresponding value is the number of times that food item was ordered
          in table_orders, across all people.

    Use a for loop with a dictionary accumulator, and use mutating operations to update
    the accumulator in the loop body.

    >>> orders = {'David': ['Vegetarian stew', 'Poutine', 'Vegetarian stew'],\
                  'Mario': ['Steak pie', 'Poutine', 'Vegetarian stew'],\
                  'Jen': ['Steak pie', 'Steak pie']}
    >>> get_order_quantities(orders) == {'Vegetarian stew': 3, 'Poutine': 2, 'Steak pie': 3}
    True
    """
    #ACCUMULATOR
    order_so_far = {}
    for person in table_orders:
        for food in table_orders[person]:
            if food in order_so_far:
                order_so_far[food] = order_so_far[food] + 1
            else:
                order_so_far.update({food: 1})
    return order_so_far

####################################################################################################
# Number theory
####################################################################################################
def is_coprime(m: int, n: int) -> bool:
    """Return whether m and n are coprime (review the reading for the definition of coprime).

    Hints:
        - Use the math module's gcd function to calculate the gcd of two numbers.

    >>> is_coprime(3, 7)
    True
    >>> is_coprime(3, 9)
    False
    """
    if math.gcd(m, n) == 1:
        return True
    else:
        return False


def find_gcd(numbers: set[int]) -> int:
    """Return the greatest common divisor of all the given numbers.

    Preconditions:
        - len(numbers) >= 2

    Hints:
        - Use the math module's gcd function to calculate the gcd of two numbers.
        - Use an accumulator to store the gcd of the numbers seen so far.
        - For all ints x, gcd(x, 0) = x.
        - For all ints a, b, c, the gcd of all three numbers is equal to gcd((gcd(a, b), c).
          That is, you can calculate the gcd of a and b first, then calculate the gcd of
          that number and c.

    >>> find_gcd({18, 12})
    6
    >>> find_gcd({121, 99, -11, 0})
    11
    """
    #ACCUMULATOR gcd_so_far: keep track of greatest common divisor so far
    gcd_so_far = 0
    for num in numbers:
        gcd_so_far = math.gcd(gcd_so_far, num)
    return gcd_so_far


def equivalent_mod(a: int, b: int, n: int) -> bool:
    """Return whether a is equivalent to b modulo n.

    You can compute this by comparing remainders.

    Preconditions:
        - n >= 1

    >>> equivalent_mod(10, 66, 4)  # Both have remainder 2
    True
    >>> equivalent_mod(13, 19, 5)
    False
    """
    if a % n == b % n:
        return True
    else:
        return False


@given(a=integers(), n=integers(min_value=1))
def test_equivalence_reflexive(a: int, n: int) -> None:
    """Test that a is equivalent to a modulo n.

    (This property holds for all ints a and n, if n > 1.)
    """
    assert equivalent_mod(a, a, n)


@given(a=integers(), b=integers(), n=integers(min_value=1))
def test_equivalence_add_multiples(a: int, b: int, n: int) -> None:
    """Test that a is equivalent to (a + bn) modulo n.

    (This property holds for all ints a, b, and n, if n > 1.)
    """
    assert equivalent_mod(a, (a + b * n), n)


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={
        'max-line-length': 100,
        'extra-imports': ['math', 'python_ta.contracts', 'hypothesis.strategies'],
        'disable': ['R1705', 'W1114']
    })

    import python_ta.contracts
    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest
    doctest.testmod(verbose=True)

    import pytest
    pytest.main(['prep6.py'])
