"""Lecture 16 examples"""


def emphasize(words: list[str]) -> None:
    """Add emphasis to the end of a list of words."""
    new_words = ['believe', 'me!']
    list.extend(words, new_words)


def emphasize_v2(words: list[str]) -> None:
    """Add emphasis to the end of a list of words."""
    new_words = ['believe', 'me!']
    words = words + new_words
    # return words


def euclidean_gcd(a: int, b: int) -> int:
    """Return the gcd of a and b.

    Preconditions:
    - a >= 0
    - b >= 0
    """
    # 1. Initialize two variables x, y to the given numbers a and b.
    # x = a
    # y = b
    x, y = a, b
    x, y = abs(a), abs(b)  # Handling negatives

    while y != 0:  # 4. Repeat steps 2 and 3 until y is 0.
        # Loop invariant:
        # assert math.gcd(a, b) == math.gcd(x, y)  (would need to import math to run)

        # 2. Let r be the remainder when x is divided by y.
        r = x % y
        # 3. Reassign x and y to y and r, respectively.
        # x = y
        # y = r
        x, y = y, r

    # 5. At this point, x refers to the gcd of a and b.
    return x


def extended_euclidean_gcd(a: int, b: int) -> tuple[int, int, int]:
    """Return the gcd of a and b, and integers p and q such that

    gcd(a, b) == p * a + b * q.

    Preconditions:
    - a >= 0
    - b >= 0

    >>> extended_euclidean_gcd(13, 10)
    (1, -3, 4)
    """
    x, y = a, b

    px, qx = 1, 0
    py, qy = 0, 1  # NEW

    while y != 0:
        # assert math.gcd(x, y) == math.gcd(a, b)  # L.I. 1
        assert x == px * a + qx * b              # L.I. 2 (NEW)
        assert y == py * a + qy * b              # L.I. 3 (NEW)

        q, r = divmod(x, y)  # equivalent to q, r = (x // y, x % y)
        x, y = y, r

        px, qx, py, qy = py, qy, px - q * py, qx - q * qy  # NEW

    return x, px, qx
