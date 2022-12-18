"""CSC110 Fall 2022 Assignment 1: Data and Functions (Colour Visualizations)

Module Description
==================
This Python file contains some code for visualizing colours using Pygame.

You do *not* need to understand how any of this code works for Assignment 1.
But don't worry, over the next few weeks you'll learn about how to use Pygame
to create your own visualizations.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2022 David Liu and Mario Badr.
"""
import pygame
from PIL import Image


def show_colours_pygame(colours: list) -> None:
    """Visualize the given list of colours using Pygame.

    Takes a list of colours, where each colour is represented as a tuple of three
    integers: (r, g, b). The list must not be empty and must have length <= 100.

    When this function is called, each colour appears as a filled squared in
    a Pygame window. When the window is open, you can close it like a normal window
    (press the red X in the top-right corner).

    NOTE: this function is similar to, but different from, the version provided in Tutorial 1.
    """
    assert colours != [], 'You must call show_colours_pygame with at least one colour.'
    assert len(colours) <= 100, 'You can visualize a maximum of 100 colours.'
    pygame.display.init()

    screen_width = 800
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill((255, 255, 255))  # Fill screen with white

    rect_width = min(screen_width // len(colours), 50)

    x_start = (screen_width - rect_width * len(colours)) // 2
    y_start = (screen_height - rect_width) // 2

    for i in range(len(colours)):
        pygame.draw.rect(
            screen, colours[i],
            pygame.Rect(x_start + rect_width * i, y_start, rect_width, rect_width)
        )

    pygame.display.flip()

    pygame.event.clear()
    pygame.event.set_blocked(None)
    pygame.event.set_allowed(pygame.QUIT)
    pygame.event.wait()

    pygame.display.quit()


def show_colour_rows_pygame(colour_rows: list) -> None:
    """Visualize the given list of colour rows using Pygame. (This is a "2-D" version of show_colours_pygame.)

    This list must not be empty and must have length <= 100.
    Takes a list of colours, where each colour is represented as a tuple of three
    integers: (r, g, b). The list must not be empty and must have length <= 100.

    When this function is called, each colour appears as a solid vertical bar in
    a Pygame window. When the window is open, you can close it like a normal window
    (press the red X in the top-right corner).
    """
    assert colour_rows != [], 'You must call show_colour_rows_pygame with at least one colour row.'
    assert len(colour_rows) <= 100, 'You can visualize a maximum of 100 colour rows.'
    pygame.display.init()

    screen_width = 800
    screen_height = 800
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill((255, 255, 255))  # Fill screen with white

    rect_width = min(screen_height // len(colour_rows), screen_width // len(colour_rows[0]), 50)

    x_start = (screen_width - rect_width * len(colour_rows[0])) // 2
    y_start = (screen_height - rect_width * len(colour_rows)) // 2

    for i in range(len(colour_rows)):
        for j in range(len(colour_rows[i])):
            pygame.draw.rect(
                screen, colour_rows[i][j],
                pygame.Rect(x_start + rect_width * j, y_start + rect_width * i, rect_width, rect_width)
            )

    pygame.display.flip()

    pygame.event.clear()
    pygame.event.set_blocked(None)
    pygame.event.set_allowed(pygame.QUIT)
    pygame.event.wait()

    pygame.display.quit()


def load_image_pixels(file_path: str) -> list:
    """Return the pixels contained in the image in the given file_path.

    The pixels are returned as a list of colour rows, i.e., a list of lists of colours.
    The first colour row represents the *top* row of the image.
    """
    image = Image.open(file_path)
    raw_pixel_data = image.load()

    return [[list(raw_pixel_data[x, y][:3]) for x in range(0, image.width)] for y in range(0, image.height)]


def save_image(file_path: str, image_data: list) -> None:
    """Save the given image_data into an image file at location file_path.

    You may ASSUME that:
    - every element of image_data is a valid colour row with the same length
    - file_path is a valid file name or path (with existing folder names), and ends with
      a valid image file extension (e.g., '.jpg')
    """
    height = len(image_data)
    width = len(image_data[0])
    image = Image.new('RGB', (width, height))

    [image.putpixel((x, y), tuple(image_data[y][x])) for x in range(width) for y in range(height)]

    image.save(file_path)
