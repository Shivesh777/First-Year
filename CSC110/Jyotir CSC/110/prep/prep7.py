"""CSC110 Fall 2021 Prep 7: Programming Exercises

Instructions (READ THIS FIRST!)
===============================

This Python module contains several function headers and descriptions.
We have marked each place you need to fill in with the word "TODO".
As you complete your work in this file, delete each TODO comment.

You do not need to include doctests for this prep, though we strongly encourage you
to check your work carefully!

Note: the last two function's preconditions refer to math.gcd, which isn't actually
imported. This means that python_ta.contracts won't actually check those preconditions,
so it will be up to you to verify that these preconditions hold when you call the
functions in your own testing.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 David Liu, Mario Badr, and Tom Fairgrieve.
"""


###############################################################################
# Caesar cipher with ASCII characters (from Notes 7.1)
###############################################################################
def encrypt_ascii(k: int, plaintext: str) -> str:
    """Return the encrypted message using the Caesar cipher with key k.

    Preconditions:
        - all({ord(c) < 128 for c in plaintext})
        - 1 <= k <= 127

    >>> encrypt_ascii(4, 'Good morning!')
    'Kssh$qsvrmrk%'
    """
    ciphertext = ''

    for letter in plaintext:
        ciphertext = ciphertext + chr((ord(letter) + k) % 128)

    return ciphertext


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


###############################################################################
# Decrypting ciphertexts by brute force
###############################################################################
def brute_force_ascii_caesar(ciphertext: str) -> dict[int, str]:
    """Return a mapping of possible secret keys to decrypted plaintext messages.

    The mapping's keys should be the set {1, 2, ..., 127}.
    The corresponding value of key k is the plaintext message obtained by decrypting
    the given ciphertext with the secret key k, using ascii_decrypt.

    Preconditions:
        - ciphertext != ''
        - all({ord(c) < 128 for c in ciphertext})

    You may use either a dictionary comprehension or a for loop.
    (For extra practice, try implementing this function both ways!)

    >>> result = brute_force_ascii_caesar('Kssh$qsvrmrk%')
    >>> len(result)
    127
    >>> result[4]
    'Good morning!'
    """
    dic = {}
    for k in range(1, 128):
        dic.update({k: decrypt_ascii(k, ciphertext)})
    return dic


###############################################################################
# Implementing a new symmetric-key cryptosystem
###############################################################################
# In this exercise, you'll implement the encryption and decryption functions for a new
# symmetric-key cryptosystem described as follows:
#
# - The plaintexts and ciphertexts are strings.
# - The secret key is from the set {2, 3, ...}.
# - Encrypt(k, m) works as follows:
#     PRECONDITION: math.gcd(k, len(m)) = 1.
#         (It's possible to make the encryption work without this assumption,
#          but harder to do, so for this prep you can assume this holds.)
#
#     The ciphertext c has the same length as m.
#     For all i in {0, 1, ..., len(m) - 1), c[(i * k) % len(m)] = m[i].
#     In other words, c is a permutation (reordering) of the characters of m.
#
# - Decrypt(k, c) works as follows:
#     PRECONDITION: math.gcd(k, len(c)) = 1.
#
#     Simply do the encryption in reverse:
#     For all i in {0, 1, ..., len(c) - 1), m[i] = c[(i * k) % len(m)].
#
#  Example: m = 'David is cool', and k = 2. len(m) = 13 (Follow along on paper!)
#    m[0] -> c[0]
#    m[1] -> c[2]
#    m[2] -> c[4]
#    m[3] -> c[6]
#    m[4] -> c[8]
#    m[5] -> c[10]
#    m[6] -> c[12]
#    m[7] -> c[1]   <-- Since we're taking remainders modulo 13, and (2 * 7) % 13 = 1.
#    m[8] -> c[3]
#    m[9] -> c[5]
#    m[10] -> c[7]
#    m[11] -> c[9]
#    m[12] -> c[11]
#
#    So the encrypted string is 'Dsa vciodo li'


def encrypt_symmetric_modulo(k: int, plaintext: str) -> str:
    """Return the encrypted message of plaintext with the above cryptosystem using the key k.

    Preconditions:
        - math.gcd(k, len(plaintext)) == 1

    >>> encrypt_symmetric_modulo(2, 'David is cool')
    'Dsa vciodo li'

    Hint: this is tricky, and easiest done using an index-based for loop and list mutation.
    We've set up an accumulator for you to use: a list of characters of length m that you
    should fill in. Inside your loop use list index assignment to set a particular index
    in the accumulator, and then at the end of the function join the characters into a
    single string using str.join('', the_accumulator_list).
    """
    n = len(plaintext)

    # Accumulator
    ciphertext_characters = [''] * n

    for i in range(0, n):
        ciphertext_characters[(i * k) % len(plaintext)] = plaintext[i]

    return str.join('', ciphertext_characters)


def decrypt_symmetric_modulo(k: int, ciphertext: str) -> str:
    """Return the decrypted message of ciphertext using the key k.

    Preconditions:
        - math.gcd(k, len(ciphertext)) == 1

    >>> decrypt_symmetric_modulo(2, 'Dsa vciodo li')
    'David is cool'

    Hint: this one is easier to implement than encrypt_symmetric_modulo.
    You can use the same approach you used for that function, or a different approach.
    """
    n = len(ciphertext)
    encrypted_txt = [''] * n
    for i in range(0, n):
        encrypted_txt[i] = ciphertext[(i * k) % len(encrypted_txt)]
    return str.join('', encrypted_txt)


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'max-line-length': 100,
        'extra-imports': ['math', 'python_ta.contracts'],
        'disable': ['R1705']
    })

    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()
