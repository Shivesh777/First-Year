"""CSC110 Fall 2021 Assignment 1, Part 5

Instructions (READ THIS FIRST!)
===============================

Please follow the instructions in the assignment handout to complete this file.

Throughout this module, we assume that images are at least 4 pixels wide and 4 pixels high.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2021 Mario Badr and Tom Fairgrieve.
"""
from statistics import median

import a1_image


def create_example_pixel_data() -> list:
    """Return a new list of pixels that can be used in the doctest examples. The list describes
    an image that is 4 pixels wide and 4 pixels high. Each element in the list is a three-element
    tuple that corresponds to the red, green, and blue colour channels, respectively.

    The pixels appear in the order of left-to-right, bottom-to-top (i.e., the same as
    a1_image.load_image).
    """
    return [(128, 128, 128), (35, 50, 65), (210, 32, 68), (32, 208, 43),    # y = 0 (bottom)
            (130, 20, 42), (43, 44, 45), (17, 243, 82), (61, 85, 92),       # y = 1
            (201, 23, 23), (23, 23, 23), (42, 180, 19), (16, 58, 29),       # y = 2
            (1, 52, 128), (26, 123, 128), (71, 234, 82), (23, 108, 34)]     # y = 3 (top)


def get_pixel(pixel_data: list, image_width: int, x: int, y: int) -> tuple:
    """Return a new RGB-tuple of the pixel at location (x, y) from the pixels in pixel_data that has
    width image_width.

    Assume that pixel_data was obtained from an image using a1_image.load_image.

    >>> example_pixels = create_example_pixel_data()
    >>> get_pixel(example_pixels, 4, 0, 0)
    (128, 128, 128)
    >>> get_pixel(example_pixels, 4, 1, 2)
    (23, 23, 23)
    """
    index = x + y * image_width
    r, g, b = pixel_data[index]

    return r, g, b


def get_pixel_window(pixel_data: list, width: int, x: int, y: int) -> list:
    """Return a new list of RGB-tuples of the pixel at (x, y), along with its neighbours, from the
    pixels in pixel_data that has width image_width.

    A neighbouring pixel is a pixel that "touches" the pixel at (x, y), including diagonals.

    Assume that the location (x, y) is not on any edge of the image described in pixel_data.

    >>> example_pixels = create_example_pixel_data()
    >>> get_pixel_window(example_pixels, 4, 1, 1)
    [(201, 23, 23), (23, 23, 23), (42, 180, 19), (130, 20, 42), (43, 44, 45), (17, 243, 82), \
(128, 128, 128), (35, 50, 65), (210, 32, 68)]
    >>> get_pixel_window(example_pixels, 4, 2, 2)
    [(26, 123, 128), (71, 234, 82), (23, 108, 34), (23, 23, 23), (42, 180, 19), (16, 58, 29), \
(43, 44, 45), (17, 243, 82), (61, 85, 92)]
    """
    return [get_pixel(pixel_data, width, x + j, y + i) for i in range(1, -1 - 1, -1)
            for j in range(-1, 1 + 1)]


def separate_colour_channels(rgb_pixels: list) -> dict:
    """Return a dictionary mapping the strings 'r', 'g', and 'b' to a list of the red, green, and
    blue colour channels, respectively, in rgb_pixels. The value lists should have the same order
    as rgb_pixels.

    >>> example_pixels = create_example_pixel_data()
    >>> separate_colour_channels(example_pixels) == \
    {'r': [128, 35, 210, 32, 130, 43, 17, 61, 201, 23, 42, 16, 1, 26, 71, 23],\
    'g': [128, 50, 32, 208, 20, 44, 243, 85, 23, 23, 180, 58, 52, 123, 234, 108],\
    'b': [128, 65, 68, 43, 42, 45, 82, 92, 23, 23, 19, 29, 128, 128, 82, 34]}
    True
    """


def calculate_median_colour(colour_channels: dict) -> tuple:
    """Return the median colour in colour_channels.

    The median colour is the median value of each colour channel, type converted to an integer.

    Hint: use median from the statistics module. Be careful because the call to median may return a
    float.

    >>> example_pixels = create_example_pixel_data()
    >>> separated_colour_channels = separate_colour_channels(example_pixels)
    >>> calculate_median_colour(separated_colour_channels)
    (38, 71, 55)
    """


def apply_median_filter(pixel_data: list, image_width: int, image_height: int) -> list:
    """Return a new list of pixels formed from the corresponding pixels in pixel_data (that
    represents an image with width image_width and height image_height), except with a median filter
    applied to the pixels.

    The median filter should not process boundaries (i.e., the edges of the image), so the returned
    new list of pixels represents an image with width image_width - 2 and height image_height - 2.

    >>> example_pixels = create_example_pixel_data()
    >>> apply_median_filter(example_pixels, 4, 4)
    [(43, 44, 45), (35, 58, 45), (42, 52, 45), (26, 108, 45)]
    """
    windows = [get_pixel_window(pixel_data, image_width, x, y)
               for y in range(1, image_height - 1) for x in range(1, image_width - 1)]
    window_channels = [separate_colour_channels(window) for window in windows]
    return [calculate_median_colour(window_channel) for window_channel in window_channels]


def run_median_filter_example(source: str, destination: str) -> None:
    """Apply the median filter to an example image file at source and save the result in
    destination.
    """
    original_pixel_data, original_width, original_height = a1_image.load_image(source)

    new_pixel_data = apply_median_filter(original_pixel_data, original_width, original_height)

    new_width = original_width - 2
    new_height = original_height - 2
    a1_image.save_image(destination, new_pixel_data, new_width, new_height)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (Delete the "#" and space before each line.)
    import python_ta
    python_ta.check_all(config={
        'extra-imports': ['statistics', 'a1_image'],
        'max-line-length': 100
    })
