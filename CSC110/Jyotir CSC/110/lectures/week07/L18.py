"""CSC110 Lecture 18 - Starter file

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.
"""


def extended_gcd(a: int, b: int) -> tuple[int, int, int]:
    """Return the gcd of a and b, and integers p and q such that

    gcd(a, b) == p * a + b * q.

    >>> extended_gcd(10, 3)
    (1, 1, -3)
    """
    x, y = a, b

    # Initialize px, qx, py, and qy
    px, qx = 1, 0
    py, qy = 0, 1

    while y != 0:
        # Loop invariants
        # assert math.gcd(a, b) == math.gcd(x, y)  # L.I. 1
        assert x == px * a + qx * b  # L.I. 2
        assert y == py * a + qy * b  # L.I. 3

        q, r = divmod(x, y)  # quotient and remainder when a is divided by b

        # Update x and y
        x, y = y, r

        # Update px, qx, py, and qy
        px, qx, py, qy = py, qy, px - (q * py), qx - (q * qy)

    return x, px, qx


def modular_inverse(a: int, n: int) -> int:
    """Return the inverse of a modulo n, in the range 0 to n - 1 inclusive.

    Preconditions:
    - n > 0
    - gcd(a, n) == 1




    >>> modular_inverse(10, 3)  # 10 * 1 is equivalent to 1 modulo 3
    1
    >>> modular_inverse(3, 10)  # 3 * 7 is equivalent to 1 modulo 10
    7
    """

    x, p1, q1 = extended_gcd(a, n)

    # Step 2: Try the examples, and notice that the docstring says the return value must be in
    # the range "0 to n-1". How can we use modulo to fix this?

    return p1 % n

def ComputeGCD(a: int, b: int):
    if b == 0:
        return a
    else:
        return ComputeGCD(b, a % b)

num1 = int(input("Enter a num"))
num2 = int(input("Enter a num"))
print(ComputeGCD(num1, num2))
