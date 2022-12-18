"""Lecture 8 examples"""
from python_ta.contracts import check_contracts


def max_length(strings: set) -> int:
    """Return the maximum length of a string in the given
    strings.

    Preconditions:
      - strings != set()

    Postconditions:
      - return_value is the max length of a string in strings
    """
    return max({len(s) for s in strings})


@check_contracts
def calculate_pay(start: int, end: int, pay_rate: float) -> float:
    """Return the pay of an employee who worked for the given time at the given pay rate.

    start and end represent the hour (from 0 to 23 inclusive) that the employee
    started and ended their work.

    pay_rate is the hourly pay rate and must be >= 15.0 (the minimum wage).

    Preconditions:
    - 0 <= start <= 23
    - 0 <= end <= 23
    - 0 less than end and less than 23 LOL
    - pay_rate >= 15.0
    - start < end

    >>> calculate_pay(3, 5, 15.5)
    31.0
    >>> calculate_pay(9, 21, 22.0)
    264.0
    """
    return (end - start) * pay_rate


def is_even(value: int) -> bool:
    """Return whether value is even."""
    return value % 2 == 0


# Exercise 2
def divides(d: int, n: int) -> bool:
    """Return whether d divides n.

    >>> divides(3, 9)   # Is 9 divisible by 3? (Yes)
    True
    >>> divides(3, 10)  # Is 10 divisible by 3? (No)
    False
    """
    if d == 0:
        return n == 0
    else:
        return n % d == 0
