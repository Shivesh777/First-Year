"""Tom Lecture 13 examples"""
from python_ta.debug import AccumulationTable
import math

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

    # for i in range(1, len(s))
    for i in range(0, len(s) - 1):  # s = 'look', len(s) = 4, so range(0, 3)
        if s[i] == s[i + 1]:
            repeats_so_far = repeats_so_far + 1

    return repeats_so_far


def count_money(counts: list[int], denoms: list[float]) -> float:
    """Return the total amount of money for the given coin
    counts and denominations.

    >>> count_money([2, 4, 3], [0.05, 0.10, 0.25])
    1.25
    """
    money_so_far = 0.0

    for i in range(0, len(counts)):
        money_so_far = money_so_far + counts[i] * denoms[i]

    return money_so_far


def sum_all(lists_of_numbers: list[list[int]]) -> int:
    """Return the sum of all the numbers in the given
    lists_of_numbers.

    >>> sum_all([[1, 2, 3], [10, -5], [100]])
    111
    """
    sum_so_far = 0

    for numbers in lists_of_numbers:  # numbers is a list[int]
        # sum_so_far = sum_so_far + ...
        for number in numbers:
            sum_so_far = sum_so_far + number

    return sum_so_far

def multiply_adjacent_repeats(strings: list[str]) -> int:
    """Return the product of the numbers of times in each
    given string that two adjacent characters are equal.

    >>> multiply_adjacent_repeats([
    ...     'look',      # 1 repeat
    ...     'Davviid',   # 2 repeats
    ...     'bbccaaa'])  # 4 repeats
    8
    """
    product_so_far = 1

    for s in strings:
        repeats_so_far = 0

        # for i in range(1, len(s))
        for i in range(0, len(s) - 1):  # s = 'look', len(s) = 4, so range(0, 3)
            if s[i] == s[i + 1]:
                repeats_so_far = repeats_so_far + 1

        repeats = repeats_so_far

        # repeats = count_adjacent_repeats(s)
        product_so_far = product_so_far * repeats

    return product_so_far

def all_fluffy(s: str) -> bool:
    """Return whether every character in s is fluffy.

    Fluffy characters are those that appear in the word 'fluffy'.

    >>> all_fluffy('fly')
    True
    >>> all_fluffy('fun')
    False
    """
    # Rewrite the following using an index based for loop
    # for char in s:
    #     if char not in 'fluffy':
    #         return False
    # return True
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
    """
    for i in range(0, len(lst) - 1):
        if lst[i] > lst[i+1]:
            return False
    return True


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
    str_so_far = ''
    for i in range(0, len(s)):
        str_so_far = str_so_far + s[i] * stretch_factors[i]
    return str_so_far

    # Compare to inner_product:
    # sum_so_far = 0.0
    #
    # for i in range(0, len(nums1)):
    #     sum_so_far = sum_so_far + nums1[i] * nums2[i]
    #
    # return sum_so_far


def total_mice(dict_of_cats: dict[str, list[str]]) -> int:
    """Return the number of mice stored in the given cat dictionary.

    dict_of_cats is a dictionary here:
        - Each key is the name of a cat
        - Each corresponding value is a list of items that the cat owns.
          An item is a *mouse* when it contains the string 'mouse'.
          (You can use the "in" operator to check whether one string is
          in another.)
        - 'mouse' appears at most once in each item in each list of items

    >>> total_mice({'Romeo': ['mouse 1', 'my fav mouse', 'flower'],
    ...             'Juliet': ['sock', 'mouse for tonight']})
    3
    >>> total_mice({'Asya': ['chocolate', 'toy'], 'Mitzey': []})
    0

    HINT: remember that when iterating over a dictionary, the loop
    variable refers to the *key* of the dictionary. Use key lookup
    (i.e., `dict_of_cats[key]`) to access the corresponding value.
    """
    mice_so_far = 0
    for cat in dict_of_cats:
        for item in dict_of_cats[cat]:
            if 'mouse' in item:
                mice_so_far = mice_so_far + 1
    return mice_so_far



def can_pay_with_two_coins(denoms: set[int], amount: int) -> bool:
    """Return whether the given amount is the sum of two distinct numbers
    from denoms.

    >>> can_pay_with_two_coins({1, 5, 10, 25}, 35)
    True
    >>> can_pay_with_two_coins({1, 5, 10, 25}, 12)
    False
    """
    # Notice that this is a version of the Cartesian product.
    # Version 1 (with accumulator). But can convert to early return!
    can_pay_so_far = False

    for x in denoms:
        for y in denoms:
            if x != y and x + y == amount:
                can_pay_so_far = True

    return can_pay_so_far


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

    for num_list in lists_of_numbers:
        sum_so_far = 0
        len_so_far = 0
        for num in num_list:
            sum_so_far = sum_so_far + num
            len_so_far = len_so_far + 1
        avg = sum_so_far / len_so_far
        if avg > max_so_far:
            max_so_far = avg
    return max_so_far

# PythonTA demo
def my_sum_pyta(numbers: list[int]) -> int:
    """Return the sum of the given numbers."""
    # ACCUMULATOR sum_so_far: keep track of the
    # sum of the numbers seen so far in the loop.
    sum_so_far = 0

    with AccumulationTable(['sum_so_far']):
        for number in numbers:
            sum_so_far = sum_so_far + number

    return sum_so_far


def sum_all_pyta(lists_of_numbers: list[list[int]]) -> int:
    """Return the sum of all the numbers in the given lists_of_numbers."""
    sum_so_far = 0

    for numbers in lists_of_numbers:              # numbers is a list[int]
        with AccumulationTable(['sum_so_far']):
            for number in numbers:                # number is an int
                sum_so_far = sum_so_far + number

    return sum_so_far

if __name__ == '__main__':
    import doctest
    doctest.testmod()
