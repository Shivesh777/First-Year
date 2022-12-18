"""Tom's Lecture 12 examples"""


from dataclasses import dataclass
import datetime


@dataclass
class MarriageData:
    """..."""
    id: int
    civic_centre: str
    num_licenses: int
    month: datetime.date


def long_greeting(names: list[str]) -> str:
    """Return a greeting message that greets every person in names.

    Each greeting should have the form "Hello <name>! " (note the space at the end).
    The returned string should be the concatenation of all the greetings.

    >>> long_greeting(['David', 'Mario'])  # Note the "extra" space at the end
    'Hello David! Hello Mario! '
    """
    greet_so_far = ''
    for name in names:
        new_greeting = 'Hello ' + name + '! '
        greet_so_far = greet_so_far + new_greeting
        # greet_so_far += new_greeting
    return greet_so_far


def total_licenses_for_centre_v1(data: list[list], civic_centre: str) -> int:
    """Return how many marriage licenses were issued in the given civic centre."""
    return sum([row[2] for row in data if row[1] == civic_centre])

def total_licenses_for_centre_v2(data: list[MarriageData], civic_centre: str) -> int:
    """Return how many marriage licenses were issued in the given civic centre.

    Use a comprehension for this version.
    """
    return sum([row.num_licenses for row in data if row.civic_centre == civic_centre])

def total_licenses_for_centre_v3(data: list[MarriageData], civic_centre: str) -> int:
    """Return how many marriage licenses were issued in the given civic centre.

    Use a for loop for this version.
    """
    num_licenses_so_far = 0
    for row in data:
        if row.civic_centre == civic_centre:
            num_licenses_so_far = num_licenses_so_far + row.num_licenses
    return num_licenses_so_far

def civic_centre_meets_threshold_v1(data: list[list],
                                    civic_centre: str, num: int) -> bool:
    """Return whether civic_centre issued at least num marriage licences every month.

    You only need to worry about the rows that appear in data;
    don't worry about "missing" months.

    Preconditions:
        - num > 0
        - civic_centre in {'TO', 'NY', 'ET', 'SC'}
        - data satisfies all of the properties described in earlier lectures
    """
    licenses_issued = [row[2] for row in data if row[1] == civic_centre]
    return all({num_issued >= num for num_issued in licenses_issued})


def civic_centre_meets_threshold_v2(data: list[MarriageData],
                                    civic_centre: str, num: int) -> bool:
    """Return whether civic_centre issued at least num marriage licences every month.

    You only need to worry about the rows that appear in data;
    don't worry about "missing" months.

    Preconditions:
        - num > 0
        - civic_centre in {'TO', 'NY', 'ET', 'SC'}
        - data satisfies all of the properties described in earlier lectures

    Use a comprehension for this version.
    """

def civic_centre_meets_threshold_v3(data: list[MarriageData],
                                    civic_centre: str, num: int) -> bool:
    """Return whether civic_centre issued at least num marriage licences every month.

    You only need to worry about the rows that appear in data;
    don't worry about "missing" months.

    Preconditions:
        - num > 0
        - civic_centre in {'TO', 'NY', 'ET', 'SC'}

    Use a for loop for this version.
    """



def count_uppercase(s: str) -> int:
    """Return the number of uppercase letters in s.

    >>> count_uppercase('Mario')
    1
    >>> count_uppercase('lol')
    0
    """
    count_so_far = 0
    for char in s:
        if str.isupper(char):
            count_so_far = count_so_far + 1
        # alternate instead of if statement: 
        #count_so_far = count_so_far + str.isupper(char)
    return count_so_far


def all_fluffy(s: str) -> bool:
    """Return whether every character in s is fluffy.

    Fluffy characters are those that appear in the word 'fluffy'.

    >>> all_fluffy('fly')
    True
    >>> all_fluffy('fun')
    False
    """
    # wrong: returns after looking at first char in s
    #for char in s:
    #    if char not in 'fluffy':
    #        return False
    #    else:
    #        return True

    # wrong: since it returns the status of last char in s
    #fluffy_so_far = False
    #for char in s:
    #    if char not in 'fluffy':
    #        fluffy_so_far = False
    #    else:
    #        fluffy_so_far = True
    #return fluffy_so_far
    for char in s:
        if char not in 'fluffy':
            return False
    return True


def sum_davids(scores: dict[str, int]) -> int:
    """Return the sum of all values in scores that correspond to a key that
    contains 'David'.

    >>> sum_davids({'David Liu': 3, 'Mario Badr': 7, 'David Bowie': 5})
    8
    """
    sum_so_far = 0
    for key in scores:
        if 'David' in key:
            sum_so_far = sum_so_far + scores[key]
    return sum_so_far


def david_vs_mario(scores: dict[str, int]) -> str:
    """Return the name of the person with the highest total score in scores.

    David's score is the sum of all values in scores that correspond
    to a key that contains the string 'David'.

    Mario's score is the sum of all values in scores that correspond
    to a key that contains the string 'Mario'.

    If there is a tie, return 'David' (obviously).

    >>> david_vs_mario({'David L': 3, 'Mario B': 7, 'David B': 5, 'Super Mario': 12})
    'Mario'
    """
    david_total_so_far = 0
    mario_total_so_far = 0
    for name in scores:
        if 'David' in name:
            david_total_so_far = david_total_so_far + scores[name]
        elif 'Mario' in name:
            mario_total_so_far = mario_total_so_far + scores[name]
    if david_total_so_far >= mario_total_so_far:
        return 'David'
    else:
        return 'Mario'

if __name__ == '__main__':
    import doctest
    doctest.testmod()
