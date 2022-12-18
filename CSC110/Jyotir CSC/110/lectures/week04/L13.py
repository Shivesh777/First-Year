"""CSC110 Lecture 13 - Starter file

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.
"""
import math


####################################################################################################
# Exercise 1 - all_fluffy
####################################################################################################
def all_fluffy(s: str) -> bool:
    """Return whether every character in s is fluffy.

    Fluffy characters are those that appear in the word 'fluffy'.

    >>> all_fluffy('fffffuy')
    True
    >>> all_fluffy('abcfluffy')
    False
    """
    for i in range(0, len(s)):
        if s[i] not in 'fluffy':
            return False
    return True


####################################################################################################
# Demo 1
####################################################################################################
def count_adjacent_repeats(string: str) -> int:
    """Return the number of repeated adjacent characters in string.

    >>> count_adjacent_repeats('look')
    1
    >>> count_adjacent_repeats('David')
    0
    >>> count_adjacent_repeats('canal')
    0
    """
    # ACCUMULATOR repeats_so_far: keep track of the number of adjacent
    # characters that are identical
    repeats_so_far = 0

    for i in range(0, len(string)):
        if string[i] == string[i + 1]:
            repeats_so_far = repeats_so_far + 1

    return repeats_so_far


####################################################################################################
# Exercise 1 - is_sorted
####################################################################################################
def is_sorted(lst: list[int]) -> bool:
    """Return whether lst is sorted.

    A list L is sorted when for every pair of *adjacent* elements
    x and y in L, x <= y.

    lists of length < 2 are always sorted.

    >>> is_sorted([1, 5, 7, 100])
    True
    >>> is_sorted([1, 2, 1, 2, 1])
    False
    """
    for i in range(0, len(lst) - 1):
        if lst[i] > lst[i+1]:
            return False
    return True


####################################################################################################
# Demo 2
####################################################################################################
def count_money(counts: list[int], denoms: list[float]) -> float:
    """Return the total amount of money for the given coin counts and denominations.

    counts stores the number of coins of each type, and denominations stores the
    value of each coin type. Each element in counts corresponds to the element at
    the same index in denoms.

    Preconditions:
      - len(counts) == len(values)

    >>> count_money([2, 4, 3], [0.05, 0.10, 0.25])
    1.25
    """
    money_so_far = 0
    for i in range(len(counts)):
        money_so_far = money_so_far + counts[i] * denoms[i]
    return money_so_far

####################################################################################################
# Exercise 1 - inner_product and stretch_string
####################################################################################################
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
    x = 0
    for i in range(0, len(nums1)):
        x = x + nums1[i] * nums2[i]
    return x


def stretch_string(s: str, stretch_factors: list[int]) -> str:
    """Return a string consisting of the characters in s, each repeated
    a given number of times.


    Each character in s is repeated n times, where n is the int at the
    corresponding index in stretch_factors.
    For example, the first character in s is repeated stretch_factors[0] times.

    Preconditions:
        - len(s) == len(stretch_factors)
        - all({factor >= 0 for factor in stratch_factors})

    >>> stretch_string('David', [2, 4, 3, 1, 1])
    'DDaaaavvvid'
    >>> stretch_string('echo', [0, 0, 1, 5])
    'hooooo'
    """
    counter = ''
    for i in range(len(stretch_factors)):
        counter += s[i] * stretch_factors[i]
    return counter



####################################################################################################
# Demo 3
####################################################################################################
def sum_all(lists_of_numbers: list[list[int]]) -> int:
    """Return the sum of all numbers in lists_of_numbers.

    >>> sum_all([[1, 2, 3], [10, -5], [100]])
    111
    """
    # ACCUMULATOR sum_so_far: keep track of the running sum of the numbers.
    sum_so_far = 0

    for numbers in lists_of_numbers:  # numbers is a list of numbers, not a single number!
        for number in numbers:  # number is a single number
            sum_so_far = sum_so_far + number

    return sum_so_far


####################################################################################################
# Exercise 2 - total_mice
####################################################################################################
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
    """
    count = 0
    for cat in dict_of_cats:
        for i in range(len(dict_of_cats[cat])):
            if 'mouse' in dict_of_cats[cat][i]:
                count += 1
    return count


####################################################################################################
# Exercise 2 - can_pay_with_two_coins and max_average
####################################################################################################
def can_pay_with_two_coins(denoms: set[int], amount: int) -> bool:
    """Return whether the given amount is the sum of two distinct numbers
    from denoms.

    >>> can_pay_with_two_coins({1, 5, 10, 25}, 35)
    True
    >>> can_pay_with_two_coins({1, 5, 10, 25}, 12)
    False
    """


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
    for lst in lists_of_numbers:
      avg = calculate_average(lst)
        if max_so_far
