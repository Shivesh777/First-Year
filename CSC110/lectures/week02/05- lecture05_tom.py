"""Tom's Lecture 5 Examples"""


def alice(x: int) -> int:
    """No details to save space"""
    return x + 2

def bob(x: int) -> int:
    """No details to save space"""
    return x * 3

def cube(x: float) -> float:
    """Return x cubed.

    >>> cube(3.0)
    27.0
    >>> cube(2.5)
    15.625
    """
    return x ** 3


def is_even(n: int) -> bool:
    """Return whether n is even.

    >>> is_even(42)
    True
    >>> is_even(1961)
    False
    """
    return n % 2 == 0

if __name__ == '__main__':
    import doctest
    doctest.testmod()
