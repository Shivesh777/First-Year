"""CSC110 Fall 2022: Food Delivery System Entities

Module Description
==================

This module contains the data classes used to represent the individual entities
in our food delivery system.

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

from dataclasses import dataclass
import datetime
from typing import Optional


@dataclass
class Vendor:
    """A vendor that sells groceries or meals.

    This could be a grocery store or restaurant.

    Instance Attributes:
      - name: the name of the vendor
      - address: the address of the vendor
      - menu: the menu of the vendor with the name of the food item mapping to
              its price
      - location: the location of the vendor as (latitude, longitude)

    Representation Invariants:
      - self.name != ''
      - self.address != ''
      - all(self.menu[item] >= 0 for item in self.menu)
      - -90.0 <= self.location[0] <= 90.0
      - -180.0 <= self.location[1] <= 180.0

    Sample Usage:
    >>> mcdonalds = Vendor(name='McDonalds', address='160 Spadina Ave',\
                           menu={'fries': 4.5}, location=(43.649, -79.397))
    """
    name: str
    address: str
    menu: dict[str, float]
    location: tuple[float, float]  # (lat, lon) coordinates


@dataclass
class Customer:
    """A person who orders food.

    Instance Attributes:
      - name: the name of the customer
      - location: the location of the customer as (latitude, longitude)

    Representation Invariants:
      - self.name != ''
      - -90.0 <= self.location[0] <= 90.0
      - -180.0 <= self.location[1] <= 180.0

    Sample Usage:

    >>> david = Customer('David', (44.649, -79.115))
    """
    name: str
    location: tuple[float, float]


@dataclass
class Order:
    """A food order from a customer.

    Instance Attributes:
      - customer: the customer who placed this order
      - vendor: the vendor that the order is placed for
      - food_items: a mapping from names of food to the quantity being ordered
      - start_time: the time the order was placed
      - courier: the courier assigned to this order (initially None)
      - end_time: the time the order was completed by the courier (initially None)

    Representation Invariants:
      - all(self.food_items[item] >= 1 for item in self.food_items)

    Sample Usage:

    >>> david = Customer('David', (43.671, -79.413))
    >>> mcdonalds = Vendor(name='McDonalds', address='160 Spadina Ave',\
                           menu={'fries': 4.5}, location=(43.649, -79.397))
    >>> order = Order(customer=david, vendor=mcdonalds,\
                      food_items={'fries': 10},\
                      start_time=datetime.datetime(2020, 11, 5, 11, 30))
    >>> order.courier is None  # Illustrating default values
    True
    >>> order.end_time is None
    True
    """
    customer: Customer
    vendor: Vendor
    food_items: dict[str, int]
    start_time: datetime.datetime
    courier: Optional[Courier] = None
    end_time: Optional[datetime.datetime] = None


@dataclass
class Courier:
    """A person who delivers food orders from vendors to customers.

    Instance Attributes:
      - name: the name of the courier
      - location: the location of the courier as (latitude, longitude)
      - current_order: the order that the courier is currently assigned to,
                       or None if the courier is not assigned to any order

    Representation Invariants:
      - self.name != ''
      - -90 <= self.location[0] <= 90
      - -180 <= self.location[1] <= 180
      - self.current_order is None or self.current_order.courier is self
    """
    name: str
    location: tuple[float, float]
    current_order: Optional[Order] = None


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
