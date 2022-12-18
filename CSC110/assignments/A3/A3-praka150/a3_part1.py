"""CSC110 Fall 2022 Assignment 3, Part 1: Data Analysis with Toronto Health

Instructions (READ THIS FIRST!)
===============================

This Python module contains the functions you will complete for Part 1 of this assignment.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2022 David Liu, Tom Fairgrieve, and Angela Zavaleta Bernuy
"""
import csv
from dataclasses import dataclass

from plotly.express import scatter


###############################################################################
# Part 1(a)
###############################################################################
@dataclass
class HypertensionData:
    """A data class representing neighbourhood hypertension data.

    (You'll note that this data class has a lot of attributes! Another representation
    we could have used was to store the counts in a dictionary with appropriate keys.)

    Instance Attributes:
        - name: the name of the neighbourhood
        - num_hypertension_all: the number of people in the neighbourhood with hypertension
        - num_all: the number of people in the neighbourhood
        - num_hypertension_20-44: the number of people aged 20-44 in the neighbourhood with hypertension
        - num_20_44: the number of people aged 20-44 in the neighbourhood
        - num_hypertension_45_64: the number of people aged 45-64 in the neighbourhood with hypertension
        - num_45_64: the number of people aged 45-64 in the neighbourhood
        - num_hypertension_65_plus: the number of people aged 65 and older in the neighbourhood with hypertension
        - num_65_plus: the number of people aged 65 and older in the neighbourhood
    """
    name: str
    num_hypertension_all: int
    num_all: int
    num_hypertension_20_44: int
    num_20_44: int
    num_hypertension_45_64: int
    num_45_64: int
    num_hypertension_65_plus: int
    num_65_plus: int


@dataclass
class LowIncomeData:
    """A data class representing neighbourhood low income data.

    Instance Attributes:
        - name: the name of the neighbourhood
        - num_low_income: the number of people in the neighbourhood with low income status
        - population_total: the total number of people in the neighbourhood
    """
    name: str
    num_low_income: int
    population_total: int


def load_hypertension_data(filename: str) -> list[HypertensionData]:
    """Return a list of HypertensionData based on the data in filename.

    The returned list must match the same order the rows appear in the given file.

    Preconditions:
    - filename refers to a csv file whose format matches the hypertension dataset description
      on the assignment handout.

    >>> data = load_hypertension_data('datasets/part1/hypertension_data_small.csv')
    >>> len(data)
    5
    """
    data_so_far = []

    with open(filename) as f:
        reader = csv.reader(f, delimiter=',')

        # Skip the first header row.
        next(reader)

        for row in reader:
            # row is a list of strings
            # Your task is to extract the relevant data from row and add it to the accumulator.
            # Make sure to use type conversion to ensure instance attributes have the correct type
            data_so_far += [HypertensionData(row[0], int(row[1]), int(row[2]), int(row[3]), int(row[4]), int(row[5]),
                                             int(row[6]), int(row[7]), int(row[8]))]

    return data_so_far


def load_low_income_data(filename: str) -> list[LowIncomeData]:
    """Return a list of LowIncomeData values representing the data in filename.

    The returned list must match the same order the rows appear in the given file.

    Preconditions:
    - filename refers to a csv file whose format matches the low income dataset description
      on the assignment handout.

    >>> data = load_low_income_data('datasets/part1/low_income_data_small.csv')
    >>> len(data)
    5
    """
    data_so_far = []

    with open(filename) as f:
        reader = csv.reader(f, delimiter=',')

        # Skip header row
        next(reader)

        for row in reader:
            # row is a list of strings
            # Your task is to extract the relevant data from row and add it to the accumulator.
            # Make sure to use type conversion to ensure instance attributes have the correct type.
            data_so_far += [LowIncomeData(row[0], int(row[2]), int(row[1]))]

    return data_so_far


###############################################################################
# Part 1(b)
###############################################################################
def total_num_hypertension(data: list[HypertensionData]) -> int:
    """Return the total number of people aged 20+ with hypertension in the given data.

    Preconditions:
    - data does not contain any duplicated neighbourhood names

    >>> data = load_hypertension_data('datasets/part1/hypertension_data_small.csv')
    >>> total_num_hypertension(data) == 23205
    True
    """
    sum_so_far = 0
    for row in data:
        sum_so_far += row.num_hypertension_all
    return sum_so_far


def high_hypertension_rate(data: list[HypertensionData], threshold: float) -> set[str]:
    """Return the names of the neighbourhoods in the given data whose hypertension rate is >= threshold.

    The *hypertension rate* of a neighbourhood is defined as:

        (# people aged 20+ with hypertension) / (# people aged 20+)

    Preconditions:
    - data does not contain any duplicated neighbourhood names
    - 0.0 <= threshold <= 1.0

    >>> data = load_hypertension_data('datasets/part1/hypertension_data_small.csv')
    >>> result = high_hypertension_rate(data, 0.24)
    >>> result == {'Thistletown-Beaumond Heights', 'Rexdale-Kipling'}
    True
    """
    set_so_far = set()
    for row in data:
        if row.num_hypertension_all / row.num_all >= threshold:
            set_so_far.add(row.name)
    return set_so_far


def get_hypertension_rates(data: list[HypertensionData], age_group: str) -> dict[str, float]:
    """Return a dictionary mapping each given neighbourhood's name to the neighbourhood's hypertension rate
    for the given age group.

    age_group specifies which group to calculate the hypertension rates for, and can be one of:
        - '20+': all people aged 20+, i.e., the whole dataset
        - '20-44': only people aged 20-44
        - '45-64': only people aged 45-64
        - '65+': only people aged 65+

    Preconditions:
    - data does not contain any duplicated neighbourhood names
    - age_group in {'20+', '20-44', '45-64', '65+'}

    >>> data = load_hypertension_data('datasets/part1/hypertension_data_small.csv')
    >>> result = get_hypertension_rates(data, '65+')
    >>> len(result)  == 5
    True

    >>> round(result['Thistletown-Beaumond Heights'], 4)  # For testing purposes, round to 4 decimal places
    0.7634
    """
    dict_so_for = {}
    if age_group == '20+':
        for row in data:
            dict_so_for.update({row.name: row.num_hypertension_all / row.num_all})
        return dict_so_for
    elif age_group == '20-44':
        for row in data:
            dict_so_for.update({row.name: row.num_hypertension_20_44 / row.num_20_44})
        return dict_so_for
    elif age_group == '45-64':
        for row in data:
            dict_so_for.update({row.name: row.num_hypertension_45_64 / row.num_45_64})
        return dict_so_for
    else:
        for row in data:
            dict_so_for.update({row.name: row.num_hypertension_65_plus / row.num_65_plus})
        return dict_so_for

###############################################################################
# Part 1(c)
###############################################################################


@dataclass
class CombinedRateData:
    """A data class representing neighbourhood hypertension and low income rate data.

    Instance Attributes:
        - name: the name of the neighbourhood
        - hypertension_rate: the hypertension rate for a particular age group in the neighbourhood
            NOTE: this attribute will be used to store rates for different age groups,
                  e.g. "people aged 20+" or "people aged 45-64"
        - low_income_rate: the proportion of neighbourhood residents with low income status

    Representation Invariants:
    - 0.0 <= self.hypertension_rate <= 1.0
    - 0.0 <= self.low_income_rate <= 1.0
    """
    name: str
    hypertension_rate: float
    low_income_rate: float


def get_low_income_rates(data: list[LowIncomeData]) -> dict[str, float]:
    """This function evaluates low income rates for every village and presents
    the data in the form of a dictionary."""
    dict_so_far = {}
    for row in data:
        dict_so_far.update({row.name: row.num_low_income / row.population_total})
    return dict_so_far


def combine_rates(hypertension_data: list[HypertensionData],
                  low_income_data: list[LowIncomeData],
                  age_group: str) -> list[CombinedRateData]:
    """Return a list of CombinedRateData values for the neighbourhoods in both hypertension_data and low_income_data.

    The age_group parameter determines what age group to calculate hypertension rates for. It has the same
    meaning as the age_group parameter for get_hypertension_rates from Part 1(b).

    Review the above data class definition for CombinedRateData to understand what pieces of information each
    instance of CombinedRateData should store. To compute the low income rate, use the population total in
    the LowIncomeData instance.

    Note that you should NOT assume that hypertension_data and low_income_data store the same neighbourhoods,
    or have a particular order. If a neighbourhood appears in one of the input lists but not the other,
    that neighbourhood should NOT be included in the returned list.

    Preconditions:
    - neighbourhood names in hypertension_data are unique
    - neighbourhood names in low_income_data are unique
    - age_group in {'20+', '20-44', '45-64', '65+'}

    >>> example_hypertension_data = load_hypertension_data('datasets/part1/hypertension_data_small.csv')
    >>> example_low_income_data = load_low_income_data('datasets/part1/low_income_data_small.csv')
    >>> example_combined_data = combine_rates(example_hypertension_data, example_low_income_data, '20+')
    >>> len(example_combined_data)
    5

    HINTS:
    1. You may find the get_hypertension_rates function from above useful, and may wish to define a similar
       "get_low_income_rates" function.
    2. Remember that you can check whether a given value k is a key in a dictionary using the "in" operator.
    """
    list_so_for = []
    h_data = get_hypertension_rates(hypertension_data, age_group)
    i_data = get_low_income_rates(low_income_data)
    for village in h_data:
        if village in i_data:
            list_so_for += [CombinedRateData(village, h_data[village], i_data[village])]
    return list_so_for


def plot_combined_rates(neighbourhood_data: list[CombinedRateData], age_group: str) -> None:
    """Display a scatterplot of the neighbourhood low income rates vs. hypertension rates, using plotly.

    Also label each point in the scatterplot using the name of the neighbourhood.
    age_group is used to label the y-axis with the correct age group for the hypertension rates.

    Preconditions:
    - neighbourhood_data does not contain any duplicated neighbourhood names
    - age_group in {'20+', '20-44', '45-64', '65+'}

    NOTE: You should NOT modify this function, but should be able to (roughly) understand what
    it is doing.
    """
    figure = scatter(
        data_frame=neighbourhood_data,  # The data to plot (in our case, a list of data class instances)
        x='low_income_rate',            # The instance attribute name to use for x values
        y='hypertension_rate',          # The instance attribute name to use for y values
        hover_name='name',              # The instance attribute name to use for point labels
        title='Low Income vs. Hypertension Rates by Toronto Neighbourhood',  # The graph title
        labels={
            'low_income_rate': 'Proportion of Residents with Low Income Status',                  # Label for the x-axis
            'hypertension_rate': f'Proportion of Residents (aged {age_group}) with Hypertension'  # Label for the y-axis
        }
    )

    # Show the figure in the browser
    figure.show()
    # Is the above not working for you? Comment out that line of code, and uncomment the following line:
    # figure.write_html('my_figure.html')
    # This will create a new file called 'my_figure.html', which you can manually open in your web browser.


def part1_example(hypertension_file: str, low_income_file: str, age_group: str) -> None:
    """Display a scatterplot comparing the low income and hypertension rates in the given datasets.

    age_group is used to specify which age group to compute hypertension rates for.

    Preconditions:
    - age_group in {'20+', '20-44', '45-64', '65+'}
    - hypertension_file refers to a csv file whose format matches the hypertension dataset description
      on the assignment handout.
    - low_income_file refers to a csv file whose format matches the low income dataset description

    HINTS:
    - This is a "putting it all together" function, so the actual code here should be pretty
      simple, and mainly call functions you've already implemented above!
    """
    h_data = load_hypertension_data(hypertension_file)
    i_data = load_low_income_data(low_income_file)
    c_data = combine_rates(h_data, i_data, age_group)
    plot_combined_rates(c_data, age_group)


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)

    # When you are ready to check your work with python_ta, uncomment the following lines.
    # (In PyCharm, select the lines below and press Ctrl/Cmd + / to toggle comments.)
    import python_ta
    python_ta.check_all(config={
        'max-line-length': 120,
        'disable': ['too-many-instance-attributes'],
        'allowed-io': ['load_hypertension_data', 'load_low_income_data'],
        'extra-imports': ['csv', 'plotly.express'],
    })
