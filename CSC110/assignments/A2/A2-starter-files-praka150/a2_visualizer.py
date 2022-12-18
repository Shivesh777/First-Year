"""CSC110 Fall 2022 Assignment 2, Part 3: Wordle!

Module Description
==================
This Python file contains some code for defining various constants related to Wordle.

You should not modify this file (we will be using our own version for testing purposes).
You do *not* need to understand how any of this code works for Assignment 2.
However, you should be able to read the function headers and docstrings of the functions
in the section labelled "Main visualization functions", as you will be using them in
Part 3 of the assignment.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2022 David Liu, Tom Fairgrieve, and Angela Zavaleta Bernuy.
"""
import pygame
from python_ta.contracts import check_contracts
from a2_wordle_helpers import CORRECT, INCORRECT, WRONG_POSITION


###############################################################################
# Main visualization functions (this is the only section you need to read to
# complete this assignment)
###############################################################################
@check_contracts
def draw_wordle(answer: str, guesses: list[str], statuses: list[list[str]]) -> None:
    """Visualize the given Wordle game using Pygame.

    Preconditions:
        - answer != ''
        - all({len(guess) == len(answer) for guess in guesses})
        - all({len(status) == len(answer) for status in statuses})
        - all({status in {CORRECT, INCORRECT, WRONG_POSITION} for status in statuses})
    """
    screen = _initialize_pygame_window()

    _draw_guesses(screen, guesses, statuses)
    _draw_answer(screen, answer)

    pygame.display.flip()

    pygame.event.clear()
    pygame.event.set_blocked(None)
    pygame.event.set_allowed(pygame.QUIT)
    pygame.event.wait()

    pygame.display.quit()


@check_contracts
def draw_wordle_answers(answers: list[str], guesses: list[str], statuses: list[list[str]]) -> None:
    """Visualize the given Wordle game (with multiple answers) using Pygame.

    Preconditions:
        - all({len(guess) == len(answer) for guess in guesses for answer in answers})
        - all({len(status) == len(answer) for status in statuses  for answer in answers})
        - all({status in {CORRECT, INCORRECT, WRONG_POSITION} for status in statuses})

    To start, the first answer in answers is displayed. You can use the left/right arrow
    keys to switch between the different given answers.
    """
    screen = _initialize_pygame_window()

    current_answer_index = 0

    pygame.event.clear()
    pygame.event.set_blocked(None)
    pygame.event.set_allowed([pygame.KEYDOWN, pygame.QUIT])
    while True:
        answer = answers[current_answer_index]
        screen.fill((255, 255, 255))  # Fill screen with white
        _draw_guesses(screen, guesses, statuses)
        _draw_answer(screen, answer)
        pygame.display.flip()

        # Wait for an event (either pygame.MOUSEBUTTONDOWN or pygame.QUIT)
        event = pygame.event.wait()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            current_answer_index = (current_answer_index + 1) % len(answers)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            current_answer_index = (current_answer_index - 1) % len(answers)
        elif event.type == pygame.QUIT:
            pygame.display.quit()
            return


@check_contracts
def draw_wordle_guesses(answer: str, all_guesses: list[list[str]], statuses: list[list[str]]) -> None:
    """Visualize the given Wordle game (with reverse-engineered guesses) using Pygame.

    Note that all_guesses is now a list of lists of guesses. Each inner list represents one possible sequence
    of guesses that is consistent with the given statuses and answer.

    Preconditions:
        - answer != ''
        - all({len(status) == len(answer) for status in statuses})
        - all({status in {CORRECT, INCORRECT, WRONG_POSITION} for status in statuses})
        - all({len(guesses) == len(statuses) for guesses in all_guesses})
        - all({len(guess) == len(answer) for guesses in all_guesses for guess in guesses})
    """
    screen = _initialize_pygame_window()

    all_guesses_and_blank = [[' ' * len(answer)] * len(statuses)] + all_guesses
    current_guess_index = 0

    pygame.event.clear()
    pygame.event.set_blocked(None)
    pygame.event.set_allowed([pygame.KEYDOWN, pygame.QUIT])
    while True:
        guesses = all_guesses_and_blank[current_guess_index]
        screen.fill((255, 255, 255))  # Fill screen with white
        _draw_guesses(screen, guesses, statuses)
        _draw_answer(screen, answer)
        pygame.display.flip()

        # Wait for an event (either pygame.MOUSEBUTTONDOWN or pygame.QUIT)
        event = pygame.event.wait()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            current_guess_index = (current_guess_index + 1) % len(all_guesses_and_blank)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            current_guess_index = (current_guess_index - 1) % len(all_guesses_and_blank)
        elif event.type == pygame.QUIT:
            pygame.display.quit()
            return


###############################################################################
# These functions are responsible for interacting with pygame
###############################################################################
def _initialize_pygame_window() -> pygame.Surface:
    """Initialize and return a new pygame window.
    """
    pygame.display.init()

    screen_width = 633
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill((255, 255, 255))  # Fill screen with white
    pygame.display.set_caption("Wordle, CSC110 Edition!")

    return screen


###############################################################################
# These functions are responsible for drawing the individual words to the screen.
# You don't need to worry about any code below this line (and in fact, should
# not call any of the functions below in your own code).
###############################################################################
# Constants (font)
pygame.init()  # Need to initialize pygame to create a font
FONT = pygame.font.Font('assets/FreeSansBold.otf', 50)

# Constants (colours)
RECT_COLOURS = {
    CORRECT: '#6aaa64',         # green
    WRONG_POSITION: '#c9b458',  # orange
    INCORRECT: '#787c7e',       # grey
}


# Constants (screen layout)
LETTER_SIZE = 75
LETTER_X_SPACING = 10
LETTER_Y_SPACING = 12
ANSWER_HEIGHT = LETTER_SIZE + 2 * LETTER_Y_SPACING


def _draw_guesses(screen: pygame.Surface, guesses: list[str], statuses: list[list[str]]) -> None:
    """Draw a list of guesses and corresponding status rectangles to the screen.

    The x- and y-coordinates of each letter are computed so that the letter grid is horizontally and vertically centred.
    """
    grid_height = len(guesses) * LETTER_SIZE + (len(guesses) - 1) * LETTER_Y_SPACING
    init_y = (screen.get_height() - ANSWER_HEIGHT - grid_height) // 2

    [_draw_word(screen, guesses[i], statuses[i], init_y + i * (LETTER_SIZE + LETTER_Y_SPACING))
     for i in range(0, len(guesses))]


def _draw_answer(screen: pygame.Surface, answer: str) -> None:
    """Draw the answer of the Wordle puzzle at the bottom of the pygame screen.

    The x-coordinates of each letter are computed so that the letters are vertically centred,
    and the y-coordinates are chosen so the answer appears at the bottom of the screen.
    """
    answer_y = screen.get_height() - LETTER_SIZE - 2 * LETTER_Y_SPACING
    _draw_word(screen, answer, [CORRECT] * len(answer), answer_y)


def _draw_word(screen: pygame.Surface, word: str, status: list[str], y: int) -> None:
    """Draw a word and status rectangles to the given screen at the given y coordinate.

    The x-coordinates of each letter and rectangle are computed based on screen.width and the number of letters,
    so that the letters are vertically centered.
    """
    word_width = len(word) * LETTER_SIZE + (len(word) - 1) * LETTER_X_SPACING
    init_x = (screen.get_width() - word_width) // 2

    [_draw_letter(screen, word[i], status[i], init_x + i * (LETTER_SIZE + LETTER_X_SPACING), y)
     for i in range(0, len(word))]


def _draw_letter(screen: pygame.Surface, letter: str, status_char: str, bg_x: int, bg_y: int) -> None:
    """Draw a letter on the screen at the given position. Letters are automatically converted to uppercase.
    """
    bg_rect = (bg_x, bg_y, LETTER_SIZE, LETTER_SIZE)
    bg_colour = RECT_COLOURS[status_char]
    text_position = (bg_x + LETTER_SIZE // 2, bg_y + LETTER_SIZE // 2)
    text_screen = FONT.render(str.upper(letter), True, "white")
    text_rect = text_screen.get_rect(center=text_position)
    pygame.draw.rect(screen, bg_colour, bg_rect)
    screen.blit(text_screen, text_rect)


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={
        'max-line-length': 120,
        'disable': ['expression-not-assigned'],
        'generated-members': ['pygame.*'],
        'extra-imports': ['pygame', 'a2_wordle_helpers']
    })
