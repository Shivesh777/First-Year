"""Lecture 12 examples"""
from dataclasses import dataclass
import datetime


def my_sum(numbers: list[int]) -> int:
    """Return the sum of the given numbers.

    Preconditions:
    - all x > 0

    >>> my_sum([10, 20, 30])
    60
    """
    sum_so_far = 0

    for number in numbers:
        sum_so_far = sum_so_far + number

    return sum_so_far


# Exercise 1
def long_greeting(names: list[str]) -> str:
    """Return a greeting message that greets every person in names.

    Each greeting should have the form "Hello <name>! " (note the space at the end).
    The returned string should be the concatenation of all the greetings.

    >>> long_greeting(['David', 'Mario'])  # Note the "extra" space at the end
    'Hello David! Hello Mario! '
    """
    # For comparison
    # sum_so_far = 0
    #
    # for number in numbers:
    #     sum_so_far = sum_so_far + number
    #
    # return sum_so_far

    message_so_far = ''

    for name in names:
        message_so_far = message_so_far + 'Hello ' + (name * 10) + '! '

        # This is similar to my_sum, but isn't quite right
        # message_so_far = message_so_far + name

        # Homework: try running this!
        # message_so_far = message_so_far + ' Hello ' + (name * 10) + '!'

    return message_so_far


def my_len(items: list) -> int:
    """Return the size of the given list.

    >>> my_len([10, 20, 30])
    3
    """
    # ACCUMULATOR len_so_far: keep track of the
    # number of the elements in numbers seen so far.
    len_so_far = 0

    for _ in items:  # underscore is used to name a loop variable that isn't used in the body
        len_so_far = len_so_far + 1

    return len_so_far


def my_avg(numbers: list[int]) -> int:
    """Return the average of the given numbers.

    Preconditions:
    - numbers != []
    """
    # TWO accumulators!
    # ACCUMULATOR len_so_far: keep track of the
    # number of items seen so far.
    len_so_far = 0
    # ACCUMULATOR sum_so_far: keep track of the
    # sum of items seen so far.
    sum_so_far = 0

    for number in numbers:
        len_so_far = len_so_far + 1
        sum_so_far = sum_so_far + number

    return sum_so_far / len_so_far


# Exercise 2
@dataclass
class MarriageData:
    """..."""
    id: int
    civic_centre: str
    num_licenses: int
    month: datetime.date


def total_licenses_for_centre_v1(data: list[list], civic_centre: str) -> int:
    """Return how many marriage licenses were issued in the given civic centre."""
    return sum([row[2] for row in data if row[1] == civic_centre])


def total_licenses_for_centre_v2(data: list[MarriageData], civic_centre: str) -> int:
    """Return how many marriage licenses were issued in the given civic centre.

    Use a comprehension for this version.
    """
    return sum([row.num_licenses for row in data if row.civic_centre == civic_centre])


def total_licenses_for_centre_v3(data: list[MarriageData], civic_centre: str) -> int:
    """Return how many marriage licenses were issued in the given civic centre.

    Use a for loop for this version.
    """
    licenses_so_far = 0

    for row in data:
        if row.civic_centre == civic_centre:
            licenses_so_far = licenses_so_far + row.num_licenses

    return licenses_so_far


def sum_evens(numbers: list[int]) -> int:
    """Return the sum of the given numbers that are even.

    >>> sum_evens([10, 3, 4])
    14
    """
    # ACCUMULATOR sum_so_far: keep track of the
    # sum of the elements in numbers seen so far.
    sum_so_far = 0

    for number in numbers:
        if number % 2 == 0:
            sum_so_far = sum_so_far + number

    return sum_so_far


def any_contains_cool(strings: list[str]) -> bool:
    """Return whether at least one given string contains the string `'cool'`.

    >>> any_contains_cool(['David', 'is', 'very cool', 'of', 'course'])
    True
    """
    # ACCUMULATOR cool_so_far: keep track of
    # whether 'cool' is in any string seen so far.
    cool_so_far = False

    for string in strings:
        if 'cool' in string:
            cool_so_far = True

    return cool_so_far


def any_contains_cool_v2(strings: list[str]) -> bool:
    """Return whether at least one given string contains the string `'cool'`.
    """
    # No accumulator, but using an *early return*
    for string in strings:
        if 'cool' in string:
            return True

    return False


def any_contains_cool_v3(strings: list[str]) -> bool:
    """Return whether at least one given string contains the string `'cool'`.

    >>> any_contains_cool_v2(['David', 'is', 'very cool', 'of', 'course'])
    True
    """
    for string in strings:
        if 'cool' in string:
            return True

        # PROBLEM: this return statement is now part of the loop body,
        # and will cause the loop to stop early!
        return False


# Exercise 3
def civic_centre_meets_threshold_v1(data: list[list],
                                    civic_centre: str, num: int) -> bool:
    """Return whether civic_centre issued at least num marriage licences every month.

    You only need to worry about the rows that appear in data;
    don't worry about "missing" months.

    Preconditions:
        - num > 0
        - civic_centre in {'TO', 'NY', 'ET', 'SC'}
        - data satisfies all of the properties described in earlier lectures
    """
    licenses_issued = [row[2] for row in data if row[1] == civic_centre]
    return all({num_issued >= num for num_issued in licenses_issued})


def civic_centre_meets_threshold_v2(data: list[MarriageData],
                                    civic_centre: str, num: int) -> bool:
    """Return whether civic_centre issued at least num marriage licences every month.

    You only need to worry about the rows that appear in data;
    don't worry about "missing" months.

    Preconditions:
        - num > 0
        - civic_centre in {'TO', 'NY', 'ET', 'SC'}
        - data satisfies all of the properties described in earlier lectures

    Use a comprehension for this version.
    """
    licenses_issued = [row.num_licenses for row in data if row.civic_centre == civic_centre]
    return all({num_issued >= num for num_issued in licenses_issued})


def civic_centre_meets_threshold_v3(data: list[MarriageData],
                                    civic_centre: str, num: int) -> bool:
    """Return whether civic_centre issued at least num marriage licences every month.

    You only need to worry about the rows that appear in data;
    don't worry about "missing" months.

    Preconditions:
        - num > 0
        - civic_centre in {'TO', 'NY', 'ET', 'SC'}

    Use a for loop for this version.
    """
    # Version 1: using an accumulator
    licenses_so_far = 0

    for row in data:
        if row.civic_centre == civic_centre:
            licenses_so_far = row.num_licenses

    return licenses_so_far >= num

    # Version 2: still using an accumulator, but now with an additional early return
    # licenses_so_far = 0
    #
    # for row in data:
    #     if row.civic_centre == civic_centre:
    #         licenses_so_far = row.num_licenses
    #
    #     if licenses_so_far >= num:
    #         return True
    #
    # return False


def count_uppercase(s: str) -> int:
    """Return the number of uppercase letters in s.

    >>> count_uppercase('Mario')
    1
    >>> count_uppercase('lol')
    0
    """
    num_uppercase_so_far = 0

    for char in s:
        if str.isupper(char):
            num_uppercase_so_far = num_uppercase_so_far + 1

    return num_uppercase_so_far


def all_fluffy(s: str) -> bool:
    """Return whether every character in s is fluffy.

    Fluffy characters are those that appear in the word 'fluffy'.

    >>> all_fluffy('fly')
    True
    >>> all_fluffy('fun')
    False
    """
    # This is an example of UNIVERSAL search ("for all characters char in s, char is fluffy")
    # We can still use an early return, but now the early return should occur if we find a
    # *counterexample* to the search condition.
    for char in s:
        if char not in 'fluffy':
            return False

    return True

    # Good homework exercise: try implementing this function using the accumulator pattern
    # and no early return.


def sum_davids(scores: dict[str, int]) -> int:
    """Return the sum of all values in scores that correspond to a key that
    contains 'David'.

    >>> sum_davids({'David Liu': 3, 'Mario Badr': 7, 'David Bowie': 5})
    8
    """
    sum_so_far = 0

    # I've provided a structure that you'll need to fill in.
    # Remember that key is a KEY in the dictionary, and scores[key]
    # is the CORRESPONDING VALUE in the dictionary for that key.
    for key in scores:
        if ...:
            sum_so_far = sum_so_far + ...

    return sum_so_far


def david_vs_mario(scores: dict[str, int]) -> str:
    """Return the name of the person with the highest total score in scores.

    David's score is the sum of all values in scores that correspond
    to a key that contains the string 'David'.

    Mario's score is the sum of all values in scores that correspond
    to a key that contains the string 'Mario'.

    If there is a tie, return 'David' (obviously).

    >>> david_vs_mario({'David L': 3, 'Mario B': 7, 'David B': 5, 'Super Mario': 12})
    'Mario'
    """
    # Similar to sum_davids, but now use TWO accumulators!
    sum_david_so_far = 0
    sum_mario_so_far = 0

    for key in scores:
        ...

    if sum_david_so_far >= sum_mario_so_far:
        return ...
    else:
        return ...
