"""CSC110 Fall 2022 Assignment 1, Part 4: Colour Rows

Instructions (READ THIS FIRST!)
===============================

Please follow the instructions in the assignment handout to complete this file.

Note that unlike Part 2, you only need to complete the function bodies.
You are not required to add more doctest examples, though you may do so to help
with your own understanding/testing.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2022 David Liu, Tom Fairgrieve, Angela Zavaleta Bernuy.
"""
import a1_helpers


###################################################################################################
# 0. Warmup
###################################################################################################
def warmup_part4() -> None:
    """Visualize an example colour row using pygame.

    This function illustrates the use of the helper function a1_helpers.show_colours_pygame
    that we have provided you. We encourage you to use that function to visualize your
    work on the various questions in this part of the assignment!
    """
    example_colours = [[0, 255, 200], [1, 2, 3], [100, 100, 100], [181, 57, 173], [33, 0, 197]]
    a1_helpers.show_colours_pygame(example_colours)


###################################################################################################
# 1. Cropping colour rows
###################################################################################################
def crop_row(colour_row: list, start: int, num_colours: int) -> list:
    """Return a colour row containing the specified colours from the given colour_row.

    Notes:
    1. start is the index of the first colour to take from colour_row.
    2. num_colours specifies the number of colours to take from colour_row.
        If num_colours == 0, no colours are taken (and an empty list is returned)

    You may ASSUME that:
    - colour_row is a valid colour row (i.e., is a list of RGB tuples)
    - start >= 0
    - num_colours >= 0
    - start + num_colours <= len(colour_row)

    >>> example_colours = [[0, 255, 200], [1, 2, 3], [100, 100, 100], [181, 57, 173], [33, 0, 197]]
    >>> crop_row(example_colours, 1, 2)  # Take two colours from example_colours starting at index 1
    [[1, 2, 3], [100, 100, 100]]
    """
    return [colour_row[x] for x in range(start, start + num_colours)]


def crop_row_border_single(colour_row: list) -> list:
    """Return a colour row with the colours from the given colour_row, except with the first and last colour removed.

    You may ASSUME that:
    - colour_row is a valid colour row (i.e., is a list of RGB tuples)
    - len(colour_row) >= 2

    >>> example_colours = [[0, 255, 200], [1, 2, 3], [100, 100, 100], [181, 57, 173], [33, 0, 197]]
    >>> crop_row_border_single(example_colours)
    [[1, 2, 3], [100, 100, 100], [181, 57, 173]]

    You may implement this function by using a list comprehension OR by calling crop_row
    with the appropriate arguments. (For extra practice, try both ways!)
    """
    return [colour_row[x] for x in range(1, len(colour_row) - 1)]


def crop_row_border_multiple(colour_row: list, border_size: int) -> list:
    """Return a colour row with the colours from the given colour_row, except with
    the first and last border_size colours removed.

    Note: when border_size == 1, this function does the same thing as crop_row_border_single.

    You may ASSUME that:
    - colour_row is a valid colour row (i.e., is a list of RGB tuples)
    - 1 <= border_size <= len(colour_row) // 2

    >>> example_colours = [[0, 255, 200], [1, 2, 3], [100, 100, 100], [181, 57, 173], [33, 0, 197]]
    >>> crop_row_border_multiple(example_colours, 1)  # Remove the first and last colours
    [[1, 2, 3], [100, 100, 100], [181, 57, 173]]
    >>> crop_row_border_multiple(example_colours, 2)  # Remove the first 2 and last 2 colours
    [[100, 100, 100]]

    You may implement this function by using a list comprehension OR by calling crop_row
    with the appropriate arguments. (For extra practice, try both ways!)
    """
    return [colour_row[x] for x in range(border_size, len(colour_row) - border_size)]


###################################################################################################
# 2. Changing colours (reds)
###################################################################################################
def remove_red_in_row(colour_row: list) -> list:
    """Return a new colour row consisting of the same colours as the given row, except each colour
    has its "red" value changed to 0.

    >>> example_colours = [[0, 255, 200], [1, 2, 3], [100, 100, 100], [181, 57, 173], [33, 0, 197]]
    >>> remove_red_in_row(example_colours)
    [[0, 255, 200], [0, 2, 3], [0, 100, 100], [0, 57, 173], [0, 0, 197]]
    """
    return [[0, x[1], x[2]] for x in colour_row]


def fade_red_in_row(colour_row: list) -> list:
    """Return a new colour row consisting of the same colours as the given row, except each colour
    has its "red" value multiplied by 0.25 and rounded to the nearest integer.

    You may ASSUME that:
    - colour_row is a valid colour row (i.e., is a list of RGB tuples)

    >>> example_colours = [[0, 255, 200], [1, 2, 3], [100, 100, 100], [181, 57, 173], [33, 0, 197]]
    >>> fade_red_in_row(example_colours)
    [[0, 255, 200], [0, 2, 3], [25, 100, 100], [45, 57, 173], [8, 0, 197]]
    """
    return [[round(x[0] * 0.25), x[1], x[2]] for x in colour_row]


###################################################################################################
# 3. Changing colours (fade and blur)
###################################################################################################
def fade_row(colour_row: list) -> list:
    """Return a new colour row consisting of the colours in the given row, with each faded by an
    amount corresponding to its index.

    We perform a *fade* on the colour tuple at index i by multiplying each of its int values
    by (i / len(colour_row)) and then rounding to the nearest integer.
    So for example, if len(colour_row) == 5:

    - colour_row[0] has each of its colour values multipled by 0 / 5 = 0.0, so you always get [0, 0, 0]
    - colour_row[1] has each of its colour values multipled by 1 / 5 = 0.2 and then rounded
    - colour_row[4] has each of its colour values multiplied 4 / 5 = 0.8 and then rounded

    You may ASSUME that:
    - colour_row is a valid colour row (i.e., is a list of RGB tuples)

    >>> example_colours = [[0, 255, 200], [1, 2, 3], [100, 100, 100], [181, 57, 173], [33, 0, 197]]
    >>> fade_row(example_colours)
    [[0, 0, 0], [0, 0, 1], [40, 40, 40], [109, 34, 104], [26, 0, 158]]
    """
    return [[round(colour_row[i][j] * i / len(colour_row)) for j in range(3)] for i in range(len(colour_row))]


def avg_colours(clr1: list, clr2: list, clr3: list) -> list:
    """Returns a list of the average of three colours.

    >>> example_colours = [[0, 255, 200], [1, 2, 3], [100, 100, 100]]
    >>> avg_colours(example_colours[0], example_colours[1], example_colours[2])
    [34, 119, 101]"""
    return [round(sum([clr1[j], clr2[j], clr3[j]]) / 3) for j in range(3)]


def blur_row(colour_row: list) -> list:
    """Return a new colour row consisting of the colours in the given row blurred together.

    We perform a *blur* on the colour tuple at index i by taking the average of the colour values
    at indexes i - 1, i, and i + 1, rounding to the nearest integer.

    For simplicity, we ignore the first and last colours in the row, and the returned list has length *2 less*
    than the original row.

    You may ASSUME that:
    - colour_row is a valid colour row (i.e., is a list of RGB tuples)
    - len(colour_row) >= 2

    >>> example_colours = [[0, 255, 200], [1, 2, 3], [100, 100, 100], [181, 57, 173], [33, 0, 197]]
    >>> blur_row(example_colours)
    [[34, 119, 101], [94, 53, 92], [105, 52, 157]]

    Hints:
        - Because you are dropping the first and last colours in the row, you can use a similar
          approach as crop_row_border_single.
        - You may find it helpful to first define a new function that takes three colours and
          returns their average, and then use that function here. But there are many other approaches
          you can take as well!
        - Even if you get stuck, you can move onto Part 5 and come back to this function later.
    """
    return [avg_colours(colour_row[i - 1], colour_row[i], colour_row[i + 1]) for i in range(1, len(colour_row) - 1)]


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
        'extra-imports': ['a1_helpers'],
        'max-line-length': 120
    })
