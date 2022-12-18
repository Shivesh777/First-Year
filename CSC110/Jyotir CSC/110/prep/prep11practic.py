"""CSC110: Food Delivery System Class
Copyright and Usage Information
===============================
This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.
This file is Copyright (c) 2021 David Liu, Mario Badr, and Tom Fairgrieve.
"""
from __future__ import annotations
import datetime
# This is the Python module containing the individual entity data classes.
from L30_entities import Restaurant, Customer, Courier, Order


class FoodDeliverySystem:
    """A system that maintains all entities (restaurants, customers, couriers, and
orders).
    Representation Invariants:
        - self.name != ''
        - all(r == self._restaurants[r].name for r in self._restaurants)
        - all(c == self._customers[c].name for c in self._customers)
        - all(c == self._couriers[c].name for c in self._couriers)
    """
    # Private Instance Attributes:
    #   - _restaurants: a mapping from restaurant name to Restaurant object.
    #       This represents all the restaurants in the system.
    #   - _customers: a mapping from customer name to Customer object.
    #       This represents all the customers in the system.
    #   - _couriers: a mapping from courier name to Courier object.
    #       This represents all the couriers in the system.
    #   - _orders: a list of all orders (both open and completed orders).
    _restaurants: dict[str, Restaurant]
    _customers: dict[str, Customer]
    _couriers: dict[str, Courier]
    _orders: list[Order]

    ###########################################################################
    # Exercise 2: Developing the FoodDeliverySystem class
    ###########################################################################
    def __init__(self) -> None:
        """Initialize a new food delivery system.
        The system starts with no entities.
        """


    def add_restaurant(self, restaurant: Restaurant) -> bool:
        """Add the given restaurant to this system.
        Do NOT add the restaurant if one with the same name already exists.
        Return whether the restaurant was successfully added to this system.
        """

    def add_customer(self, customer: Customer) -> bool:
        """Add the given customer to this system.
        Do NOT add the customer if one with the same name already exists.
        Return whether the customer was successfully added to this system.
        """

    def add_courier(self, courier: Courier) -> bool:
        """Add the given courier to this system.
        Do NOT add the courier if one with the same name already exists.
        Return whether the courier was successfully added to this system.
        """

    ###########################################################################
    # Exercise 3: Handling orders
    ###########################################################################
    def place_order(self, order: Order) -> bool:
        """Add an order to this system.
        Do NOT add the order if no couriers are available (i.e., are already
assigned orders).
        - If a courier is available, add the order and assign it a courier, and
return True.
        - Otherwise, do not add the order, and return False.
        Preconditions:
            - order not in self._orders
        """

    def complete_order(self, order: Order, timestamp: datetime.datetime) -> None:
        """Record that the given order has been delivered successfully at the given
timestamp.
        Make the courier who was assigned this order available to take a new order.
        TODO: in addition to implementing the function, add the following
preconditions:
            - the order is not already complete
            - the given timestamp is after the order's start time
              (you can use < to compare datetime.datetimes)
        """


if __name__ == '__main__':
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()
    import doctest

    doctest.testmod(verbose=True)
    # import python_ta
    # python_ta.check_all(config={
    #     'extra-imports': ['dataclasses', 'datetime', 'python_ta.contracts',
'math', 'L30_entities'],
#     'allowed-io': ['run_example'],
#     'max-line-length': 100,
#     'disable': ['R1705', 'C0200', 'R0201']
# })
