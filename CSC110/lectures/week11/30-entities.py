"""Lecture 29 (Food Delivery System Entities)
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
    """
    customer: Customer
    vendor: Vendor
    food_items: dict[str, int]  # The food items and their quantities
    start_time: datetime.datetime
    courier: Optional[Courier] = None
    end_time: Optional[datetime.datetime] = None


###############################################################################
# Lecture Exercise
###############################################################################
@dataclass
class Courier:
    """A person who delivers food orders from vendors to customers.

    Instance Attributes:
      - name: the name of the courier
      - location: the location of the courier as (latitude, longitude)
      - current_order: the order that the courier is currently assigned to,
                       or None if the courier is not assigned to any order

    Representation Invariants:
      - (in English)
          IF self.current_order is not None,
          THEN the order's courier is equal to self

          (p => q) <=> ((not p) or q)

      - (in Python)
          (self.current_order is None) or (self.current_order.courier == self)
          (self.current_order is None) or (self.current_order.courier is self)  <-- This one is better, because it's checking whether the objects are the same (in memory)
    """
    name: str
    location: tuple[float, float]
    current_order: Optional[Order] = None


if __name__ == '__main__':
    import doctest
    doctest.testmod(verbose=True)
