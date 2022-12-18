"""Lecture 11 Worksheet - Tom"""
from dataclasses import dataclass
from python_ta.contracts import check_contracts
import datetime


@dataclass
class Person:
    """A custom data type that represents data for a person.

    Representation Invariants:
        - self.age >= 0
    """
    given_name: str
    family_name: str
    age: int
    address: str


@dataclass
class Student:
    """A student at the University of Toronto.

    Representation Invariants:
        - len(self.given_name + self.family_name) != 0
        - self.year_of_study >= 1
        - len(self.utorid) != 0
        - str.isalnum(self.utorid)

        - others?
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

    """
    president: Student
    vice_president: Student
    events: list[str]



@check_contracts
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
    # From before
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
    # From before
    # return all({row[2] >= num for row in data if row[1] == civic_centre})

    return all({row.num_licenses >= num for row in data if row.civic_centre == civic_centre})


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
    return sum([row.num_licenses for row in data if row.civic_centre == civic_centre])


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

if __name__ == '__main__':
    import python_ta.contracts
    python_ta.contracts.check_all_contracts()

    data = create_small_sample_data()
    marriage_data = [MarriageData(row[0], row[1], row[2], row[3]) for row in data]

    m = MarriageData(1662, 'NY', 150, datetime.date(2011, 2, 1))
    # self.civic_centre in {'TO', 'NY', 'ET', 'SC'}
    # self.num_licenses >= 0
