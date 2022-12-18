"""CSC110 Fall 2022 Assignment 1, Part 2: Programming Exercises

Instructions (READ THIS FIRST!)
===============================

This Python module contains the functions you should complete for Part 2 of this assignment.
Your task is to complete this module by doing the following for EACH function below:

1. Add a new doctest example to the function description in the space provided.
   This will ensure you understand what the function is supposed to do.
   (If you want, you may add more than one doctest for your own testing purposes.)
2. Implement the body of the function so that it does what its description claims.

In some function descriptions, we have written "You may ASSUME..." This means that
when you are writing each function body, you only have to consider possible values
for the parameters that satisfy these assumptions. You do not need to check for,
or "handle", values that violate these assumptions.

We have marked each place you need to write a doctest/code with the word "TODO".
As you complete your work in this file, delete each "TODO" comment---this is a
good habit to get into early!

By the way, we *will* be checking that you've added new doctest examples, and that
your examples correctly illustrate a call to that function. Don't skip this!

For instructions on checking your work with python_ta, please consult the
assignment handout.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2022 David Liu, Mario Badr, Tom Fairgrieve,
and Angela Zavaleta Bernuy.
"""
import math


def calculate_sphere_volume(radius: float) -> float:
    """Return the volume of a sphere with the given radius, rounded to 2 decimal places.

    You may ASSUME that:
    - radius > 0

    You can consult https://en.wikipedia.org/wiki/Sphere#Enclosed_volume to find the
    mathematical formula for the volume of a sphere. Use math.pi in your code as the
    value of pi in the formula.

    >>> calculate_sphere_volume(1.0)
    4.19
    >>> calculate_sphere_volume(4.0)
    268.08
    """
    volume = 4 / 3 * math.pi * (radius ** 3)
    return round(volume, 2)


def format_name_and_number(given_name: str, family_name: str, phone_number: int) -> str:
    """Return a formatted string for the person with given_name, family_name, and phone_number.

    The format of the returned string is:

        <family_name>, <given_name>: <phone_number>

    where <family_name> is converted to ALL CAPS. Our doctest example illustrates this!

    >>> format_name_and_number('David', 'Liu', 4169990000)
    'LIU, David: 4169990000'
    >>> format_name_and_number('Shivesh', 'PrAkAsh', 4043217777)
    'PRAKASH, Shivesh: 4043217777'
    """
    f_string = str.upper(family_name) + ", " + given_name + ": " + str(phone_number)
    return f_string


def get_vowel_locations(s: str) -> list:
    """Return a list of booleans indicating whether each character in s is a lowercase vowel.

    The returned list should have the same length as s, where:
        - The first list element is True if s[0] is a lowercase vowel, and False otherwise
        - The second list element is True if s[1] is a lowercase vowel, and False otherwise
        - etc.

    A lowercase vowel is one of the five letters {'a', 'e', 'i', 'o', 'u'}.
    Note that uppercase vowels like 'A' are NOT the same as lowercase vowels.

    HINT: use a comprehension!

    >>> get_vowel_locations('hello')
    [False, True, False, False, True]
    >>> get_vowel_locations('india')
    [True, False, False, True, True]
    """
    vowel_lower = {'a', 'e', 'i', 'o', 'u'}
    return [x in vowel_lower for x in s]


def get_divisibility_dict(numbers: set, divisor: int) -> dict:
    """Return a dictionary mapping each number in numbers to whether it is divisible by divisor.

    You may ASSUME that:
      - divisor != 0

    >>> get_divisibility_dict({16, 20, 30}, 4) == {16: True, 20: True, 30: False}
    True
    >>> get_divisibility_dict({28, 63, 93}, 7) == {28: True, 63: True, 93: False}
    True
    """
    return {x: x % divisor == 0 for x in numbers}


###################################################################################################
# "Main block" (we'll discuss what this means in lecture)
###################################################################################################
if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True)

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (In PyCharm, select the lines below and press Ctrl/Cmd + / to toggle comments.)
    import python_ta

    python_ta.check_all(config={
        'extra-imports': ['math'],
        'max-line-length': 120
    })
