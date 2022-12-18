"""David's Lecture 4 Examples"""


def square(x: float) -> float:
    """Return x squared.

    >>> square(3.0)
    9.0
    >>> square(2.5)
    6.25
    """
    x_squared = x ** 2
    return x_squared


def calculate_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """Return the distance between points (x1, y1) and (x2, y2),
    rounded to 1 decimal place.

    >>> calculate_distance(0.0, 0.0, 3.0, 4.0)
    5.0
    >>> calculate_distance(1.0, 0.0, 3.0, 4.0)
    4.5
    """
    dx_squared = (x2 - x1) ** 2
    dy_squared = (y2 - y1) ** 2
    exact_distance = (dx_squared + dy_squared) ** 0.5
    return round(exact_distance, 1)


# Exercise 2: The Function Design Recipe
# Q1 (note the use of the word "whether")
def is_same_length(list1: list, list2: list) -> bool:
    """Return whether list1 and list2 contain the same number of elements.

    >>> is_same_length([1, 2, 3], [4, 5, 6])
    True
    >>> is_same_length([1, 2, 3], [])
    False
    """
    return len(list1) == len(list2)


# Q2 (your parameter names, description might be different, and that's okay!)
def after_tax_cost(price: float, tax_rate: float) -> float:
    """Return the after-tax cost for the given price,
    rounded to two decimal places.

    >>> after_tax_cost(5.0, 0.01)
    5.05
    >>> after_tax_cost(5.0, 0.1)
    5.5
    """
    return round(price * (1 + tax_rate), 2)


# Q3 (many things might be different, and that's okay!)
def total_after_tax_cost(prices: list, tax_rate: float) -> float:
    """Return the total after-tax cost for all given prices,
    rounded to two decimal places. (Ignores rounding errors.)

    >>> total_after_tax_cost([2.0, 3.0], 0.01)
    5.05
    """
    # This solution follows two steps (and I've broken it down into two lines of code
    # to make that super clear).
    #
    # 1. Calculate all of the after-tax prices (this is a "collection transformation",
    #    perfect for a comprehension).
    # 2. Calculate the sum of all the after-tax prices (good review of a built-in Python function!).

    # Could do this...
    # after_tax_prices = [round(price * (1 + tax_rate), 2) for price in prices]

    # Or reuse the function we defined in Question 2!
    after_tax_prices = [after_tax_cost(price, tax_rate) for price in prices]
    return sum(after_tax_prices)


# Exercise 3, Q3
def convert_to_uppercase(strings: list) -> list:
    """Return a new list with the strings in the input list each converted to uppercase.

    >>> convert_to_uppercase(['David', 'Tom', 'cool'])
    ['DAVID', 'TOM', 'COOL']
    """
    return [str.upper(s) for s in strings]
