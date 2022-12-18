"""CSC110 Fall 2022: Food Delivery System Events

Module Description
==================

This module contains the class definitions of the various event classes
for our food delivery system. The first is the definition of an abstract
class Event, followed by concrete subclasses for different event types.

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
import random

from entities import Order, Vendor
from food_delivery_system import FoodDeliverySystem


class Event:
    """An abstract class representing an event in a food delivery simulation.

    Instance Attributes:
        - timestamp: the start time of the event
    """
    timestamp: datetime.datetime

    def __init__(self, timestamp: datetime.datetime) -> None:
        """Initialize this event with the given timestamp."""
        self.timestamp = timestamp

    def handle_event(self, system: FoodDeliverySystem) -> list[Event]:
        """Mutate the given food delivery system to process this event.

        Return a new list of new events created by processing this event.
        """
        raise NotImplementedError


class NewOrderEvent(Event):
    """An event representing when a customer places an order at a vendor."""
    # Private Instance Attributes:
    #   _order: the new order to be added to the FoodDeliverySystem
    _order: Order

    def __init__(self, order: Order) -> None:
        """Initialize a NewOrderEvent for the given order."""
        Event.__init__(self, order.start_time)
        self._order = order

    def handle_event(self, system: FoodDeliverySystem) -> list[Event]:
        """Mutate system by placing an order.

        If an order can be placed, return a CompleteOrderEvent based on an estimate of when the
        order will be completed.

        If the order cannot be placed, try to place it again in 5 minutes.
        """
        success = system.place_order(self._order)

        if success:
            # If the order was successfully placed, return a corresponding CompleteOrderEvent
            completion_time = self.timestamp + datetime.timedelta(minutes=random.randint(1, 30))
            # completion_time = self.timestamp + datetime.timedelta(minutes=10)
            return [CompleteOrderEvent(completion_time, self._order)]
        else:
            # If the order wasn't successfully placed, try to place the order again in 5 minutes
            self._order.start_time = self.timestamp + datetime.timedelta(minutes=5)
            return [NewOrderEvent(self._order)]

    def __str__(self) -> str:
        """Return a string representation for this event.

        Useful if we want to call print on the event.
        """
        return f'{self.timestamp}: New order from {self._order.customer.name} for {self._order.vendor.name}'


###############################################################################
# Lecture Exercise
###############################################################################
class CompleteOrderEvent(Event):
    """An event representing when an order is delivered to a customer by a courier."""
    # Private Instance Attributes:
    #   _order: the order to be completed by this event
    _order: Order

    def __init__(self, timestamp: datetime.datetime, order: Order) -> None:
        Event.__init__(self, timestamp)
        self._order = order

    def handle_event(self, system: FoodDeliverySystem) -> list[Event]:
        """Mutate the system by recording that the order has been delivered to the customer."""
        system.complete_order(self._order, self.timestamp)
        return []

    def __str__(self) -> str:
        """Return a string representation for this event.

        Useful if we want to call print on the event.
        """
        return f'{self.timestamp}: Order from {self._order.customer.name} was ' \
               f'completed by {self._order.courier.name}'


###############################################################################
# Lecture Exercise (Event for randomly generating orders)
###############################################################################
class GenerateOrdersEvent(Event):
    """An event that causes a random generation of new orders.

    Private Representation Invariants:
        - self._duration > 0
    """
    # Private Instance Attributes:
    #   - _duration: the number of hours to generate orders for
    _duration: int

    def __init__(self, timestamp: datetime.datetime, duration: int) -> None:
        """Initialize this event with timestamp and the duration in hours.

        Preconditions:
            - duration > 0
        """
        Event.__init__(self, timestamp)
        self._duration = duration

    def handle_event(self, system: FoodDeliverySystem) -> list[Event]:
        """Generate new orders for this event's timestamp and duration."""
        customers = system.get_customers()
        vendors = system.get_vendors()

        events = []  # Event accumulator

        current_time = self.timestamp
        end_time = self.timestamp + datetime.timedelta(hours=self._duration)

        while current_time < end_time:
            # Create a randomly-generated Order called new_order
            customer = random.choice(customers)
            vendor = random.choice(vendors)
            food_items = {}  # This is a simple version
            new_order = Order(customer=customer, vendor=vendor, food_items=food_items,
                              start_time=current_time)

            new_order_event = NewOrderEvent(new_order)
            events.append(new_order_event)

            # Update current_time
            current_time = current_time + datetime.timedelta(minutes=random.randint(1, 60))

        return events

    def __str__(self) -> str:
        """Return a string representation for this event.

        Useful if we want to call print on the event.
        """
        return f'{self.timestamp}: Generating new orders (up to {self._duration} hours)'
