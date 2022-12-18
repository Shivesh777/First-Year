"""Tom's Lecture 4 Examples"""


def fahrenheit_to_celsius(deg_f: float) -> float:
    """Return the celsius temperature corresponding to the fahrenheit measure deg_f.

    >>> fahrenheit_to_celsius(80.0)
    26.666666666666668
    >>> fahrenheit_to_celsius(0.0)
    -17.77777777777778
    """
    return (deg_f - 32) * 5 / 9


# we developed the distance function by following the Function Design Recipe
#   a few typos were made along the way - the corresponding error messages
#   appear in the log
def distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """Return the distance between (x1, y1) and (x2, y2).

    >>> distance(0.0, 0.0, 3.0, 4.0)
    5.0
    >>> distance(-5.0, 0.0, 0.0, -12.0)
    13.0
    """
    delta_x = x2 - x1
    delta_y = y2 - y1
    return (delta_x ** 2 + delta_y ** 2) ** 0.5


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


# Q2 (your parameter names, description and body might be different. That's okay!)
def after_tax_cost(price: float, tax_rate: float) -> float:
    """Return the after-tax cost for the given price and tax_rate, rounded to two decimal places.

    >>> after_tax_cost(5.0, 0.13)
    5.65
    >>> after_tax_cost(0.0, 0.05)
    0.0
    """
    return round(price * (1 + tax_rate), 2)


# Q3 (many things might be different, and that's okay!)
def total_after_tax_cost(prices: list, tax_rate: float) -> float:
    """Return the total after-tax cost for all given prices assuming tax_rate,
    rounded to two decimal places.

    >>> total_after_tax_cost([2.0, 3.0], 0.13)
    5.65
    >>> total_after_tax_cost([], 0.05)
    0.0
    """
    return round(after_tax_cost(sum(prices), tax_rate), 2)

    # Or,
    # return round(sum([after_tax_cost(price, tax_rate) for price in prices]), 2)

    # Or without using after_tax_cost at all
    # return round(sum(prices) * (1 + tax_rate), 2)


## Exercise 3: Practice with methods

# Q3
def convert_to_uppercase(strings: list) -> list:
    """Return a new list with the strings in the input list each converted to uppercase.

    >>> convert_to_uppercase(['David', 'Tom', 'cool'])
    ['DAVID', 'TOM', 'COOL']
    """
    return [str.upper(s) for s in strings]
