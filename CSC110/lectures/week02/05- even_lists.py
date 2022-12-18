"""Functions that determine whether numbers are even."""


def is_even(n: int) -> bool:
    """Return whether n is even.

    >>> is_even(42)
    True
    >>> is_even(1989)
    False
    """
    return n % 2 == 0


def all_even(numbers: list) -> bool:
    """Return whether every number in numbers is even.

    >>> all_even([0, 2, 4])
    True
    >>> all_even([0, 1, 2])
    False
    """
    # return True
    return list.count([is_even(n) for n in numbers], True) == len(numbers)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
