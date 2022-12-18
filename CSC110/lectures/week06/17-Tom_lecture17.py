"""Tom's Lecture 17 examples - copied from David"""


def extended_euclidean_gcd(a: int, b: int) -> tuple[int, int, int]:
    """Return the gcd of a and b, and integers p and q such that

    gcd(a, b) == p * a + b * q.

    Preconditions:
        - a > 0  # Simplifying assumption for now
        - b > 0  # Simplifying assumption for now
    """
    x, y = a, b

    px, qx = 1, 0
    py, qy = 0, 1

    while y != 0:
        # assert math.gcd(x, y) == math.gcd(a, b)  # Loop Invariant 1
        assert x == px * a + qx * b                # Loop Invariant 2
        assert y == py * a + qy * b                # Loop Invariant 3

        q, r = divmod(x, y)

        x, y = y, r
        px, qx, py, qy = py, qy, px - q * py, qx - q * qy

    return (x, px, qx)


def modular_inverse(a: int, n: int) -> int:
    """Return the inverse of a modulo n, in the range 0 to n - 1 inclusive.

    Preconditions:
        - gcd(a, n) == 1
        - n > 0

    >>> modular_inverse(10, 3)  # 10 * 1 is equivalent to 1 modulo 3
    1
    >>> modular_inverse(3, 10)  # 3 * 7 is equivalent to 1 modulo 10
    7
    """
    # By the GCD Characterization Theorem, since gcd(a, n) = 1,
    # there exist integers p, q ∈ Z such that 1 = a * p + n * q.
    result = extended_euclidean_gcd(a, n)
    p = result[1]

    # And so n | a * p − 1 (by the definition of divisibility, taking k= −q)!
    # COMMENT: This statement is *not* necessary for the code to run, I put it in
    # just to illustrate how we can take statements in proofs and turn them into
    # assertions in code.
    # assert (a * p1 - 1) % n == 0

    # So let p = p1. Then n | a * p − 1, and so by the definition of
    # modular equivalence, a * p ≡ 1 (mod n).
    # We also use "% n" so that the p gets into the correct range.
    return p % n
