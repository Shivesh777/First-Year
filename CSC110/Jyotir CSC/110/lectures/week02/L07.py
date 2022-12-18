"""CSC110 Lecture 7 - Starter file

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
def get_status(scheduled: int, estimated: int) -> str:
    """Return the flight status for the given scheduled and estimated departure times.

    The times are given as integers between 0 and 23 inclusive, representing
    the hour of the day.

    The status is either 'On time' or 'Delayed'.

    >>> get_status(10, 10)
    'On time'
    >>> get_status(10, 12)
    'Delayed'
    """


####################################################################################################
# Exercise 1: Practice with if-statements
####################################################################################################
def can_vote(age: int) -> str:
    """Return a string indicating whether age is a legal voting age in Canada.

    In Canada, you must be at least 18 years old to vote.
    """
    if age < 18:
        return 'Too young to vote'
    else:
        return 'Allowed to vote'


def format_name(first: str, last: str) -> str:
    """Return the first and last names as a single string in the form: last, first.

    Mononymous persons (those with no last name) should have their name returned without a comma.

    >>> format_name('Cherilyn', 'Sarkisian')
    'Sarkisian, Cherilyn'
    >>> format_name('Cher', '')
    'Cher'
    """



def larger_sum(nums1: list, nums2: list) -> list:
    """Return the list with the larger sum.

    Assume that nums1 and nums2 are lists of floats.
    In the event of a tie, return nums1.

    >>> larger_sum([1.26, 2.01, 3.3], [3.0, 3.0, 3.0])
    [3.0, 3.0, 3.0]
    >>> larger_sum([2.0, 1.0], [1.0, 2.0])
    [2.0, 1.0]
    """


####################################################################################################
# Exercise 2: Multiple branches
####################################################################################################
def porridge_satisfaction(temperature: float) -> str:
    """Return what a picky eater says when tasting porridge with the given temperature.

    Temperatures greater than 50.0 are too hot, temperatures less than 49.0 are too cold,
    and the temperatures in between are just right.

    >>> porridge_satisfaction(65.5)
    'This porridge is too hot! Ack!!'
    >>> porridge_satisfaction(30.0)
    'This porridge is too cold! Brrr..'
    >>> porridge_satisfaction(49.5)
    'This porridge is just right! Yum!!'
    """
    if temperature > 50:
        return 'This porridge is too hot! Ack!!'
    elif temperature > 49.0:
        return 'This porridge is just right! Yum!!'
    else:
        return 'This porridge is too cold! Brrr..'



def rock_paper_scissors(player1: str, player2: str) -> str:
    """Return the winner of a game of rock, paper, scissors.

    The game is played with the following rules:
        1) 'rock' wins against 'scissors'
        2) 'scissors' wins against 'paper'
        3) 'paper' wins against 'rock'

    Ties are allowed.

    You may assume that the input strings are in {'rock', 'paper', 'scissors'}.

    >>> rock_paper_scissors('rock', 'scissors')
    'Player1 wins'
    >>> rock_paper_scissors('rock', 'paper')
    'Player2 wins'
    >>> rock_paper_scissors('rock', 'rock')
    'Tie!'
    """
    if player1 == player2:
        return 'Tie!'
    elif player1 == 'rock':
        if player2 == 'scissors':
            return 'Player1 wins'
        else:
            return 'Player2 wins'
    elif player2 == 'rock':
        if player1 == 'scissors':
            return 'Player2 wins'
        else:
            return 'Player1 wins'
    elif player1 == 'scissors' and player2 == 'paper':
        return 'Player1 wins'
    else:
        return 'Player2 wins'



####################################################################################################
# Exercise 3: Simplifying if-statements
####################################################################################################
def is_odd(n: int) -> bool:
    """Return whether n is odd (not divisible by 2).
    """
    return n % 2 == 0


def is_teenager(age: int) -> bool:
    """Return whether age is between 13 and 18 inclusive.

    HINT: identify the range of integers that make this function return True.
    """
    if age < 13:
        return False
    else:
        if age > 18:
            return False
        else:
            return True


def is_common_prefix(prefix: str, s1: str, s2: str) -> bool:
    """Return whether prefix is a common prefix of both s1 and s2.
    """
    if str.startswith(s1, prefix):
        if str.startswith(s2, prefix):
            return True
        else:
            return False
    else:
        return False


def same_corresponding_values(mapping: dict, key1: str, key2: str) -> bool:
    """Return whether the two given keys have the same corresponding value in mapping.

    Return False if at least one of the keys is not in the mapping.
    """
    if key1 not in mapping:
        return False
    elif key2 not in mapping:
        return False
    elif mapping[key1] == mapping[key2]:
        return True
    else:
        return False


####################################################################################################
# Exercise 4: The order of if conditions
####################################################################################################
def pick_animal1(number: int) -> str:
    """Return an animal (based on a number range).
    >>> pick_animal1(5)
    'Cat'
    """
    if number > 1:
        return 'Cat'
    elif number > 10:
        return 'Dog'
    else:
        return 'Duck'


def pick_animal2(number: int) -> str:
    """Return an animal (based on a number range)."""
    if number > 10:
        return 'Cat'
    elif number > 1:
        return 'Dog'
    else:
        return 'Duck'
