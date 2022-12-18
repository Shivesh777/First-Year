"""Lecture 11 examples"""
from dataclasses import dataclass
from python_ta.contracts import check_contracts
import datetime


# NOTE: I said in lecture that the @check_contracts decorator could go above or below
# the @dataclass decorator, but this was incorrect! The @check_contracs decorator must
# go ABOVE the @dataclass in order to get it to check the class representation invariants.
# (That's a bug in PythonTA that hopefully will be fixed next year!)
@check_contracts
@dataclass
class Person:
    """A person with some basic demographic information.

    Representation Invariants:
      - self.age >= 0
    """
    given_name: str
    family_name: str
    age: int
    address: str


@dataclass
class MarriageRow:
    """A custom data type for representing one row of information in
    the marriage license dataset from last lecture.

    Instance Attributes:                              --- NOTE: Add this when writing the docstring!
      - id: a unique identifier for the record
      - civic_centre: the name of the civic centre
      - num_licenses: the number of licenses issued
      - month: the month these licenses were issued

    Representation Invariants:

    - self.civic_centre in {'ET', 'NY', 'SC', 'TO'}
    - self.num_licenses >= 0

    # list version
    [1657, 'ET', 80, datetime.date(2011, 1, 1)]

    >>> MarriageRow(1657, 'ET', 80, datetime.date(2011, 1, 1))
    MarriageRow(id=1657, civic_centre='ET', num_licenses=80, month=datetime.date(2011, 1, 1))

    # Alternate example format (recommended):

    >>> row = MarriageRow(1657, 'ET', 80, datetime.date(2011, 1, 1))
    >>> row.id
    1657
    >>> row.civic_centre
    'ET'
    >>> row.num_licenses
    80
    >>> row.month
    datetime.date(2011, 1, 1)
    """
    id: int
    civic_centre: str
    num_licenses: int
    month: datetime.date


# Exercise 1
@dataclass
class FoodContainer:
    """A container that can store different foods."""
    label: str
    contents: list[str]


def num_contents(food_containers: list[FoodContainer]) -> int:
    """Return the total number of items contained in the given food_containers.

    >>> container1 = FoodContainer('David', ['ham', 'cheese', 'chocolate'])
    >>> container2 = FoodContainer('Tom', ['sushi', 'chips'])
    >>> num_contents([container1, container2])
    5
    """
    all_lengths = [len(container.contents) for container in food_containers]
    return sum(all_lengths)


# Exercise 2
@check_contracts
@dataclass
class Student:
    """A student at the University of Toronto.

    Representation Invariants:

        - # Some possibilities for year_of_study
        - self.year_of_study >= 1   # year of study is at least 1
        - 1 <= self.year_of_study <= 4
        - self.year_of_study in range(1, 5)  # in [1, 2, 3, 4]

        - # Some possibilities for utorid
        - self.utorid != ''         # UTORid can't be blank
        - str.isalnum(self.utorid)  # UTORid must be alphanumeric

        - # Some possibilities for names (but this makes some assumptions about the format of names!)
        - self.given_name != ''     # Given name can't be blank
        - self.family_name != ''    # Family name can't be blank
    """
    given_name: str
    family_name: str
    year_of_study: int
    utorid: str


@check_contracts
@dataclass
class Cssu:
    """The Computer Science Student Union at the University of Toronto.

    Instance Attributes:
        - president: The Student who is the president
        - vice_president: The Student who is vice-president
        - events: The names of events that the CSSU holds throughout the year

    Representation Invariants:
        - self.president.year_of_study in {3, 4}
        - self.president.year_of_study >= 3


        - (self.president).given_name != (self.vice_president).given_name
        - self.president != self.vice_president


        - all({event != '' and str.isalpha(event) for event in self.events})


    """
    president: Student
    vice_president: Student
    events: list[str]


# Exercise 3
@dataclass
class MarriageData:
    """A record of the number of marriage licenses issued in a civic centre
    in a given month.

    Instance Attributes:
      - id: a unique identifier for the record
      - civic_centre: the name of the civic centre
      - num_licenses: the number of licenses issued
      - month: the month these licenses were issued
    """
    id: int
    civic_centre: str
    num_licenses: int
    month: datetime.date  # Make sure to "import datetime"


def civic_centres(data: list[MarriageData]) -> set[str]:
    """Return a set of all the civic centres found in data.
    """
    # Tabular data version (from last week)
    # return {row[1] for row in data}

    return {row.civic_centre for row in data}


def civic_centre_meets_threshold(data: list[MarriageData], civic_centre: str,
                                 num: int) -> bool:
    """Return whether civic_centre issued at least num marriage licences every
    month.

    You only need to worry about the rows that appear in data; don't worry about
    "missing" months.

    Preconditions:
        - civic_centre in {'TO', 'NY', 'ET', 'SC'}

    HINT: you'll need to use a filtering comprehension.
    """
    # Tabular data version (from last week)
    # return all({row[2] > num for row in data if row[1] == civic_centre})

    return all({row.num_licenses > num for row in data if row.civic_centre == civic_centre})


def summarize_licences_by_centre(data: list[MarriageData]) -> dict[str, int]:
    """Return the total number of licences issued by each civic centre in <data>.

    Returns a dictionary where keys are civic centre names and values are the
    total number of licences issued by that civic centre.

    HINT: you will find it useful to write a function that calculates the total
    number of licences issued for a given civic centre as a parameter,
    e.g. total_licenses_for_centre(data, civic_centre).
    """
    all_civic_centres = civic_centres(data)

    return {civic_centre: total_licenses(data, civic_centre) for civic_centre in all_civic_centres}


def total_licenses(data: list[MarriageData], civic_centre: str) -> int:
    """Return the total number of licenses issued by civic centre."""
    # Tabular data version (from last week)
    # return sum([row[2] for row in data if row[1] == civic_centre])

    return sum([row.num_licenses for row in data if row.civic_centre == civic_centre])
