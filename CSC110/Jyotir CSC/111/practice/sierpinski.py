"""CSC111 Course Notes: 12.6 Application: Fractals

Module Description
==================

This Python module contains code for an animated drawing of the Sierpinski Triangle.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC111 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC111 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 David Liu and Mario Badr.
"""
import pygame

# Define some colours using their RGB values
FOREGROUND = (255, 113, 41)
BACKGROUND = (46, 47, 41)

# The minimum number of pixels in the Sierpinski triangle
MIN_SIDE = 3

# Amination drawing delay (in ms)
DELAY = 5


def sierpinski(screen: pygame.Surface, v0: tuple[int, int], v1: tuple[int, int],
               v2: tuple[int, int]) -> None:
    """Draw a Sierpinski Triangle on the given screen, with the given vertices.

    Each of v0, v1, and v2 is an (x, y) tuple representing a vertex of the triangle.
    v0 is the lower-left vertex, v1 is the upper vertex, and v2 is the lower-right vertex.
    """
    if v2[0] - v0[0] < MIN_SIDE:
        pygame.draw.polygon(screen, FOREGROUND, [v0, v1, v2])
    else:
        pygame.draw.polygon(screen, FOREGROUND, [v0, v1, v2])

        pygame.display.flip()
        pygame.time.wait(DELAY)

        mid0 = midpoint(v0, v1)
        mid1 = midpoint(v0, v2)
        mid2 = midpoint(v1, v2)

        # Draw centre "sub-triangle"
        pygame.draw.polygon(screen, BACKGROUND, [mid0, mid1, mid2])

        pygame.display.flip()
        pygame.time.wait(DELAY)

        # Recursively draw other three "sub-triangles"
        sierpinski(screen, v0, mid0, mid1)
        sierpinski(screen, mid0, v1, mid2)
        sierpinski(screen, mid1, mid2, v2)


def midpoint(p1: tuple[int, int], p2: tuple[int, int]) -> tuple[int, int]:
    """Return the midpoint of p1 and p2."""
    return (p1[0] + p2[0]) // 2, (p1[1] + p2[1]) // 2


if __name__ == '__main__':
    # Initialize a pygame window
    pygame.init()
    window = pygame.display.set_mode((800, 800))
    window.fill(BACKGROUND)

    # Draw the Sierpinski Triangle!
    sierpinski(window, (100, 670), (400, 150), (700, 670))

    # Render the image to our screen
    pygame.display.flip()

    # Wait until the user closes the Pygame window
    while True:
        if any(event.type == pygame.QUIT for event in pygame.event.get()):
            break
    pygame.display.quit()
    pygame.quit()
