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
    """A system that maintains all entities (restaurants, customers, couriers, and orders).

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
        self._restaurants = {}
        self._customers = {}
        self._couriers = {}
        self._orders = []

    def add_restaurant(self, restaurant: Restaurant) -> bool:
        """Add the given restaurant to this system.

        Do NOT add the restaurant if one with the same name already exists.

        Return whether the restaurant was successfully added to this system.
        """
        if restaurant.name in self._restaurants:
            return False

        self._restaurants[restaurant.name] = restaurant
        return True

    def add_customer(self, customer: Customer) -> bool:
        """Add the given customer to this system.

        Do NOT add the customer if one with the same name already exists.

        Return whether the customer was successfully added to this system.
        """
        if customer.name in self._customers:
            return False

        self._customers[customer.name] = customer
        return True

    def add_courier(self, courier: Courier) -> bool:
        """Add the given courier to this system.

        Do NOT add the courier if one with the same name already exists.

        Return whether the courier was successfully added to this system.
        """
        if courier.name in self._couriers:
            return False

        self._couriers[courier.name] = courier
        return True

    ###########################################################################
    # Exercise 3: Handling orders
    ###########################################################################
    def place_order(self, order: Order) -> bool:
        """Add an order to this system.

        Do NOT add the order if no couriers are available (i.e., are already assigned orders).

        - If a courier is available, add the order and assign it a courier, and return True.
        - Otherwise, do not add the order, and return False.

        Preconditions:
            - order not in self._orders
        """
        # available_couriers = []
        # for courier in self._couriers:
        #     if self._couriers[courier].current_order is None:
        #         available_couriers.append(self._couriers[courier])
        #
        # if available_couriers == []:
        #     return False
        #
        # available_couriers[0].current_order = order
        # order.courier = available_couriers[0]
        # self._orders.append(order)
        # return True

        for _, courier in self._couriers.items():
            if courier.current_order is None:
                order.courier = courier
                courier.current_order = order
                self._orders.append(order)
                return True

        return False

    def complete_order(self, order: Order, timestamp: datetime.datetime) -> None:
        """Record that the given order has been delivered successfully at the given timestamp.

        Make the courier who was assigned this order available to take a new order.

        Preconditions:
            - order.end_time is None
            - order.start_time < timestamp
        """
        order.end_time = timestamp
        order.courier.current_order = None
        order.courier = None

    def get_customers(self) -> list[Customer]:
        return [self._customers[name] for name in self._customers]


if __name__ == '__main__':
    import python_ta.contracts

    python_ta.contracts.DEBUG_CONTRACTS = False
    python_ta.contracts.check_all_contracts()

    import doctest

    doctest.testmod(verbose=True)

    # import python_ta
    # python_ta.check_all(config={
    #     'extra-imports': ['dataclasses', 'datetime', 'python_ta.contracts', 'math', 'L30_entities'],
    #     'allowed-io': ['run_example'],
    #     'max-line-length': 100,
    #     'disable': ['R1705', 'C0200', 'R0201']
    # })
