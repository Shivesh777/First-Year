"""David Lecture 17 examples"""


def extended_euclidean_gcd(a: int, b: int) -> tuple[int, int, int]:
    """Return the gcd of a and b, and integers p and q such that
    gcd(a, b) == p * a + b * q.

    Preconditions:
    - a >= 0
    - b >= 0

    >>> extended_euclidean_gcd(10, 3)
    (1, 1, -3)
    """
    x, y = a, b

    px, qx = 1, 0
    py, qy = 0, 1

    while y != 0:
        # assert math.gcd(x, y) == math.gcd(a, b)  # L.I. 1
        assert x == px * a + qx * b                # L.I. 2
        assert y == py * a + qy * b                # L.I. 3

        q, r = divmod(x, y)  # equivalent to q, r = (x // y, x % y)
        x, y = y, r

        px, qx, py, qy = py, qy, px - q * py, qx - q * qy

    return x, px, qx


def modular_inverse(a: int, n: int) -> int:
    """Return the inverse of a modulo n, in the range 0 to n - 1 inclusive.

    Preconditions:  (TODO: fill this in!)
    - math.gcd(a, n) == 1  # (in English: the gcd of a and n is 1)
    - n >= 1

    >>> modular_inverse(10, 3)  # 10 * 1 is equivalent to 1 modulo 3
    1
    >>> modular_inverse(3, 10)  # 3 * 7 is equivalent to 1 modulo 10
    7
    """
    # TODO: implement this function!
    result = extended_euclidean_gcd(a, n)
    gcd, p, q = result[0], result[1], result[2]

    # This isn't necessary, just a useful reminder!
    assert gcd == a * p + q * n

    return p % n

    # This has the right idea, but p isn't guaranteed to be in {0, 1, ..., n - 1}
    # return p

    # This has the right idea, but p could be < -n (so p + n still may not be
    # in the same range).
    # if p > 0:
    #     return p
    # else:
    #     return p + n









