"""CSC110 Lecture 9 - Starter file

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.
"""


####################################################################################################
# Lecture Demo
####################################################################################################
def is_even(value: int) -> bool:
    """Return whether value is divisible by 2.

    >>> is_even(2)
    True
    >>> is_even(17)
    False
    """
    return value % 2 == 0


def num_evens(nums: list[int]) -> int:
    """Return the number of even elements in nums.

    >>> num_evens([1, 2, 3])
    1
    >>> num_evens([2, 4, 4])
    3
    """
    return len([n for n in nums if is_even(n)])


LOVES_TABLE = [
    [False, True, True, False],
    [False, True, True, True],
    [False, False, True, False],
    [False, False, True, True]
]

A = {
    'Breanna': 0,
    'Malena': 1,
    'Patrick': 2,
    'Ella': 3
}

B = {
    'Sophia': 0,
    'Thelonius': 1,
    'Stanley': 2,
    'Laura': 3,
}


def loves(a: str, b: str) -> bool:
    """Return whether the person at index a loves the person at index b.

    Preconditions:
      - a in A
      - b in B

    >>> loves('Breanna', 'Sophia')
    False
    """
    a_index = A[a]
    b_index = B[b]
    return LOVES_TABLE[a_index][b_index]


def loves_someone(a: str) -> bool:
    """Return whether a loves at least one person in B.

    Preconditions:
      - a in A
    """
    return any({loves(a, b) for b in B})


def loved_by_everyone(b: str) -> bool:
    """Return whether b is loved by everyone in A.

    Preconditions:
      - b in B
    """
    return all({loves(a, b)} for a in A)


####################################################################################################
# Exercise 1
####################################################################################################
def divides(d: int, n: int) -> bool:
    """Return whether d divides n."""
    possible_divisors = range(-abs(n), abs(n) + 1)
    return any({n == k * d for k in possible_divisors})


####################################################################################################
# Exercise 3
###################################################################################################
EMPLOYEES = [
    ('Aizah', 70000, 'Sales'),
    ('Betty', 25000, 'Sales'),
    ('Carlos', 50000, 'HR'),
    ('Doug', 40000, 'Sales'),
    ('Ellen', 60000, 'Design'),
    ('Flo', 30000, 'Design')
]


def is_rich(employee: tuple[str, int, str]) -> bool:
    """Return whether the employee is rich.

    An employee is rich if they earn more than $45,000.
    """
    return employee[1] > 45000


def same_department(employee1: tuple[str, int, str], employee2: tuple[str, int, str]) -> bool:
    """Return whether employee1 and employee2 are in the same department."""
    return employee1[2] == employee2[2]
