"""Tom Lecture 14 examples"""
from dataclasses import dataclass
import datetime
from typing import Dict, List, Set


def squares(nums: List[int]) -> List[int]:
    """Return a list of the squares of the given numbers.

    >>> squares([1, 2, 3])
    [1, 4, 9]
    """
    # return [num ** 2 for num in nums] # This is from the slides
    return [num * num for num in nums]  # This is more similar to the other two versions


def squares_reassignment(nums: List[int]) -> List[int]:
    """Return a list of the squares of the given numbers."""
    squares_so_far = []

    for num in nums:
        squares_so_far = squares_so_far + [num ** 2]

    return squares_so_far


def squares_mutation(nums: List[int]) -> List[int]:
    """Return a list of the squares of the given numbers."""
    squares_so_far = []

    for num in nums:
        list.append(squares_so_far, num ** 2)

    return squares_so_far


def move_item(items: list, other_items: set) -> None:
    """Remove the first item from items and add it to other_items.

    Preconditions:
        - items != []


    >>> numbers_list = [1, 2, 3]
    >>> numbers_set = {10, 20}
    >>> move_item(numbers_list, numbers_set)
    >>> numbers_list
    [2, 3]
    >>> numbers_set == {1, 10, 20}
    True
    """
    first_item = list.pop(items, 0)
    set.add(other_items, first_item)

    # alternate, simplified solution
    # set.add(other_items, list.pop(items, 0))


@dataclass
class MarriageData:
    """A record of the number of marriage licenses issued in a civic centre
    in a given month.

    Instance Attributes:
      - id: a unique identifier for the record
      - civic_centre: the name of the civic centre
      - num_licenses: the number of licenses issued
      - month: the month these licenses were issued

    Representation Invariant omitted.
    """
    id: int
    civic_centre: str
    num_licenses: int
    month: datetime.date


def filter_by_name(data: List[MarriageData], civic_centre: str) -> List[MarriageData]:
    """Return all rows in data with the matching civic centre civic_centre.

    Equivalent to:
      [row for row in data if row.civic_centre == civic_centre]
    """
    rows_so_far = []

    for row in data:
        if row.civic_centre == civic_centre:
            list.append(rows_so_far, row)

    return rows_so_far


def num_issued_by(data: list[MarriageData], civic_centre: str) -> set[int]:
    """Return the unique numbers of marriage licenses issued in a month at the
    given civic_centre.

    Equivalent to:
      {row.num_licenses for row in data if row.civic_centre == civic_centre}
    """
    nums_so_far = set()

    for row in data:
        if row.civic_centre == civic_centre:
            set.add(nums_so_far, row.num_licenses)

    return nums_so_far


def marriages_by_centre(data: list[MarriageData], month: datetime.date) -> dict[str, int]:
    """Return a mapping from civic centre name to the number of marriage licenses
    issued by that centre in the given month.

    Preconditions:
        - Each civic centre has only one row of MarriageData for the given month.

    Equivalent to:
        {row.civic_centre: row.num_licenses for row in data if row.month == month}
    """
    mapping_so_far = {}

    for row in data:
        if row.month == month:
            # Update the dictionary!
            mapping_so_far[row.civic_centre] = row.num_licenses

    return mapping_so_far


# Worked Example
def total_marriages_by_centre(data: List[MarriageData]) -> Dict[str, int]:
    """Return mapping from civic centre name to the total number of marriage licenses ever
    issued by that centre.
    """

    totals_so_far = {}
    for row in data:
        civic_centre = row.civic_centre
        num_licenses = row.num_licenses
        # Incorrect - it requires civic_centre to already be a key in the dict
        # totals_so_far[civic_centre] = totals_so_far[civic_centre] + num_licenses
        if civic_centre in totals_so_far:
            totals_so_far[civic_centre ] += num_licenses
        else:
            totals_so_far[civic_centre] = num_licenses

        # slightly simpler alternate
        # if civic_centre not in totals_so_far:
        #     totals_so_far[civic_centre] = 0
        # totals_so_far[civic_centre] += num_licenses
    return totals_so_far

if __name__ == '__main__':
    import doctest
    doctest.testmod()
