from __future__ import annotations
# needed so that Order can refer to Courier

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
      - -90 <= self.location[0] <= 90
      - -180 <= self.location[1] <= 180
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
    """
    customer: Customer
    vendor: Vendor
    food_items: dict[str, int]
    start_time: datetime.datetime
    courier: Optional[Courier] = None
    end_time: Optional[datetime.datetime] = None

###############################################################################
# Exercise 1: Designing a `Courier` data class
###############################################################################
@dataclass
class Courier:
    """A person who delivers food orders from vendors to customers.

    Instance Attributes:
        - name: the name of the courier
        - location: the location of the courier as (latitude, longitude)
        - order: the order that the courier is currently assigned to

    Representation Invariants:
        - self.name != ''
        - -90 <= self.location[0] <= 90
        - -180 <= self.location[1] <= 180

        - self.order is None or self.order.courier is self



    >>> courier = Courier('Courier 1', (44.639, -79.215))
    >>> courier.order is None
    True
    """
    name: str
    location: tuple[float, float]
    order: Optional[Order] = None

    # Can two `Order` objects refer to the same `Courier` instance? Why or why not?

    # Yes.
    # The representation invariant in 2 is added to `Courier`, and so we can only
    # check that courier's `order` attribute.
    # If another `Order` object also referred to the same `Courier` object, there
    # would be no way to know (from inside the `Courier` class).
    #
    # But, if a similar representation invariant is added to `Order`, then the answeri
    # changes to No.

    # See posted diagram

    # other possible instance attributes
    # - type of vehicle
    # - average speed
    # - working vs. not working (i.e., available)
    # - max radius
    # - et cetera

