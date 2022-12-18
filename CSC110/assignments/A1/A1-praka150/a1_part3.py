"""CSC110 Fall 2022 Assignment 1, Part 3: Interpreting Test Results

Instructions (READ THIS FIRST!)
===============================

This Python module contains the program and tests described in Part 3.
You can run this file as given to see the pytest report given in the handout.
Your task is to fix all errors in this file so that each test passes
(see assignment handout for details).

NOTE: We are *not* checking this file with PythonTA, since you will only
be making very small changes to the file.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2022 David Liu, Mario Badr, Tom Fairgrieve,
and Angela Zavaleta Bernuy
"""


###############################################################################
# David and Tom's program
###############################################################################
def get_largest_bill(bills: list) -> float:
    """Return the highest bill amount paid by a customer, rounded to two decimal places.

    Each element of bills is a dictionary with two key-value pairs:

    - key 'food', which corresponds to the total menu price of the food and drink
      that the customer ordered
    - key 'songs', which corresponds to the number of songs the customer sang

    You may ASSUME that:
        - bills is non-empty
        - every element of bills is a dictionary with the format described above
        - all menu totals and number of songs are >= 0
    """
    return max([calculate_total_cost(bill['food'], bill['songs']) for bill in bills])


def calculate_total_cost(menu_amount: float, songs: int) -> float:
    """Return the total cost for the given bill, rounded to two decimal places.

    You may ASSUME that:
    - menu_amount >= 0 and songs >= 0
    """
    tax_amount = menu_amount * 0.13
    tip_amount = menu_amount * 0.08
    song_amount = songs * 5

    return round(menu_amount + tax_amount + tip_amount + song_amount, 2)


###############################################################################
# Tests for get_largest_bill
###############################################################################
def test_single_bill() -> None:
    """Test get_largest_bill when there's only one customer.
    """
    bills = [{'food': 10.0, 'songs': 10}]

    expected = 62.1
    actual = get_largest_bill(bills)
    assert actual == expected


def test_two_customers() -> None:
    """Test get_largest_bill when there are two different bills.
    """
    bills = [
        {'food': 15.0, 'songs': 3},
        {'food': 16.2, 'songs': 2}
    ]

    expected = 33.15
    actual = get_largest_bill(bills)
    assert actual == expected


def test_just_food() -> None:
    """Test get_largest_bill when the customers only ordered food and drink, but no songs.
    """
    bills = [
        {'food': 10.0, 'songs': 0},
        {'food': 17.3, 'songs': 0},
        {'food': 21.25, 'songs': 0},
        {'food': 3.1, 'songs': 0},
        {'food': 0.0, 'songs': 0}]

    expected = 25.71
    actual = get_largest_bill(bills)
    assert actual == expected


if __name__ == '__main__':
    import pytest
    pytest.main(['a1_part3.py', '--no-header', '-v'])
