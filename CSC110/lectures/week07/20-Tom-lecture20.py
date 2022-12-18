"""Lecture 20 Examples for Tom's section"""
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
    # 1. Compute n = pq.
    n = p * q

    # 2. Choose integer e in {2, 3, .. phi(n)} such that gcd(e, phi(n)) = 1.
    phi_n = (p - 1) * (q - 1)
    e = random.randint(2, phi_n)
    while math.gcd(e, phi_n) > 1:
        e = random.randint(2, phi_n)

    assert math.gcd(e, phi_n) == 1  # We know this is true after the while loop ends

    # 3. Compute d (inverse of e modulo phi(n)). ed equivalent to 1 (mod phi(n)).
    # d = [x for x in range(2, phi_n) if e * x % phi_n == 1][0]
    d = modular_inverse(e, phi_n)

    # alternate: d = pow(e, -1, phi_n)

    # Return private key and public key.
    return ((p, q, d), (n, e))


def rsa_encrypt(public_key: tuple[int, int], plaintext: int) -> int:
    """Encrypt the given plaintext using the recipient's public key.

    Preconditions:
        - public_key is a valid RSA public key (n, e)
        - 0 < plaintext < public_key[0]
    """
    n, e = public_key
    # alternate:
    # n = public_key[0]
    # e = public_key[1]
    return pow(plaintext, e, n)


def rsa_decrypt(private_key: tuple[int, int, int], ciphertext: int) -> int:
    """Decrypt the given ciphertext using the recipient's private key.

    Preconditions:
        - private_key is a valid RSA private key (p, q, d)
        - 0 < ciphertext < private_key[0] * private_key[1]
    """
    p, q, d = private_key[0], private_key[1], private_key[2]
    n = p * q

    return pow(ciphertext, d, n)


def rsa_encrypt_text(public_key: tuple[int, int], plaintext: str) -> str:
    """Encrypt the given plaintext using the recipient's public key.

    Preconditions:
        - public_key is a valid RSA public key (n, e)
        - all({0 < ord(c) < public_key[0] for c in plaintext})
    """
    # From Caesar cipher
    ciphertext = ''
    for letter in plaintext:
        # Version 1:
        ciphertext = ciphertext + chr(rsa_encrypt(public_key, ord(letter)))

        # Version 2: (a little faster since fewer function calls)
        # ciphertext = ciphertext + chr(pow(ord(letter), e, n))

    return ciphertext


def rsa_decrypt_text(private_key: tuple[int, int, int], ciphertext: str) -> str:
    """Decrypt the given ciphertext using the recipient's private key.

    Preconditions:
        - private_key is a valid RSA private key (p, q, d)
        - all({0 < ord(c) < private_key[0] * private_key[1] for c in ciphertext})
    """
    plaintext = ''

    for letter in ciphertext:
        plaintext = plaintext + chr(rsa_decrypt(private_key, ord(letter)))

    return plaintext


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
    result = extended_euclidean_gcd(a, n)
    p = result[1]

    return p % n

if __name__ == '__main__':
    p, q = 607, 83
    n = p * q
    phi_n = (p - 1) * (q - 1)
    e = 11
    d = 9035
    assert e * d % phi_n == 1
    public_key = (n, e)
    private_key = (p, q, d)

    print('Public key: (n, e) = ', public_key)
    print('Private key: (p, q, d) = ', private_key)

    m = 'David thinks you are cool'
    print('\nEncrypting: ', m)
    m_prime = rsa_encrypt_text(public_key, m)
    print('    gives ', m_prime)

    z = input(' ')
    print('\nDecrypting: ', m_prime)
    m_prime_prime = rsa_decrypt_text(private_key, m_prime)
    print('    gives ', m_prime_prime)

    assert m == m_prime_prime
