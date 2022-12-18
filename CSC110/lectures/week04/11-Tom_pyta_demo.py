"""Lecture 11 PyTA demo - Tom"""

# run this and the evaluate
# >>> t = Person('T', 'F', -42, '40 St. George') 
# in the console.  Draw conclusions from the observations.

from dataclasses import dataclass
from python_ta.contracts import check_contracts
import datetime


@check_contracts
@dataclass
class Person:
    """A custom data type that represents data for a person.

    Representation Invariants:
        - self.age >= 0

    >>> mario = Person('Mario', 'Badr', 12, '40 St. George')
    """
    given_name: str
    family_name: str
    age: int
    address: str
