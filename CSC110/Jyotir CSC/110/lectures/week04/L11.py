"""CSC110 Lecture 11 - Starter file

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.
"""
from dataclasses import dataclass
import datetime


####################################################################################################
# Exercise 2
####################################################################################################
@dataclass
class Student:
    """A student at the University of Toronto.

    Representation Invariants:









    """
    given_name: str
    family_name: str
    year_of_study: int
    utorid: str


@dataclass
class Cssu:
    """The Computer Science Student Union at the University of Toronto.

    Instance Attributes:
        - execs: A mapping from executive role (president, treasurer, etc.)
                 to Student.
        - merch: A mapping from clothing item (t-shirt, hoodie, etc.)
                 to price.

    Representation Invariants:











    """
    execs: dict[str, Student]
    merch: dict[str, float]


####################################################################################################
# Exercise 3
####################################################################################################
@dataclass
class MarriageData:
    """TODO"""
    id: int
    civic_centre: str
    num_licenses: int
    month: datetime.date


def civic_centres(data: list[MarriageData]) -> set[str]:
    """Return a set of all the civic centres found in data.
    """
    return {marriage.civic_centre for marriage in data}


def civic_centre_meets_threshold(data: list[MarriageData], civic_centre: str,
                                 num: int) -> bool:
    """Return whether civic_centre issued at least num marriage licences every
    month.

    You only need to worry about the rows that appear in data; don't worry about
    "missing" months.

    Preconditions:
        - civic_centre in {'TO', 'NY', ET'', 'SC'}

    HINT: you'll need to use a list comprehension with a filter.
    """
    print(all([marriage.num_licenses >= num for marriage in data if marriage.civic_centre == civic_centre]))


def issued_licenses_in_range(data: list[MarriageData], start: datetime.date,
                             end: datetime.date) -> int:
    """Return the number of marriage licenses issued between start and end,
    inclusive.

    Preconditions:
        - end > start

    HINT: You can use <, <=, >, and >= to compare date values chronologically.
    """


####################################################################################################
# Sample data for Exercise 3
####################################################################################################
# marriage_data = [
#     MarriageData(1657, 'ET', 80, datetime.date(2011, 1, 1)),
#     MarriageData(1658, 'NY', 136, datetime.date(2011, 1, 1)),
#     MarriageData(1659, 'SC', 159, datetime.date(2011, 1, 1)),
    MarriageData(1660, 'TO', 367, datetime.date(2011, 1, 1)),
#     MarriageData(1661, 'ET', 109, datetime.date(2011, 2, 1)),
#     MarriageData(1662, 'NY', 150, datetime.date(2011, 2, 1)),
#     MarriageData(1663, 'SC', 154, datetime.date(2011, 2, 1)),
#     MarriageData(1664, 'TO', 383, datetime.date(2011, 2, 1))
#     ]
