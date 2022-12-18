"""CSC110 Lecture 10 - Starter file

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.
"""
import datetime


####################################################################################################
# Sample data from the actual dataset
####################################################################################################
def create_small_sample_data() -> list[list]:
    """Return a small sample of the marriage data dataset."""
    return [
        [1657, 'ET', 80, datetime.date(2011, 1, 1)],
        [1658, 'NY', 136, datetime.date(2011, 1, 1)],
        [1659, 'SC', 159, datetime.date(2011, 1, 1)],
        [1660, 'TO', 367, datetime.date(2011, 1, 1)],
        [1661, 'ET', 109, datetime.date(2011, 2, 1)],
        [1662, 'NY', 150, datetime.date(2011, 2, 1)],
        [1663, 'SC', 154, datetime.date(2011, 2, 1)],
        [1664, 'TO', 383, datetime.date(2011, 2, 1)]
    ]


def create_large_sample_data() -> list[list]:
    """Return a large sample of the marriage data dataset."""
    return [
        [1657, 'ET', 80, datetime.date(2011, 1, 1)],
        [1658, 'NY', 136, datetime.date(2011, 1, 1)],
        [1659, 'SC', 159, datetime.date(2011, 1, 1)],
        [1660, 'TO', 367, datetime.date(2011, 1, 1)],
        [1661, 'ET', 109, datetime.date(2011, 2, 1)],
        [1662, 'NY', 150, datetime.date(2011, 2, 1)],
        [1663, 'SC', 154, datetime.date(2011, 2, 1)],
        [1664, 'TO', 383, datetime.date(2011, 2, 1)],
        [1665, 'ET', 177, datetime.date(2011, 3, 1)],
        [1666, 'NY', 231, datetime.date(2011, 3, 1)],
        [1667, 'SC', 213, datetime.date(2011, 3, 1)],
        [1668, 'TO', 589, datetime.date(2011, 3, 1)],
        [1669, 'ET', 178, datetime.date(2011, 4, 1)],
        [1670, 'NY', 277, datetime.date(2011, 4, 1)],
        [1671, 'SC', 261, datetime.date(2011, 4, 1)],
        [1672, 'TO', 660, datetime.date(2011, 4, 1)],
        [1673, 'ET', 263, datetime.date(2011, 5, 1)],
        [1674, 'NY', 376, datetime.date(2011, 5, 1)],
        [1675, 'SC', 375, datetime.date(2011, 5, 1)],
        [1676, 'TO', 871, datetime.date(2011, 5, 1)],
        [1677, 'ET', 255, datetime.date(2011, 6, 1)],
        [1678, 'NY', 365, datetime.date(2011, 6, 1)],
        [1679, 'SC', 334, datetime.date(2011, 6, 1)],
        [1680, 'TO', 870, datetime.date(2011, 6, 1)],
        [1681, 'ET', 238, datetime.date(2011, 7, 1)],
        [1682, 'NY', 364, datetime.date(2011, 7, 1)],
        [1683, 'SC', 352, datetime.date(2011, 7, 1)],
        [1684, 'TO', 989, datetime.date(2011, 7, 1)],
        [1685, 'ET', 257, datetime.date(2011, 8, 1)],
        [1686, 'NY', 366, datetime.date(2011, 8, 1)],
        [1687, 'SC', 345, datetime.date(2011, 8, 1)],
        [1688, 'TO', 965, datetime.date(2011, 8, 1)],
        [1689, 'ET', 152, datetime.date(2011, 9, 1)],
        [1690, 'NY', 255, datetime.date(2011, 9, 1)],
        [1691, 'SC', 276, datetime.date(2011, 9, 1)],
        [1692, 'TO', 638, datetime.date(2011, 9, 1)],
        [1693, 'ET', 126, datetime.date(2011, 10, 1)],
        [1694, 'NY', 201, datetime.date(2011, 10, 1)],
        [1695, 'SC', 218, datetime.date(2011, 10, 1)],
        [1696, 'TO', 468, datetime.date(2011, 10, 1)],
        [1697, 'ET', 103, datetime.date(2011, 11, 1)],
        [1698, 'NY', 191, datetime.date(2011, 11, 1)],
        [1699, 'SC', 182, datetime.date(2011, 11, 1)],
        [1700, 'TO', 340, datetime.date(2011, 11, 1)],
        [1701, 'ET', 109, datetime.date(2011, 12, 1)],
        [1702, 'NY', 171, datetime.date(2011, 12, 1)],
        [1703, 'SC', 149, datetime.date(2011, 12, 1)],
        [1704, 'TO', 356, datetime.date(2011, 12, 1)]
    ]


####################################################################################################
# Exercise 2
####################################################################################################
####################################################################################################
# Exercise 3
####################################################################################################
def civic_centres(data: list[list]) -> set[str]:
    """Return a set of all the civic centres found in data.

    Preconditions:
        - data satisfies all of the properties described in Exercise 2
    """
    return {x[1] for x in data}


def civic_centre_meets_threshold(data: list[list], civic_centre: str, num: int) -> bool:
    """Return whether civic_centre issued at least num marriage licences every month.

    You only need to worry about the rows that appear in data; don't worry about "missing" months.

    Preconditions:
        - num > 0
        - data satisfies all of the properties described in Exercise 2
        - civic_centre in {'TO', 'NY', 'ET', 'SC'}

    HINT: you'll need to use a list comprehension with a filter.
    """


def summarize_licences_by_centre(data: list[list]) -> dict[str, int]:
    """Return the total number of licences issued by each civic centre in <data>.

    Returns a dictionary where keys are civic centre names and values are the
    total number of licences issued by that civic centre.

    Preconditions:
        - data satisfies all of the properties described in Exercise 2

    HINT: you will find it useful to write a function that calculates the total
    number of licences issued for a given civic centre as a parameter,
    e.g. total_licenses_for_centre(data, civic_centre).
    """


####################################################################################################
# Exercise 4
####################################################################################################
def issued_licences_by_year(data: list[list], year: int) -> int:
    """Return the total number of marriage licences issued in <year>.

    Preconditions:
        - data satisfies all of the properties described in Exercise 2
    """


def only_first_days(data: list[list]) -> bool:
    """Return whether every row's fourth element is a datetime.date whose <day> attribute is 1.

    Preconditions:
        - data satisfies all of the properties described in Exercise 2
    """


def issued_licenses_in_range(data: list[list], start: datetime.date, end: datetime.date) -> int:
    """Return the number of marriage licenses issued between start and end, inclusive.

    Preconditions:
        - data satisfies all of the properties described in Exercise 2
        - end > start

    HINT: You can use <, <=, >, and >= to compare date values chronologically.
    """
