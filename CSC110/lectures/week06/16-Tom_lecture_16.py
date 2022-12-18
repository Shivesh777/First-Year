"""Tom's lecture 16 examples"""

import math


def euclidean_gcd(a: int, b: int) -> int:
    """Return the gcd of a and b.

    Preconditions:
      - a >= 0
      - b >= 0

    >>> euclidean_gcd(124124124, 110)
    2
    >>> euclidean_gcd(19201, 3587)
    211
    """
    # for now, could just used variables
    # a, b (and not introduced x, y) but
    # later we want both a,b and x,y.
    x = a
    y = b
    while y != 0:
        # Loop invariant: gcd(a, b) == gcd(x, y)
        assert math.gcd(a, b) == math.gcd(x, y)
        # apply the theorem
        r = x % y

        x = y
        y = r

    return x




if __name__ == '__main__':
    import doctest
    doctest.testmod()
