"""David's Lecture 6 examples"""


def longest_cool_string(strings: list) -> int:
    """Return the length of the longest given string that contains the substring 'cool'.

    >>> longest_cool_string(['cool beans', 'hello', 'David is cool'])
    13
    """
    # First, find the strings containing 'cool'
    cool_strings = {string for string in strings if 'cool' in string}

    # Then, find their lengths.
    cool_lengths = {len(string) for string in cool_strings}

    # Finally, return the max length
    return max(cool_lengths)

    # Alternate version (combining the above steps into a single line):
    # return max({len(string) for string in strings if 'cool' in string})


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
