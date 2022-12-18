"""CSC110 Fall 2022: Food Delivery System Class

Module Description
==================

This module contains the FoodDeliverySystem class, which is responsible for
managing all entities in our food delivery system.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2022 David Liu and Mario Badr.
"""
from __future__ import annotations

import datetime
import logging  # NEW!
from typing import Optional

from entities import Vendor, Customer, Courier, Order


class FoodDeliverySystem:
    """A system that maintains all entities (vendors, customers, couriers, and orders).

    Representation Invariants:
        - all(vendor == self._vendors[vendor].name for vendor in self._vendors)
        - all(customer == self._customers[customer].name for customer in self._customers)
        - all(courier == self._couriers[courier].name for courier in self._couriers)
    """
    # Private Instance Attributes:
    #   - _vendors: a mapping from vendor name to Vendor object.
    #       This represents all the vendors in the system.
    #   - _customers: a mapping from customer name to Customer object.
    #       This represents all the customers in the system.
    #   - _couriers: a mapping from courier name to Courier object.
    #       This represents all the couriers in the system.
    #   - _orders: a list of all orders (both open and completed orders).
    _vendors: dict[str, Vendor]
    _customers: dict[str, Customer]
    _couriers: dict[str, Courier]
    _orders: list[Order]

    def __init__(self) -> None:
        """Initialize a new food delivery system.

        The system starts with no entities.
        """
        self._vendors = {}
        self._customers = {}
        self._couriers = {}
        self._orders = []

    def add_vendor(self, vendor: Vendor) -> bool:
        """Add the given vendor to this system.

        Do NOT add the vendor if one with the same name already exists.

        Return whether the vendor was successfully added to this system.
        """
        if vendor.name in self._vendors:
            return False
        else:
            logging.info(f'Added vendor with name {vendor.name}')
            self._vendors[vendor.name] = vendor
            return True

    def add_customer(self, customer: Customer) -> bool:
        """Add the given customer to this system.

        Do NOT add the customer if one with the same name already exists.

        Return whether the customer was successfully added to this system.
        """
        if customer.name in self._customers:
            return False
        else:
            logging.info(f'Added customer with name {customer.name}')
            self._customers[customer.name] = customer
            return True

    def add_courier(self, courier: Courier) -> bool:
        """Add the given courier to this system.

        Do NOT add the courier if one with the same name already exists.

        Return whether the courier was successfully added to this system.
        """
        if courier.name in self._couriers:
            return False
        else:
            logging.info(f'Added courier with name {courier.name}')
            self._couriers[courier.name] = courier
            return True

    def place_order(self, order: Order) -> bool:
        """Add an order to this system.

        Do NOT add the order if no couriers are available (i.e., are already assigned orders).

        - If a courier is available, add the order and assign it a courier, and return
          an estimate of how long the order will take to be delivered (in seconds).
        - Otherwise, do not add the order, and return None.

        Preconditions:
            - order not in self._orders
        """
        # Find an available courier and assign them to the order.
        # If there are no couriers available, None is returned.
        courier = self._assign_courier(order)

        if courier is None:
            return False
        else:
            # Only add the order if it was assigned a courier.
            logging.info(f'Placed order from {order.customer.name} for {order.vendor.name}. '
                         f'Items ordered: {order.food_items}.')
            self._orders.append(order)
            return True

    def _assign_courier(self, order: Order) -> Optional[Courier]:
        """Find an available courier and assign the order to them.

        Return the courier assigned to the order, or None if no courier was
        available.
        """
        for _, courier in self._couriers.items():
            if courier.current_order is None:
                order.courier = courier
                courier.current_order = order

                return courier

        return None

    def complete_order(self, order: Order, timestamp: datetime.datetime) -> None:
        """Record that the given order has been delivered successfully at the given timestamp.

        Make the courier who was assigned this order available to take a new order.

        Preconditions:
            - order in self._orders
            - order.end_time is None
            - order.start_time < timestamp
        """
        logging.info(f'Completed order for {order.customer.name}. Order delivered by {order.courier.name}')
        order.courier.current_order = None
        order.end_time = timestamp

    ###########################################################################
    # Additional (helpful) methods
    ###########################################################################
    def get_vendors(self) -> list[Vendor]:
        """Return a list of all vendors registered with this system."""
        return list(self._vendors.values())

    def get_customers(self) -> list[Customer]:
        """Return a list of all customers registered with this system."""
        return list(self._customers.values())

    def get_orders(self) -> list[Order]:
        """Return a list of all orders placed in this system."""
        return self._orders

    def completed_orders(self) -> list[Order]:
        """Return a list of all the completed orders by this system."""
        return [order for order in self._orders if order.end_time is not None]

    def get_customer(self, name: str) -> Customer:
        """Return the customer with the given name.

        Preconditions:
        - a customer with the given name exists
        """
        return self._customers[name]

    def get_vendor(self, name: str) -> Vendor:
        """Return the food vendor with the given name.

        Preconditions:
        - a vendor with the given name exists
        """
        return self._vendors[name]

    def get_courier(self, name: str) -> Courier:
        """Return the courier with the given name.

        Preconditions:
        - a courier with the given name exists
        """
        return self._couriers[name]


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
