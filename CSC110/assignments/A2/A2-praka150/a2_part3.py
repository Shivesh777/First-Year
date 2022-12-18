"""CSC110 Fall 2022 Assignment 2, Part 3: Wordle!

Module Description
==================
This Python file contains the starter code for Part 3 of this assignment.
For more information, please see the assignment handout.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2022 David Liu, Tom Fairgrieve, and Angela Zavaleta Bernuy.
"""
from python_ta.contracts import check_contracts

from a2_wordle_helpers import ALL_STATUSES, INCORRECT, CORRECT, WRONG_POSITION, cartesian_product_general
import a2_visualizer


###################################################################################################
# Part 3(a)
###################################################################################################
@check_contracts
def is_correct_char(answer: str, guess: str, i: int) -> bool:
    """Return whether the character status of guess[i] with respect to answer is CORRECT.

    Preconditions:
    - len(answer) == len(guess)
    - 0 <= i < len(answer)

    >>> is_correct_char('teach', 'adieu', 3)
    False
    >>> is_correct_char('teaching', 'reacting', 1)
    True
    """
    return guess[i] == answer[i]


@check_contracts
def is_wrong_position_char(answer: str, guess: str, i: int) -> bool:
    """Return whether the character status of guess[i] with respect to answer is WRONG_POSITION.

    Preconditions:
    - len(answer) == len(guess)
    - 0 <= i < len(answer)

    >>> is_wrong_position_char('teach', 'adieu', 3)
    True
    >>> is_wrong_position_char('teaching', 'reacting', 1)
    False
    >>> # Cases with duplicate characters!
    >>> is_wrong_position_char('hello', 'hoops', 1)
    True
    >>> is_wrong_position_char('hello', 'hoops', 2)
    True
    """
    condition_1 = guess[i] != answer[i]
    condition_2 = any([j != i and guess[i] == answer[j] and guess[j] != answer[j] for j in range(0, len(guess))])
    return condition_1 and condition_2


@check_contracts
def is_incorrect_char(answer: str, guess: str, i: int) -> bool:
    """Return whether the character status of guess[i] with respect to answer is INCORRECT.

    Preconditions:
    - len(answer) == len(guess)
    - 0 <= i < len(answer)

    >>> is_incorrect_char('teach', 'adieu', 1)
    True
    >>> is_incorrect_char('teaching', 'reacting', 1)
    False
    >>> is_incorrect_char('hello', 'keeps', 2)
    True

    HINT: you can use the previous two status functions to implement this one.
    """
    return not (is_correct_char(answer, guess, i) or is_wrong_position_char(answer, guess, i))


@check_contracts
def get_character_status(answer: str, guess: str, i: int) -> str:
    """Return the character status of guess[i] with respect to answer.

    The return value is one of the three values {INCORRECT, WRONG_POSITION, CORRECT}.
    (These values are imported from the a2_helpers.py module for you already.)

    Preconditions:
    - len(answer) == len(guess)
    - 0 <= i < len(answer)

    >>> get_character_status('teach', 'adieu', 1) == INCORRECT
    True
    >>> get_character_status('teaching', 'reacting', 1) == CORRECT
    True
    """
    if is_correct_char(answer, guess, i):
        return CORRECT
    elif is_wrong_position_char(answer, guess, i):
        return WRONG_POSITION
    else:
        return INCORRECT


@check_contracts
def get_guess_status(answer: str, guess: str) -> list[str]:
    """Return the guess status of the given guess with respect to answer.

    The return value is a list with the same length as guess, whose
    elements are all in the set {INCORRECT, WRONG_POSITION, CORRECT}.

    Preconditions:
    - answer != ''
    - len(answer) == len(guess)

    >>> example_status = get_guess_status('teach', 'adieu')
    >>> example_status == [WRONG_POSITION, INCORRECT, INCORRECT, WRONG_POSITION, INCORRECT]
    True
    """
    return [get_character_status(answer, guess, i) for i in range(0, len(answer))]


@check_contracts
def get_guesses_statuses(answer: str, guesses: list[str]) -> list[list[str]]:
    """Return the guess statuses of each given guess with respect to answer.

    The return value is a list with the same length as guesses, where each status has
    elements that are all in the set {INCORRECT, WRONG_POSITION, CORRECT}.

    Preconditions:
    - answer != ''
    - all({len(answer) == len(guess) for guess in guesses})

    >>> example_statuses = get_guesses_statuses('teach', ['adieu'])
    >>> example_statuses == [[WRONG_POSITION, INCORRECT, INCORRECT, WRONG_POSITION, INCORRECT]]
    True
    """
    return [get_guess_status(answer, guess) for guess in guesses]


@check_contracts
def part3a_example(answer: str, guesses: list[str]) -> None:
    """Visualize the Wordle game for the given answer and guesses.

    Complete this function in two steps:

    1. First, use your get_guesses_statuses function to compute the statuses of each given guess.
    2. Then, call a2_visualizer.draw_wordle to display the result! (You will need to read
       the docstring of that function, in a2_visualizer.py, to understand how to use it.)

    NOTE: You do *NOT* need a return statement in this function. The return type annotation
    is "None", which is a special annotation meaning this function doesn't return anything.
    When you call this function in the Python console, you should see a Pygame window appear,
    like in some of the examples in Assignment 1. But after you close the Pygame window, nothing
    should display in the Python console, since this function doesn't return anything.
    """
    statuses = get_guesses_statuses(answer, guesses)
    a2_visualizer.draw_wordle(answer, guesses, statuses)


###################################################################################################
# Part 3(b)
###################################################################################################
@check_contracts
def is_correct_single(word: str, guess: str, status: list[str]) -> bool:
    """Return whether the given word is a correct answer for the given guess and status.

    Preconditions:
    - len(word) == len(guess) == len(status)
    - _is_valid_status(status)
    - word != ''

    Note: the second precondition makes uses of a helper function at the bottom of this file,
    which checks that a guess status consists only of the elements {INCORRECT, WRONG_POSITION, CORRECT}.

    >>> is_correct_single('later', 'tower', [WRONG_POSITION, INCORRECT, INCORRECT, CORRECT, CORRECT])
    True
    >>> is_correct_single('later', 'tower', [INCORRECT] * 5)
    False
    """
    return get_guess_status(word, guess) == status


@check_contracts
def is_correct_multiple(word: str, guesses: list[str], statuses: list[list[str]]) -> bool:
    """Return whether the given word is a correct answer for the given guesses and statuses.

    Preconditions:
    - len(guesses) == len(statuses)
    - all({len(word) == len(guess) for guess in guesses})
    - all({len(word) == len(status) for status in statuses})
    - all({_is_valid_status(status) for status in statuses})
    - word != ''

    >>> example_guesses = ['tower', 'lower', 'power', 'round']
    >>> example_statuses = [
    ...     [WRONG_POSITION, INCORRECT, INCORRECT, CORRECT, CORRECT],
    ...     [CORRECT, INCORRECT, INCORRECT, CORRECT, CORRECT],
    ...     [INCORRECT, INCORRECT, INCORRECT, CORRECT, CORRECT],
    ...     [WRONG_POSITION, INCORRECT, INCORRECT, INCORRECT, INCORRECT]
    ... ]
    >>> is_correct_multiple('later', example_guesses, example_statuses)
    True
    """
    return all([is_correct_single(word, guesses[x], statuses[x]) for x in range(0, len(guesses))])


@check_contracts
def find_correct_answers(word_set: set[str],
                         guesses: list[str], statuses: list[list[str]]) -> list[str]:
    """Return the list of words (from word_set) that are correct answer for the given guesses and statuses.

    The returned list should be in alphabetical order---use the built-in `sorted` function to achieve this.

    Preconditions:
    - all words in word_set have the same non-zero length
    - all({guess in word_set for guess in guesses})
    - len(guesses) == len(statuses)
    - all({len(guesses[i]) == len(statuses[i]) for i in range(0, len(guesses))})
    - all({_is_valid_status(status) for status in statuses})

    >>> example_word_set = {'later', 'liter', 'tower', 'lower', 'power', 'round', 'tiger'}
    >>> example_guesses = ['tower', 'lower', 'power', 'round']
    >>> example_statuses = [
    ...     [WRONG_POSITION, INCORRECT, INCORRECT, CORRECT, CORRECT],
    ...     [CORRECT, INCORRECT, INCORRECT, CORRECT, CORRECT],
    ...     [INCORRECT, INCORRECT, INCORRECT, CORRECT, CORRECT],
    ...     [WRONG_POSITION, INCORRECT, INCORRECT, INCORRECT, INCORRECT]
    ... ]
    >>> find_correct_answers(example_word_set, example_guesses, example_statuses)
    ['later', 'liter']
    """
    return sorted([seq for seq in word_set if is_correct_multiple(seq, guesses, statuses)])


@check_contracts
def part3b_example(word_set_file: str, guesses: list[str], statuses: list[list[str]]) -> None:
    """Visualize the Wordle game (with correct answers!) for the given guesses and statuses.

    Complete this function in two steps:

    1. Compute the correct answers for the given guesses and statuses, using the word set
        that's read in from word_set_file. (We've provided the code for reading in the
        words from the file for this function.)
    2. Then, call a2_visualizer.draw_wordle_answers to display the result!
       Note that this visualization is a bit more sophisticated than the one you used in
       part3a_example, as this one lets the user flip through the possible correct answers
       using the left/right arrow keys.

    Preconditions:
        - all words in the word_set_file have the same non-zero length
        - all guesses appear in the word_set_file
        - guesses and statuses satisfy all preconditions of find_correct_answers

    NOTE: Like part3a_example, this function shouldn't have a return statement.
    """
    with open(word_set_file) as f:
        # word_set is assigned to a set[str] containing the words in the file
        word_set = {str.strip(w) for w in f.readlines()}

    # Complete this function by deleting the ... and following the instructions in the docstring
    ans_list = find_correct_answers(word_set, guesses, statuses)
    a2_visualizer.draw_wordle_answers(ans_list, guesses, statuses)


###################################################################################################
# Part 3(c)
###################################################################################################
@check_contracts
def find_correct_guesses_single(word_set: set[str], answer: str, status: list[str]) -> list[str]:
    """Return the list of guesses from word_set that are consistent with the answer and status.

    The returned list should be in alphabetical order---as you did above, use the `sorted` function to
    achieve this.

    Preconditions:
    - answer != ''
    - answer in word_set
    - all words in word_set have the same non-zero length
    - len(answer) == len(status)
    - _is_valid_status(status)

    >>> example_word_set = {'later', 'liter', 'tower', 'lower', 'power', 'round', 'tiger'}
    >>> example_status = [WRONG_POSITION, INCORRECT, INCORRECT, CORRECT, CORRECT]
    >>> find_correct_guesses_single(example_word_set, 'later', example_status)
    ['tiger', 'tower']
    """

    return sorted([x for x in word_set if status == get_guess_status(answer, x)])


@check_contracts
def find_correct_guesses_multiple(word_set: set[str],
                                  answer: str, statuses: list[list[str]]) -> list[list[str]]:
    """Return the possible guess words from word_set that are consistent with the answer and statuses.

    The returned value is a list of lists, where each of the inner lists is a sequence of words that yields
    the given statuses with respect to the given answer.

    IMPORTANT: Call the sorted function on the list of lists before returning it. This will ensure
    that the inner lists are sorted alphabetically by their first words, breaking ties by comparing
    their second words, etc.

    Preconditions:
    - answer != ''
    - answer in word_set
    - all words in word_set have the same non-zero length
    - all({len(answer) == len(status) for status in statuses})
    - all({_is_valid_status(status) for status in statuses})

    >>> example_word_set = {'later', 'liter', 'tower', 'lower', 'power', 'round', 'tiger'}
    >>> example_statuses = [
    ...     [WRONG_POSITION, INCORRECT, INCORRECT, CORRECT, CORRECT],
    ...     [CORRECT, INCORRECT, INCORRECT, CORRECT, CORRECT]
    ... ]
    >>> find_correct_guesses_multiple(example_word_set, 'later', example_statuses)
    [['tiger', 'lower'], ['tower', 'lower']]

    Note that ['tiger', 'lower'] comes before ['tower', 'lower'] because 'tiger' comes before
    'tower' alphabetically.
    """
    temp = cartesian_product_general([find_correct_guesses_single(word_set, answer, status) for status in statuses])
    return sorted(temp)


@check_contracts
def part3c_example(word_set_file: str, answer: str, statuses: list[list[str]]) -> None:
    """Visualize the Wordle game (with reverse-engineered guesses!) for the given answer and statuses.

    Complete this function in three steps (similar to part3b_example):

    1. First, *read in the words in word_set_file*. You can reuse the same code from
       part3b_example for this step.
    2. Then, compute the possible guesses for the given answer and statuses.
    3. Then, call a2_visualizer.draw_wordle_guesses to display the result!

    Preconditions:
        - answer appears in the word_set_file
        - all words in the word_set_file have the same non-zero length
        - answer and statuses satisfy the preconditions of find_correct_guesses_multiple
    """
    with open(word_set_file) as f:
        # word_set is assigned to a set[str] containing the words in the file
        word_set = {str.strip(w) for w in f.readlines()}

    guesses = find_correct_guesses_multiple(word_set, answer, statuses)
    a2_visualizer.draw_wordle_guesses(answer, guesses, statuses)


###################################################################################################
# Part 3(d)
###################################################################################################
@check_contracts
def information_score(answer: str, guess: str) -> float:
    """Return the information score of guess with respect to answer.

    See assignment handout for the formula for information score.

    Preconditions:
    - len(answer) == len(guess)
    - answer != ''
    """
    status = get_guess_status(answer, guess)
    num_correct = status.count(CORRECT)
    num_wrong_pos = status.count(WRONG_POSITION)
    return num_correct + 0.5 * num_wrong_pos


def avg_information_score(answer: str, guesses: list) -> float:
    """Returns average information score, based on part D 2nd question"""
    total_sum = sum([information_score(x, answer) for x in guesses])
    return round(total_sum / len(guesses), 3)


@check_contracts
def find_correct_answers_and_scores(word_set: set[str],
                                    guesses: list[str], statuses: list[list[str]]) -> dict[str, float]:
    """Return a mapping from possible correct answers to their average information score (see handout for details).

    You MUST call find_correct_answers in this function. We strongly encourage you to also define at least
    one new helper function to break down this computation.

    Preconditions:
    - all words in word_set have the same non-zero length
    - all({guess in word_set for guess in guesses})
    - len(guesses) == len(statuses)
    - all({len(guesses[i]) == len(statuses[i]) for i in range(0, len(guesses))})
    - all({_is_valid_status(status) for status in statuses})
    - (NEW!) there is at least one possible correct answer

    NOTE: we haven't provided "example" code for testing this function. You may choose to do your testing
    in the Python console, by writing doctests, and/or by writing test cases or an "example" function
    similar to part3b_example/part3c_example. For the latter two testing options, please write them
    in a separate file (that will not be submitted) rather than including them in this file.
    """
    ans = find_correct_answers(word_set, guesses, statuses)
    return {x: (avg_information_score(x, ans)) for x in ans}


###################################################################################################
# Additional helper function (for some preconditions)
###################################################################################################
@check_contracts
def _is_valid_status(status: list[str]) -> bool:
    """Return whether s is a valid status.

    A valid status is a list that contains only the three statuses in ALL_STATUSES.
    This function is used in some of the precondition expressions in this file.
    You should not change this function.
    """
    return all({char_status in ALL_STATUSES for char_status in status})


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (In PyCharm, select the lines below and press Ctrl/Cmd + / to toggle comments.)
    import python_ta
    python_ta.check_all(config={
        'max-line-length': 120,
        'extra-imports': ['a2_wordle_helpers', 'a2_visualizer'],
        'disable': ['use-a-generator'],
        'allowed-io': ['part3b_example', 'part3c_example']
    })
