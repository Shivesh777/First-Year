"""CSC110 Fall 2022 Assignment 4: Number Theory, Cryptography, and Algorithm Running Time Analysis

Module Description
==================
This Python file contains some code for some helper functions for Part 4 of this assignment.
These are copies of the code we developed in lecture, and you should be understand all of it!

You should not modify this file (we will be using our own version for testing purposes).

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2022 David Liu and Tom Fairgrieve.
"""
import math
import random


def rsa_generate_key(p: int, q: int) -> \
        tuple[tuple[int, int, int], tuple[int, int]]:
    """Return an RSA key pair generated using primes p and q.

    The return value is a tuple containing two tuples:
      1. The first tuple is the private key, containing (p, q, d).
      2. The second tuple is the public key, containing (n, e).

    Preconditions:
        - p and q are prime
        - p != q

    Hints:
        - If you choose a random number e between 2 and phi(n), there isn't a guarantee that
        gcd(e, phi(n)) = 1. You can use the following pattern to keep picking random numbers
        until you get one that is coprime to phi(n).

            e = ... # Pick an initial choice
            while math.gcd(e, ___) > 1:
                e = ... # Pick another random choice

        - random.randint(a, b) returns a random number between a and b, inclusive
        - We've provided copies of the modular_inverse and extended_euclidean_gcd functions...
    """
    # 2. Compute n = pq.
    n = p * q

    # 3. Choose integer e in {2, 3, .. phi(n)} such that gcd(e, phi(n)) = 1.
    phi_n = (p - 1) * (q - 1)
    e = random.randint(2, phi_n)
    while math.gcd(e, phi_n) > 1:
        e = random.randint(2, phi_n)

    assert math.gcd(e, phi_n) == 1  # We know this is true after the while loop ends

    # 4. Compute d (inverse of e modulo phi(n)). ed equivalent to 1 (mod phi(n)).
    # d = [x for x in range(2, phi_n) if e * x % phi_n == 1][0]
    d = modular_inverse(e, phi_n)

    # Return private key and public key.
    return (p, q, d), (n, e)


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

    return x, px, qx


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
    result = extended_euclidean_gcd(a, n)
    p = result[1]

    return p % n
