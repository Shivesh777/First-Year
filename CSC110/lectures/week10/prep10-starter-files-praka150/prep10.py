"""CSC110 Fall 2022 Prep 10: Programming Exercises

Instructions (READ THIS FIRST!)
===============================

This Python module contains a new *class definition* with attributes and representation
invariants already defined. We have started a few different methods in the class body,
and your task is to implement EACH method based on the method header and description.

There are two helper functions we have provided near the bottom of this file; please do
not modify either of them.

We have marked each place you need to write code with the word "TODO".
As you complete your work in this file, delete each TODO comment.

You do not need to add additional doctests. However, you should test your work carefully
before submitting it!

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2022 David Liu and Mario Badr.
"""
import colorsys
import math
import random
import pygame

from python_ta.contracts import check_contracts


@check_contracts
class Spinner:
    """A spinner for a board game.

    A spinner has a certain number of slots, numbered starting at 0 and
    increasing by 1 each slot. For example, if the spinner has 6 slots,
    they are numbered 0 through 5, inclusive.

    A spinner also has an arrow that points to one of these slots.

    Instance Attributes:
      - slots: The number of slots in this spinner.
      - position: The slot number that the spinner's arrow is currently pointing to.

    Representation Invariants:
      - 0 <= self.position < self.slots

    Sample Usage:

    >>> s = Spinner(8)  # Create a spinner with 8 slots
    >>> s.position      # A spinner initially points to slot 0
    0
    >>> s.spin(4)
    >>> s.position
    4
    >>> s.spin(2)
    >>> s.position
    6
    >>> s.spin(2)
    >>> s.position
    0
    """
    slots: int
    position: int

    def __init__(self, size: int) -> None:
        """Initialize a new spinner with the given number of slots.

        A spinner's position always starts at 0 (so there is no "position"
        argument for the initializer).

        Preconditions:
            - size >= 1
        """
        self.slots = size
        self.position = 0

    def spin(self, force: int) -> None:
        """Spin this spinner, advancing the arrow <force> slots.

        The spinner wraps around once it reaches its maximum slot, starting
        back at 0. See the class docstring for an example of this.

        Preconditions:
            - force >= 0
        """
        self.position = (self.position + force) % self.slots

    def spin_randomly(self) -> None:
        """Spin this spinner randomly.

        This modifies the spinner's position to a random slot on the
        spinner. Each slot has an equal chance of being pointed to.

        >>> s = Spinner(8)
        >>> s.spin_randomly()
        >>> 0 <= s.position < 8
        True
        """
        self.position = random.randint(0, self.slots - 1)

    def draw(self, screen: pygame.Surface) -> None:
        """Draw this spinner onto the given pygame screen.

        (See starter file images for some examples.)

        The drawing of the spinner consists of two parts:

        1. The outline of a circle that fills the given screen (we have provided this part
           for you already).
        2. The circle is filled by equal sectors, one for each slot. The first sector
           (corresponding to slot 0) should start on the radius of the circle extending
           horizontally to the right of the circle's centre, and extend counter-clockwise.
           The remaining sectors are numbered in counter-clockwise order starting from
           this first sector.

           For example, if self.slots == 6, each sector spans 60 degrees (pi / 3 radians),
           starting at the "positive x direction" relative to the circle's centre.

           Each slot has a colour chosen by the provided get_colour function (don't change
           this function!). See below for some implementation notes.

        Note: This method will display an empty circle if the number of slots in the spinner
        is too high for a small screen size. This is normal, and you don't need to fix this.

        Preconditions:
            - screen.get_width() == screen.get_height()  # screen must be a square
        """
        screen_rect = screen.get_rect()  # A pygame Rect representing the full screen
        radius = screen_rect.width // 2  # The radius of the circle

        # 2. Draw the sectors.
        for slot in range(0, self.slots):
            # Draw each the sector for slot i using the pygame.draw.arc function.
            # First, you should read the documentation for this function here:
            # https://www.pygame.org/docs/ref/draw.html#pygame.draw.arc
            # You'll need to pass in all six arguments to pygame.draw.arc.
            # The SURFACE and RECT should be based on the full screen;
            # the COLOR should be the value obtained from calling our provided
            # helper function Spinner.get_colour;
            # the WIDTH argument should be the radius of the circle;
            # and the START_ANGLE and STOP_ANGLE should be calculated by doing a
            # bit of math. Note that the angles are all calculated in radians,
            # so you should use the constant math.pi in your calculation.
            # Hint: slot 0's sector starts with start_angle == 0.
            #
            # One limitation of pygame is that is doesn't do filled-in arcs very well.
            # To compensate for this, try adding a small value to the stop angles
            # of each sector to fill in the gaps that you'll see if you just use the
            # angles you get from evenly dividing the circle.
            # We aren't grading your choice of "small value", but we do want you to
            # experiment with it a little.
            arc_angle = 2 * math.pi / self.slots
            i_angle = slot * arc_angle
            f_angle = i_angle + (arc_angle * 1.018)
            pygame.draw.arc(screen, self.get_colour(slot), screen_rect, i_angle, f_angle, radius)



        # 1. Draw the circle outline. (This comes second to ensure it is drawn above the
        #    slot sectors.)
        pygame.draw.circle(screen, pygame.Color('black'), (radius, radius), radius, 3)

    def get_colour(self, slot: int) -> tuple[int, int, int]:
        """Return a unique pygame colour to use for the slot in spinner.

        The returned colour is grayscale when the slot is not currently selected.
        Note: Some colours may not be distinct when the spinner has over 600 slots.

        Preconditions:
            - 0 <= slot < self.slots

        You should not modify this function.
        """
        selected_colour = float_to_colour(slot / self.slots)
        if self.position == slot:
            return selected_colour
        else:
            gray_avg = sum(selected_colour) // 3
            return gray_avg, gray_avg, gray_avg


###############################################################################
# Helper functions (Pygame and colours)
###############################################################################
def run_example(spinner: Spinner) -> None:
    """Show a window that visualizes a spinner.

    You can use this function to test your other functions, and are
    free to modify this function as well.

    When you call this function, the spinner will appear in a Pygame window.
    The spinner can be spun randomly by pressing the space bar.
    """
    # We must first initialize pygame
    pygame.init()

    # Create a screen that we can draw on
    size = (500, 500)
    screen = pygame.display.set_mode(size)

    # Visualize the spinner
    screen.fill(pygame.Color('white'))
    spinner.draw(screen)
    pygame.display.flip()

    # Start the event loop
    while True:
        # Process events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # Exit the event loop
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                # Spin the spinner
                spinner.spin_randomly()

                screen.fill(pygame.Color('white'))
                spinner.draw(screen)
                pygame.display.flip()


@check_contracts
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


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (In PyCharm, select the lines below and press Ctrl/Cmd + / to toggle comments.)
    import python_ta
    python_ta.check_all(config={
        'max-line-length': 120,
        'extra-imports': ['colorsys', 'math', 'random', 'pygame'],
        'disable': ['use-a-generator'],
        'generated-members': ['pygame.*']
    })
