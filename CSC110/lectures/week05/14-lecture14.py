"""David Lecture 14 examples"""
from dataclasses import dataclass
import datetime


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
    removed_item = list.pop(items, 0)
    set.add(other_items, removed_item)

    # Alternate version
    # set.add(other_items, list.pop(items, 0))




def squares(nums: list[int]) -> list[int]:
    """Return a list of the squares of the given numbers.

    >>> squares([1, 2, 3])
    [1, 4, 9]
    """
    return [num ** 2 for num in nums]


def squares_reassignment(nums: list[int]) -> list[int]:
    """Return a list of the squares of the given numbers."""
    squares_so_far = []

    for num in nums:
        squares_so_far = squares_so_far + [num ** 2]

    return squares_so_far


def squares_mutation(nums: list[int]) -> list[int]:
    """Return a list of the squares of the given numbers."""
    squares_so_far = []

    for num in nums:
        list.append(squares_so_far, num ** 2)

    return squares_so_far


@dataclass
class MarriageData:
    """A record of the number of marriage licenses issued in a civic centre
    in a given month.

    Instance Attributes:
      - id: a unique identifier for the record
      - civic_centre: the name of the civic centre
      - num_licenses: the number of licenses issued
      - month: the month these licenses were issued

    Representation Invariants omitted.
    """
    id: int
    civic_centre: str
    num_licenses: int
    month: datetime.date


def filter_by_name(data: list[MarriageData], name: str) -> list[MarriageData]:
    """Return all rows in data with the matching civic centre <name>.

    Equivalent to:
      [row for row in data if row.civic_centre == name]
    """
    rows_so_far = []

    for row in data:
        if row.civic_centre == name:
            list.append(rows_so_far, row)

    return rows_so_far


def num_issued_by(data: list[MarriageData], civic_centre: str) -> set[int]:
    """Return the unique numbers of marriage licenses issued in a month at the
    given civic centre.

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


def total_marriages_by_centre(data: list[MarriageData]) -> dict[str, int]:
    """Return mapping from civic centre name to the total number of marriage licenses ever
    issued by that centre.
    """
    mapping_so_far = {}

    for row in data:
        name = row.civic_centre

        # Key idea: for each row in the data, if the row's civic centre is already in
        # the accumulator, increase the associated value by row.num_licenses.
        # But if the row's civic centre is NOT in the accumulator, add it to
        # the dict and set the initial value equal to row.num_licenses.
        if name in mapping_so_far:
            mapping_so_far[name] += row.num_licenses
        else:
            mapping_so_far[name] = row.num_licenses

    return mapping_so_far
