"""CSC110 Fall 2021 Prep 9: Programming Exercises

Instructions (READ THIS FIRST!)
===============================

This Python module contains several function headers and descriptions.
We have marked each place you need to fill in with the word "TODO".
As you complete your work in this file, delete each TODO comment.

You do not need to include doctests for this prep, though we strongly encourage you
to check your work carefully!

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 David Liu, Mario Badr, and Tom Fairgrieve.
"""
from dataclasses import dataclass
import math


####################################################################################################
# Part 1
#
# Most websites where you can create an account now ask you for a "strong password". The definition
# of strong password varies. In Part 1, you will implement 1 definition of a strong password and
# get some practice with functions that mutate their input.
#
# For those curious, these definitions of a "strong password" don't actually seem to be based on
# evidence. See: https://nakedsecurity.sophos.com/2014/10/24/do-we-really-need-strong-passwords/
#
# If you are still coming up with your own passwords (or, worse, reusing the same password for more
# than one account), please look into getting a password manager.
####################################################################################################
def is_strong_password(password: str) -> bool:
    """Return whether password is a strong password.

    A strong password has at least 6 characters, contains at least one lowercase letter, at least
    one uppercase letter, and at least one digit.

    >>> is_strong_password('I<3csc110')
    True
    >>> is_strong_password('ilovelamp')
    False
    """

    digit = sum(letter.isdigit() for letter in password) >= 1
    lower = sum(letter.islower() for letter in password) >= 1
    upper = sum(letter.isupper() for letter in password) >= 1
    length = len(password) >= 6
    return all([length, upper, lower, digit])


def remove_weak_passwords(passwords: list[str]) -> list[str]:
    """Remove and return the weak passwords in the given list of passwords.

    A weak password is a password that is not strong.

    This function both mutates the given list (to remove the weak passwords)
    and returns a new list (the weak passwords that were removed).
    """
    # NOTE: This implementation has an error, and does not do what the docstring claims.
    # How would you explain the error? (Not to be handed in, but a good question for review!)
    # weak_passwords = [p for p in passwords if not is_strong_password(p)]
    # all_passwords = [p for p in passwords if is_strong_password(p)]

    # Next, in the space below, implement this function remove_weak_passwords correctly.
    # Warning: do NOT attempt to mutate the passwords list while looping over it
    # ("for password in passwords:"). This leads to unexpected errors in Python!
    # Instead, first compute the passwords to remove, and then remove each of them
    # from the list of passwords. (You can look up the "list.remove" method.)

    weak_passwords = [p for p in passwords if not is_strong_password(p)]
    for i in weak_passwords:
        passwords.remove(i)
    return weak_passwords


def test_mutation() -> None:
    """Test that remove_weak_passwords correctly mutates its list argument.

    Your test case should have at least one weak password in the input passwords.
    """
    passwords = ['I<3csc110', 'ilovelamp']
    remove_weak_passwords(passwords)
    assert passwords == ['I<3csc110']


def test_return() -> None:
    """Test that remove_weak_passwords correctly returns a list of the weak passwords.

    Your test case should have at least one weak password in the input passwords.
    """
    passwords = ['I<3csc110', 'ilovelamp']
    assert remove_weak_passwords(passwords) == ['ilovelamp']


####################################################################################################
# Part 2
#
# Ideally, the passwords we use when we create our accounts are not stored in plaintext. Otherwise,
# any hacker who finds their way into a company's server has just gained access to every password
# stored on that server, with no further hacking required. Here, you will implement some functions
# to encrypt passwords.
#
# Further reading (not required for this prep)
# ============================================
#
# Unfortunately, sometimes passwords are not stored securely.
# See: https://www.howtogeek.com/434930/why-are-companies-still-storing-passwords-in-plain-text/
#
# You may also find it interesting that encryption may not be the best method for storing passwords.
# Do a quick search for: hashing vs. encryption. Here are some relevant articles:
#   - https://cheapsslsecurity.com/blog/hashing-vs-encryption/
#   - https://cybernews.com/security/hashing-vs-encryption/
#   - https://www.maketecheasier.com/password-hashing-encryption/
####################################################################################################
def divides(d: int, n: int) -> bool:
    """Return whether d divides n."""
    if d == 0:
        return n == 0
    else:
        return n % d == 0


def is_prime(p: int) -> bool:
    """Return whether p is prime."""
    possible_divisors = range(2, math.floor(math.sqrt(p)) + 1)
    return p > 1 and all({not divides(d, p) for d in possible_divisors})


def phi(n: int) -> int:
    """Return the number of positive integers between 1 and n inclusive that are coprime with n.

    You can use the math.gcd function imported from the math module.

    Preconditions:
        - n >= 1

    >>> phi(5)
    4
    >>> phi(15)
    8
    >>> phi(1)
    1
    """
    coprimes = 0
    for i in range(1, n + 1):
        if math.gcd(n, i) == 1:
            coprimes += 1
    return coprimes


@dataclass
class PublicKey:
    """A public key for the RSA cryptosystem.

    This is good review of data classes: this data class is another way of representing
    and RSA public key, rather than using tuples like we saw in class.

    TODO: translate these representation invariants into Python expressions under
          "Representation Invariants".
          1. n is greater than 1
          2. e is between 2 and phi(n) - 1, inclusive
          3. e is coprime to phi(n) (again, you can use math.gcd)

    Representation Invariants:
        - self.n >= 1
        - 2 <= self.e <= phi(self.n) - 1
        - math.gcd(self.e, phi(self.n)) == 1
    """
    n: int
    e: int


@dataclass
class PrivateKey:
    """A private key for the RSA cryptosystem.

    TODO: translate these representation invariants into Python expressions under
          "Representation Invariants".
          1. p and q are both prime
          2. p and q are not equal
          3. d is between 2 and phi(p * q) - 1, inclusive

    Representation Invariants:
        - is_prime(self.p)
        - is_prime(self.q)
        - self.p != self.q
        - 2 <= self.d <= phi(self.p * self.q) - 1
    """
    p: int
    q: int
    d: int


def encrypt_password(public_key: PublicKey, password: str) -> str:
    """Return the password encrypted using public_key and the RSA cryptosystem.

    Your implementation should be very similar to the one from class, except now
    the public key is a data class rather than a tuple.
    """
    encrypted = ''
    for letter in password:
        encrypted = encrypted + chr((ord(letter) ** public_key.e) % public_key.n)
    return encrypted


def decrypt_password(private_key: PrivateKey, encrypted: str) -> str:
    """Return decrypt the given encrypted password using private_key and the RSA cryptosystem.

    Your implementation should be very similar to the one from class, except now
    the public key is a data class rather than a tuple.
    """
    n = private_key.p * private_key.q
    decrypted = ''
    for letter in encrypted:
        decrypted = decrypted + chr((ord(letter) ** private_key.d) % n)
    return decrypted


def encrypt_passwords(public_key: PublicKey, passwords: list[str]) -> None:
    """Encrypt each password in passwords using the given public_key and the RSA cryptosystem.

    This function mutates passwords, and does not return anything.
    The encrypted passwords should appear in the same order as the
    corresponding original passwords.
    """
    for i in range(len(passwords)):
        passwords[i] = encrypt_password(public_key, passwords[i])


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 100,
        'extra-imports': ['math', 'dataclasses', 'python_ta.contracts'],
        'disable': ['R1705', 'C0200']
    })

    import python_ta.contracts
    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest
    doctest.testmod(verbose=True)

    import pytest
    pytest.main(['prep9.py', '-v'])
