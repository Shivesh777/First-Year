"""CSC110 Lecture 19 - Starter file

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.
"""


####################################################################################################
# Demo
####################################################################################################
def encrypt_ascii(k: int, plaintext: str) -> str:
    """Return the encrypted message using the Caesar cipher with key k.

    Preconditions:
        - all({ord(c) < 128 for c in plaintext})
        - 1 <= k <= 127

    >>> encrypt_ascii(4, 'Good morning!')
    'Kssh$qsvrmrk%'
    """
    # ciphertext = ''
    #
    # for letter in plaintext:
    #     ciphertext = ciphertext + chr((ord(letter) + k) % 128)
    #
    # return ciphertext
    n = len(plaintext)
    ciphertext_characters = [''] * n

    # TODO

    return str.join('', ciphertext_characters)


def decrypt_ascii(k: int, ciphertext: str) -> str:
    """Return the decrypted message using the Caesar cipher with key k.

    Preconditions:
        - all({ord(c) < 128 for c in ciphertext})
        - 1 <= k <= 127

    >>> decrypt_ascii(4, 'Kssh$qsvrmrk%')
    'Good morning!'
    """
    plaintext = ''

    for letter in ciphertext:
        plaintext += chr((ord(letter) - k) % 128)

    return plaintext


# Brute force: 'OLaTO+T^+NZZW'

####################################################################################################
# Exercise 1
####################################################################################################
def encrypt_otp(k: str, plaintext: str) -> str:
    """Return the encrypted message of plaintext using the key k with the
    one-time pad cryptosystem.

    Precondtions:
        - len(k) >= len(plaintext)
        - all({ord(c) < 128 for c in plaintext})
        - all({ord(c) < 128 for c in k})

    >>> encrypt_otp('david', 'HELLO')
    ',&B53'
    """


def decrypt_otp(k: str, ciphertext: str) -> str:
    """Return the decrypted message of ciphertext using the key k with the
    one-time pad cryptosystem.

    Precondtions:
        - all({ord(c) < 128 for c in ciphertext})
        - all({ord(c) < 128 for c in k})

    >>> decrypt_otp('david', ',&B53')
    'HELLO'
    """


####################################################################################################
# Exercise 2
####################################################################################################
def break_diffie_hellman(p: int, g: int, g_a: int, g_b: int) -> int:
    """Return the shared Diffie-Hellman secret key obtained from the eavesdropped information.

    Remember that the secret key is (g ** (a * b)) % p, where a and b are the
    secret exponents chosen by Alice and Bob.
    You'll need to find at least one of a and b to compute the secret key.

    Preconditions:
        - p, g, g_a, and g_b are the values exhanged between Alice and Bob
          in the Diffie-Hellman algorithm

    >>> p = 23
    >>> g = 2
    >>> g_a = 9  # g ** 5 % p
    >>> g_b = 8  # g ** 14 % p
    >>> break_diffie_hellman(p, g, g_a, g_b)  # g ** (5 * 14) % p
    16
    """
    for a in range(1, p):
        if (g ** a) % p == g_a:
            return (g_b ** a) % p
