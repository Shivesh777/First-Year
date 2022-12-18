"""CSC110 Fall 2020 Prep 4: Programming Exercises

Instructions (READ THIS FIRST!)
===============================

This Python module contains several function headers and descriptions.
Your task is to complete this module by doing the following for EACH function below:

1. Implement the function so that it does what its description claims.

You do *not* need to add new doctests or preconditions (and in fact
you should *not* add any preconditions!).

We have marked each place you need to write code with the word "TODO".
As you complete your work in this file, delete each TODO comment---this is a
good habit to get into early!

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2020 David Liu and Mario Badr.
"""
from dataclasses import dataclass


@dataclass
class Person:
    """A person with some basic demographic information.
    """
    given_name: str
    family_name: str
    age: int
    address: str


def greet_person(person: Person) -> str:
    """Return a greeting message for the given person.

    The message should have the form 'Hello, <given_name> <family_name>!'

    >>> david = Person('David', 'Liu', 110, '110 St. George Street')
    >>> greet_person(david)
    'Hello, David Liu!'
    """
    return "Hello, " + person.given_name + " " + person.family_name + "!"


def older_name(p1: Person, p2: Person) -> str:
    """Return the first name of the person who is older among p1 and p2.

    If p1 and p2 have the same age, return the name of p1.

    >>> david = Person('David', 'Liu', 110, '110 St. George Street')
    >>> mario = Person('Mario', 'Badr', 111, '111 St. George Street')
    >>> older_name(david, mario)
    'Mario'
    """
    if p1.age == p2.age:
        return p1.given_name
    elif p1.age > p2.age:
        return p1.given_name
    else:
        return p2.given_name


def average_age(people: list[Person]) -> float:
    """Return the average age of the people in people.

    Preconditions:
      - people != []

    >>> david = Person('David', 'Liu', 110, '110 St. George Street')
    >>> mario = Person('Mario', 'Badr', 111, '111 St. George Street')
    >>> example_people = [david, mario]
    >>> average_age(example_people)
    110.5
    """
    return sum(p.age for p in people) / len(people)


@dataclass
class Group:
    """A class representing a group of people.

    Its attributes are the group name and a list of the people in the group.
    """
    name: str
    members: list[Person]


def member_names(group: Group) -> list[str]:
    """Return the given names of the members of the given group.

    The names appear in the same order of the members in the group.

    >>> david = Person('David', 'Liu', 110, '110 St. George Street')
    >>> mario = Person('Mario', 'Badr', 111, '111 St. George Street')
    >>> cool_profs = Group('Cool Profs', [david, mario])
    >>> member_names(cool_profs)
    ['David', 'Mario']
    """
    return [x.given_name for x in group.members]


if __name__ == '__main__':
    import python_ta.contracts
    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest
    doctest.testmod(verbose=True)

    import python_ta
    python_ta.check_all(config={
        'extra-imports': ['python_ta.contracts', 'dataclasses'],
        'max-line-length': 100,
        'disable': ['R1705']
    })
