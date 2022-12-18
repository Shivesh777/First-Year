"""David Lecture 18 examples"""


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
        plaintext = plaintext + chr((ord(letter) - k) % 128)

    return plaintext


# One-Time Pad Cryptosystem
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
    # Very similar to encrypt_ascii!
    ciphertext = ''

    for i in range(0, len(plaintext)):
        ciphertext = ciphertext + chr((ord(plaintext[i]) + ord(k[i])) % 128)

    return ciphertext


def decrypt_otp(k: str, ciphertext: str) -> str:
    """Return the decrypted message of ciphertext using the key k with the
    one-time pad cryptosystem.

    Precondtions:
        - all({ord(c) < 128 for c in ciphertext})
        - all({ord(c) < 128 for c in k})

    >>> decrypt_otp('david', ',&B53')
    'HELLO'
    """
    # Very similar to decrypt_ascii!
    plaintext = ''

    for i in range(0, len(ciphertext)):
        plaintext = plaintext + chr((ord(ciphertext[i]) - ord(k[i])) % 128)

    return plaintext


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
    # try all possible 'a' values
    for possible_a in range(2, p):
        # check whether g ** a is equivalent to g_a modulo p
        if pow(g, possible_a, p) == g_a:
            # if so, compute (g ** b) ** a!
            return pow(g_b, possible_a, p)

        # This version uses ** and % instead of the pow function.
        # In general, you should use the pow function for modular
        # exponentiation, as it's more efficient for larger numbers.
        # if (g ** possible_a % p) == g_a:
        #     return g_b ** possible_a % p
