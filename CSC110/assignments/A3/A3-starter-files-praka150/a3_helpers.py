"""CSC110 Fall 2022 Assignment 2, Part 3: Chaos, Fractals, Point Sequences

Module Description
==================
This Python file contains some code for some helper functions for Part 3.

You should not modify this file (we will be using our own version for testing purposes).
You do *not* need to understand how any of this code works for Assignment 3.
However, you should be able to read the function headers and docstrings of ALL functions
in this file, as you will be using them in Part 3 of the assignment.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2022 David Liu, Tom Fairgrieve, and Angela Zavaleta Bernuy.
"""
import colorsys
import math
import sys

import pygame


###############################################################################
# Pygame helper functions (Questions 1-3)
###############################################################################
# You should read the docstrings of each function below to understand how to call them.
# However, you may *NOT* modify their implementations.

def initialize_pygame_window(width: int, height: int) -> pygame.Surface:
    """Initialize and return a new pygame window with the given width and height.

    Preconditions:
    - width >= 1
    - height >= 1
    """
    pygame.display.init()

    screen_width = width
    screen_height = height
    screen = pygame.display.set_mode((screen_width, screen_height))
    screen.fill((255, 255, 255))  # Fill screen with white
    pygame.display.set_caption("CSC110 Assignment 3, Part 3")
    pygame.display.flip()

    return screen


def draw_pixel(screen: pygame.Surface, point: tuple[int, int], colour: tuple[int, int, int]) -> None:
    """Draw a single pixel on the given screen, at the given point and with the given colour.

    Note: the coordinate system for a Pygame surface places (0, 0) at the TOP-LEFT corner, with the x-axis increasing
    to the right and the y-axis increasing down.

    Preconditions:
    - 0 <= point[0] < screen.get_width()
    - 0 <= point[1] < screen.get_height()
    """
    pixel_array = pygame.PixelArray(screen)

    # NOTE: you can safely ignore the PyCharm warning on the next line about pixel_array not defining __setitem__
    pixel_array[point[0], point[1]] = colour
    pygame.display.flip()


def wait_for_pygame_exit() -> None:
    """Wait until the user closes the Pygame window.

    Preconditions:
    - Must be called after the pygame screen has been created (e.g., by initialize_pygame_window).
    """
    print('Your drawing/animation is now complete, and you can close the Pygame window.')
    pygame.event.clear()
    pygame.event.set_blocked(None)
    pygame.event.set_allowed(pygame.QUIT)
    pygame.event.wait()

    pygame.display.quit()


###############################################################################
# Pygame helper functions (Question 4)
###############################################################################
def input_mouse_pygame() -> tuple[int, int]:
    """Wait for the user to click on the pygame window, and return the coordinates of the click position
    after the click occurs.

    The return value is the (x, y) coordinates of the mouse click position.

    NOTE: If you close the Pygame window while this function is called, you will need to restart the
    Python console.
    """
    pygame.event.clear()
    pygame.event.set_blocked(None)
    pygame.event.set_allowed([pygame.QUIT, pygame.MOUSEBUTTONUP])
    event = pygame.event.wait()

    if event.type == pygame.MOUSEBUTTONUP:
        return event.pos
    else:
        print('Exiting Pygame window. Please restart the Python console!')
        pygame.display.quit()
        sys.exit(0)


###############################################################################
# Other OPTIONAL helper functions (only used for testing purposes)
###############################################################################
def regular_polygon_vertices(screen_width: int, screen_height: int, radius: int, n: int) -> list[tuple[int, int]]:
    """Return a list of vertices of a regular n-sided polygon (i.e., a polygon with n equal sides).

    The polygon is centred on the midpoint of the screen with the given width and height.
    radius specifies the distance between each vertex and the centre of the polygon.

    Preconditions:
    - screen_width >= 2
    - screen_height >= 2
    - radius >= 1
    - n >= 3
    """
    mid_x = screen_width / 2
    mid_y = screen_height / 2

    return [(round(mid_x + radius * math.cos(2 * math.pi * i / n - math.pi / 2)),
             round(mid_y + radius * math.sin(2 * math.pi * i / n - math.pi / 2)))
            for i in range(0, n)]


def float_to_colour(x: float) -> tuple[int, int, int]:
    """Return an RGB24 colour computed from x.

    This uses x to pick a "direction on the colour wheel", using the colorsys module
    that comes with Python. You aren't responsible for knowing about how this works,
    but if you're interested you can read more about the HSV colour model at
    https://www.lifewire.com/what-is-hsv-in-design-1078068.

    Preconditions:
    - 0.0 <= x <= 1.0
    """
    rgb = colorsys.hsv_to_rgb(x, 1.0, 1.0)
    return round(rgb[0] * 255), round(rgb[1] * 255), round(rgb[2] * 255)
