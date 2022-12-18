"""CSC110 Fall 2021 Prep 10: Programming Exercises

Instructions (READ THIS FIRST!)
===============================

This Python module contains a new *class definition* with attributes and representation
invariants already defined. We have started a few different methods in the class body,
and your task is to implement EACH method based on the method header and description.

There are some helper functions we have provided near the bottom of this file; please do
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

This file is Copyright (c) 2021 David Liu, Mario Badr, and Tom Fairgrieve.
"""
import random
import tkinter as tk

PREDEFINED_COLOURS = [
    'AntiqueWhite1', 'CadetBlue1', 'DarkGoldenrod1', 'DarkOliveGreen1',
    'DarkOrange1', 'DarkOrchid1', 'DarkSeaGreen1', 'DarkSlateGray1',
    'HotPink1', 'IndianRed1', 'LightBlue1', 'LightGoldenrod1',
    'LightPink1', 'LightSkyBlue1', 'LightSteelBlue1', 'MediumOrchid1',
    'MediumPurple1', 'OliveDrab1', 'PaleGreen1', 'PaleTurquoise1',
    'PaleVioletRed1', 'RosyBrown1', 'RoyalBlue1', 'SeaGreen1',
    'SkyBlue1', 'SlateBlue1', 'SlateGray1', 'SteelBlue1', 'VioletRed1',
    'alice blue', 'antique white', 'aquamarine', 'azure', 'bisque',
    'blanched almond', 'blue violet', 'brown1', 'burlywood1',
    'cadet blue', 'chocolate1', 'coral', 'coral1', 'cornflower blue',
    'cyan', 'dark goldenrod', 'dark green', 'dark khaki',
    'dark olive green', 'dark orange', 'dark orchid', 'dark salmon',
    'dark sea green', 'dark slate blue', 'dark turquoise', 'dark violet',
    'deep pink', 'deep sky blue', 'dodger blue', 'firebrick1',
    'floral white', 'forest green', 'ghost white', 'gold',
    'goldenrod', 'goldenrod1', 'green yellow', 'hot pink', 'indian red',
    'khaki', 'khaki1', 'lavender', 'lavender blush', 'lawn green',
    'lemon chiffon', 'light blue', 'light coral', 'light cyan',
    'light goldenrod', 'light goldenrod yellow', 'light grey',
    'light pink', 'light salmon', 'light sea green', 'light sky blue',
    'light slate blue', 'light steel blue', 'light yellow', 'lime green',
    'linen', 'maroon', 'maroon1', 'medium aquamarine', 'medium blue',
    'medium orchid', 'medium purple', 'medium sea green',
    'medium slate blue', 'medium spring green', 'medium turquoise',
    'medium violet red', 'midnight blue', 'mint cream', 'misty rose',
    'navajo white', 'navy', 'old lace', 'olive drab', 'orange',
    'orange red', 'orchid1', 'pale goldenrod', 'pale green',
    'pale turquoise', 'pale violet red', 'papaya whip', 'peach puff',
    'pink', 'pink1', 'plum1', 'powder blue', 'purple', 'purple1',
    'rosy brown', 'royal blue', 'saddle brown', 'salmon', 'salmon1',
    'sandy brown', 'sea green', 'sienna1', 'sky blue', 'slate blue',
    'snow', 'spring green', 'steel blue', 'tan1', 'thistle', 'thistle1',
    'tomato', 'turquoise', 'turquoise1', 'violet red', 'wheat1',
    'white smoke', 'yellow green'
]


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

    def draw(self, canvas: tk.Canvas) -> None:
        """Draw this spinner onto the given canvas.

        (See starter file images for some examples.)

        Here is the algorithm you should follow for drawing the slots:

           The circle is filled by equal sectors, one for each slot. The first sector
           (corresponding to slot 0) should start on the radius of the circle extending
           horizontally to the right of the circle's centre, and extend counter-clockwise.
           The remaining sectors are numbered in counter-clockwise order starting from
           this first sector.

           For example, if self.slots == 6, each sector spans 60 degrees, starting at the
           "positive x direction" relative to the circle's centre.

           Each slot has a colour chosen by the provided get_colour function (don't change
           this function!). See below for some implementation notes.

        Note: This method will display an empty circle if the number of slots in the spinner
        is too high for a small screen size. This is normal, and you don't need to fix this.
        """
        height = canvas.winfo_reqheight()
        width = canvas.winfo_reqwidth()
        x, y, radius = width // 2, height // 2, width // 4
        each_angle = 360 / self.slots
        for i in range(self.slots):
            color = Spinner.get_colour(self, canvas, i)
            draw_arc(canvas, x, y, radius, i * each_angle, (i + 1) * each_angle, color)

        # Draw each the sector for slot i using the draw_arc function and get_colour method.
        # You will need to calculate the start and stop angles by doing some math. As a hint,
        # slot 0's sector has a start angle of 0.

    def get_colour(self, w: tk.Widget, slot: int) -> str:
        """Return a unique colour to use for the slot in spinner.

        The returned colour is grayscale when the slot is not currently selected.

        Preconditions:
            - 0 <= slot < spinner.slots
            - spinner.slots <= len(PREDEFINED_COLOURS)

        You should not modify this function.
        """
        normalize = len(PREDEFINED_COLOURS) // self.slots
        selected_colour = PREDEFINED_COLOURS[normalize * slot]

        if self.position == slot:
            return selected_colour
        else:
            # Convert to RGB tuple
            selected_colour = w.winfo_rgb(selected_colour)
            # Convert to grayscale
            gray_avg = sum(selected_colour[0:3]) // 3
            return rgb_to_hex((gray_avg, gray_avg, gray_avg))


####################################################################################################
# Helper functions - DO NOT CHANGE THESE
####################################################################################################
def rgb_to_hex(colour: tuple[int, int, int]) -> str:
    """Return the hex format of the RGB colour."""
    r, g, b = colour
    return f'#{r:02x}{g:02x}{b:02x}'


def draw_arc(canvas: tk.Canvas, x: int, y: int, r: int, start_angle: float, stop_angle: float,
             colour: str) -> None:
    """Draw a filled (with colour) part of a circle (with radius r) at location (x, y) starting at
    start_angle and ending at stop_angle (all angles are in degrees).
    """
    canvas.create_arc(x - r, y - r, x + r, y + r, start=start_angle,
                      extent=stop_angle - start_angle, fill=colour)


def spin_button_callback(canvas: tk.Canvas, label: tk.Label, spinner: Spinner) -> None:
    """Spin the spinner and update the canvas to show the change.

    This function is called when you click the button in the GUI. These types of functions are
    called "callbacks".
    """
    spinner.spin_randomly()

    label.configure(text=f'Position: {spinner.position}')

    spinner.draw(canvas)
    canvas.update()


def run_example(spinner: Spinner) -> None:
    """Show a window that visualizes a spinner.

    You can use this function to test your other functions.

    When you call this function, the spinner will appear in a window. You can spin the spinner
    randomly by clicking the button.
    """
    window = tk.Tk()
    window.title('Visualizing the spinner')
    # Use a frame for organizing the different widgets
    frame = tk.Frame(window)
    frame.pack()

    # Create a canvas and "initialize it" with a drawing of the spinner
    canvas = tk.Canvas(frame, bg='white', height=500, width=500)
    spinner.draw(canvas)
    # Create a label to tell us which position the spinner is at (helps with debugging)
    label = tk.Label(frame, text=f'Position: {spinner.position}')
    # Create a button to control the spinner
    spin_button = tk.Button(frame, text='Spin',
                            command=lambda: spin_button_callback(canvas, label, spinner))

    # Organize our widgets
    canvas.pack(side=tk.BOTTOM)
    spin_button.pack(side=tk.TOP)
    label.pack(side=tk.TOP)

    # Give control of our program over to tkinter
    window.mainloop()


if __name__ == '__main__':
    import python_ta
    python_ta.check_all(config={
        'max-line-length': 100,
        'extra-imports': ['python_ta.contracts', 'random', 'tkinter'],
        'disable': ['R1705', 'C0200'],
        'max-args': 7
    })

    import python_ta.contracts
    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod()
