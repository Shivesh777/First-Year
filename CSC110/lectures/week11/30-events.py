"""Lecture 30 (Events)

This is the code for Event and its subclasses from lecture, with the following modifications:

- I included a solution implementation for GenerateOrdersEvent.handle_events, but I strongly
  suggest trying to implement it yourself first for practice!!
- I added a __str__ method implementation for each Event subclass. This isn't technically necessary
  for the simulation, but because print(event) calls event.__str__(), these methods make
  printing the events in the run_simulation loop look nicer. :)
"""
from __future__ import annotations

import datetime
import random

from entities import Order
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

        (NEW) Return a new list of new events created by processing
        this event.
        """
        raise NotImplementedError


class NewOrderEvent(Event):
    """An event representing when a customer places an order at a vendor."""
    # Private Instance Attributes:
    #   _order: the new order to be added to the FoodDeliverySystem
    _order: Order

    def __init__(self, order: Order) -> None:
        """Initialize a NewOrderEvent for the given order."""
        self._order = order   # This initializes self._order

        Event.__init__(self, order.start_time)   # This initializes self.timestamp

        # This works, but is not the best practice
        # self.timestamp = order.start_time

    def handle_event(self, system: FoodDeliverySystem) -> list[Event]:
        """Mutate system by placing an order.

        (NEW) Return a new list of new events created by processing
        this event.
        """
        # NOTE: we should modify this code in case system.place_order returns False!
        # What might we do in that case?
        system.place_order(self._order)
        future_complete_time = self.timestamp + datetime.timedelta(minutes=1)
        complete_event = CompleteOrderEvent(future_complete_time, self._order)
        return [complete_event]

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
        """Mutate the system by recording that the order has been delivered to the customer.

        (NEW) Return a new list of new events created by processing
        this event.
        """
        system.complete_order(self._order, self.timestamp)
        return []  # Trigger no new events

        # Other possibilities:
        # Place an order at the same restaurant in the future
        # Place 5 orders at a competing restaurant

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
        # Conceptual idea (simple)
        # new_events = []
        #
        # for i in range(0, self._duration):
        #     new_event = NewOrderEvent(...)
        #     new_events.append(new_event)
        #
        # return new_events

        # Actual implementation
        customers = system.get_customers()
        vendors = system.get_vendors()

        events = []  # Event accumulator

        current_time = self.timestamp
        end_time = self.timestamp + datetime.timedelta(hours=self._duration)

        while current_time < end_time:
            # Create a randomly-generated Order called new_order.
            # Note the use of random.choice, which returns a random element from its argument list
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
