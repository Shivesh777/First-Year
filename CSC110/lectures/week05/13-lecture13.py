"""David Lecture 13 examples"""
from python_ta.debug import AccumulationTable
import math


# Examples from Section 5.6
def count_adjacent_repeats(s: str) -> int:
    """Return the number of times in the given string that two adjacent
    characters are equal.

    >>> count_adjacent_repeats('look')
    1
    >>> count_adjacent_repeats('David')
    0
    >>> count_adjacent_repeats('bbccaaa')
    4
    """
    repeats_so_far = 0

    for i in range(0, len(s) - 1):  # s = 'look', len(s) = 4, so range(0, 3)
        if s[i] == s[i + 1]:
            repeats_so_far = repeats_so_far + 1

    return repeats_so_far


def count_money(counts: list[int], denoms: list[float]) -> float:
    """Return the total amount of money for the given coin counts and denominations.

    counts stores the number of coins of each type, and denominations stores the
    value of each coin type. Each element in counts corresponds to the element at
    the same index in denoms.

    Preconditions:
      - len(counts) == len(denoms)

    >>> count_money([2, 4, 3], [0.05, 0.10, 0.25])
    1.25
    """
    # ACCUMULATOR money_so_far: keep track of the total money so far.
    money_so_far = 0.0

    for i in range(0, len(counts)):
        money_so_far = money_so_far + counts[i] * denoms[i]

    return money_so_far


# Exercise 1
def all_fluffy(s: str) -> bool:
    """Return whether every character in s is fluffy.

    Fluffy characters are those that appear in the word 'fluffy'.

    >>> all_fluffy('fffffuy')
    True
    >>> all_fluffy('abcfluffy')
    False
    """
    # Element-based for loop version
    # for character in s:
    #     if character not in 'fluffy':
    #         return False
    #
    # return True

    # Index-based for loop version
    for i in range(0, len(s)):
        if s[i] not in 'fluffy':
            return False

    return True


def is_sorted(lst: list[int]) -> bool:
    """Return whether lst is sorted.

    A list L is sorted when for every pair of *adjacent* elements
    x and y in L, x <= y.

    lists of length < 2 are always sorted.

    >>> is_sorted([1, 5, 7, 100])
    True
    >>> is_sorted([1, 2, 1, 2, 1])
    False
    >>> is_sorted([2, 1, 10, 20, 30, 40, 50, 50, 60, 70, 80, 90, 100, 110, 112])
    False
    """
    # if len(lst) == 0, then we have range(0, -1), an EMPTY range
    # if len(lst) == 1, then we have range(0, 0), an EMPTY range
    # Version 1
    for i in range(0, len(lst) - 1):  # INCORRECT: range(0, len(lst))
        if lst[i] > lst[i + 1]:   # OR: not (lst[i] <= lst[i + 1])
            return False

    return True

    # Version 2
    # for i in range(1, len(lst)):
    #     if lst[i - 1] > lst[i]:   # OR: not (lst[i - 1] <= lst[i])
    #         return False
    #
    # return True


def inner_product(nums1: list[float], nums2: list[float]) -> float:
    """Return the inner product of nums1 and nums2.

    The inner product of two lists is the sum of the products of the
    corresponding elements of each list:

        sum([nums1[i] * nums2[i] for i in range(0, len(nums1))])

    Preconditions:
        - len(nums1) == len(nums2)

    >>> inner_product([1.0, 2.0, 3.0], [0.5, 2.5, 0.0])
    5.5
    """
    sum_so_far = 0.0

    for i in range(0, len(nums1)):
        sum_so_far = sum_so_far + nums1[i] * nums2[i]

    return sum_so_far


def stretch_string(s: str, stretch_factors: list[int]) -> str:
    """Return a string consisting of the characters in s, each repeated
    a given number of times.

    Each character in s is repeated n times, where n is the int at the
    corresponding index in stretch_factors.
    For example, the first character in s is repeated stretch_factors[0] times.

    Preconditions:
        - len(s) == len(stretch_factors)
        - all({factor >= 0 for factor in stretch_factors})

    >>> stretch_string('David', [2, 4, 3, 1, 1])
    'DDaaaavvvid'
    >>> stretch_string('echo', [0, 0, 1, 5])
    'hooooo'
    """
    repeated_so_far = ''

    for i in range(0, len(s)):
        repeated_so_far = repeated_so_far + s[i] * stretch_factors[i]

    return repeated_so_far


def sum_all(lists_of_numbers: list[list[int]]) -> int:
    """Return the sum of all the numbers in the given lists_of_numbers.

    >>> sum_all([[1, 2, 3], [10, -5], [100]])
    111
    """
    sum_so_far = 0

    for numbers in lists_of_numbers:          # numbers is a list[int]
        for number in numbers:                # number is an int
            sum_so_far = sum_so_far + number

    return sum_so_far


def multiply_adjacent_repeats(strings: list[str]) -> int:
    """Return the product of the numbers of times in each given string that two
    adjacent characters are equal.

    >>> multiply_adjacent_repeats(['look', 'Davviid', 'bbccaaa'])  # 1 * 2 * 4
    8
    """
    product_so_far = 1

    for s in strings:
        # Version that uses a helper function
        # repeats = count_adjacent_repeats(s)
        # product_so_far = product_so_far * repeats

        # Using a nested loop
        # NOTE: repeats_so_far must be "reset" for each string s.
        # So, this assignment statement must appear inside the outer loop,
        # not above it.
        repeats_so_far = 0

        for i in range(0, len(s) - 1):  # s = 'look', len(s) = 4, so range(0, 3)
            if s[i] == s[i + 1]:
                repeats_so_far = repeats_so_far + 1

        product_so_far = product_so_far * repeats_so_far

    return product_so_far


# Exercise 2
def total_mice(dict_of_cats: dict[str, list[str]]) -> int:
    """Return the number of mice stored in the given cat dictionary.

    dict_of_cats is a dictionary here:
        - Each key is the name of a cat
        - Each corresponding value is a list of items that the cat owns.
          An item is a *mouse* when it contains the string 'mouse'.
          (You can use the "in" operator to check whether one string is
          in another.)

    >>> total_mice({'Romeo': ['mouse 1', 'my fav mouse', 'flower'],
    ...             'Juliet': ['sock', 'mouse for tonight']})
    3
    >>> total_mice({'Asya': ['chocolate', 'toy'], 'Mitzey': []})
    0

    HINT: remember that when iterating over a dictionary, the loop
    variable refers to the *key* of the dictionary. Use key lookup
    (i.e., `dict_of_cats[key]`) to access the corresponding value.
    """
    mouse_count_so_far = 0

    for cat in dict_of_cats:            # cat is 'Romeo', for example
        for item in dict_of_cats[cat]:  # dict_of_cats[cat] is ['mouse 1', 'my fav mouse', 'flower'], for example
            if 'mouse' in item:
                mouse_count_so_far = mouse_count_so_far + 1

        # could have defined an explicit variable: cat_possessions = dict_of_cats[cat]

    return mouse_count_so_far


def max_average(lists_of_numbers: list[list[float]]) -> float:
    """Return the largest average of the given lists_of_numbers.

    Preconditions:
        - lists_of_nubers != []
        - all({numbers != [] for numbers in lists_of_numbers})

    >>> max_average([[1.0, 3.4], [3.5, 4.0, -2.5]])
    2.2
    """
    # ACCUMULATOR max_so_far: keep track of the maximum average of the lists
    # visited so far. We initialize to negative infinity so that any
    # computed average will be greater than the starting value.
    # (i.e., for all floats x, x > -math.inf)
    max_so_far = -math.inf

    for numbers in lists_of_numbers:
        # Version that uses a helper function (from last lecture)
        # average = my_avg(numbers)

        # Calculate the average of numbers (this is taken directly from the Course Notes).
        sum_so_far = 0.0
        len_so_far = 0
        for number in numbers:
            sum_so_far = sum_so_far + number
            len_so_far = len_so_far + 1
        average = sum_so_far / len_so_far

        # Update max_so_far if necessary.
        if average > max_so_far:
            max_so_far = average

    return max_so_far


# PythonTA demo
def my_sum_pyta(numbers: list[int]) -> int:
    """Return the sum of the given numbers."""
    # ACCUMULATOR sum_so_far: keep track of the
    # sum of the numbers seen so far in the loop.
    sum_so_far = 0
    len_so_far = 0
    str_so_far = ''

    with AccumulationTable(['sum_so_far', 'len_so_far', 'str_so_far']):
        for number in numbers:
            sum_so_far = sum_so_far + number
            len_so_far = len_so_far + 1
            str_so_far = str_so_far + 'David' * number

    return sum_so_far


# Try out this example yourself! AccumulationTable doesn't handle nested loops
# well, but can be used to display the accumulation tables of the inner loops.
def sum_all_pyta(lists_of_numbers: list[list[int]]) -> int:
    """Return the sum of all the numbers in the given lists_of_numbers."""
    sum_so_far = 0

    for numbers in lists_of_numbers:              # numbers is a list[int]
        with AccumulationTable(['sum_so_far']):
            for number in numbers:                # number is an int
                sum_so_far = sum_so_far + number

    return sum_so_far
