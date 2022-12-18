"""Lecture 30 (Food delivery system and simulation examples)

Some new Python features we encourage you to read more about:
    - f-strings ("format strings"), to combine string literals with Python expressions,
      e.g. f'Customer {i}'
    - datetime.timedelta, to represent a difference in time (can be added to datetime.datetime objects)
    - random.uniform, to generate random floats
"""
import datetime
import random

from entities import Courier, Customer, Order, Vendor
from food_delivery_system import FoodDeliverySystem


def run_example() -> FoodDeliverySystem:
    """This is an example for creating objects in our system."""
    # Create the system
    system = FoodDeliverySystem()

    # Add customers, vendors, and couriers
    for i in range(0, 100):
        customer = Customer(
            name=f'Customer {i}',
            location=(random.uniform(42.0, 44.0), random.uniform(78.0, 80.0))
        )
        system.add_customer(customer)

        vendor = Vendor(
            name=f'Vendor {i}',
            address=f'{random.randint(1, 1000)} College St.',
            location=(random.uniform(42.0, 44.0), random.uniform(78.0, 80.0)),
            menu={'Chocolate': random.uniform(1.0, 100.0)}
        )
        system.add_vendor(vendor)

        courier = Courier(
            name=f'Courier {i}',
            location=(random.uniform(42.0, 44.0), random.uniform(78.0, 80.0))
        )
        system.add_courier(courier)

    # Place some orders
    for _ in range(0, 10):
        # Pick a random customer and vendor
        customer = system.get_customer(f'Customer {random.randint(0, 99)}')
        vendor = system.get_vendor(f'Vendor {random.randint(0, 99)}')

        # Equivalent to:
        # customer = system._customers[f'Customer {random.randint(0, 99)}']
        # vendor = system._vendors[f'Vendor {random.randint(0, 99)}']

        # Create the order
        new_order = Order(
            customer=customer,
            vendor=vendor,
            food_items={'Chocolate': random.randint(0, 10)},
            start_time=datetime.datetime(2022, 12, 1)
        )
        system.place_order(new_order)

    return system


###############################################################################
# Second example, with an event queue
###############################################################################
from events import Event, GenerateOrdersEvent
from event_queue import EventQueueList


def run_simulation(initial_events: list[Event],
                   system: FoodDeliverySystem) -> None:
    """Main function for running a simulation."""
    events = EventQueueList()
    for event in initial_events:
        events.enqueue(event)

    while not events.is_empty():
        event = events.dequeue()
        print(event)  # This is just for showing each event as it's processed

        new_events = event.handle_event(system)
        for new_event in new_events:
            events.enqueue(new_event)


def run_example_2() -> FoodDeliverySystem:
    """This is an example for running a discrete event simulation
    """
    # Create the system (this part is the same as before)
    system = FoodDeliverySystem()

    # Add customers, vendors, and couriers
    for i in range(0, 100):
        customer = Customer(
            name=f'Customer {i}',
            location=(random.uniform(42.0, 44.0), random.uniform(78.0, 80.0))
        )
        system.add_customer(customer)

        vendor = Vendor(
            name=f'Vendor {i}',
            address=f'{random.randint(1, 1000)} College St.',
            location=(random.uniform(42.0, 44.0), random.uniform(78.0, 80.0)),
            menu={'Chocolate': random.uniform(1.0, 100.0)}
        )
        system.add_vendor(vendor)

        courier = Courier(
            name=f'Courier {i}',
            location=(random.uniform(42.0, 44.0), random.uniform(78.0, 80.0))
        )
        system.add_courier(courier)

    # NEW: create an initial event
    initial_event = GenerateOrdersEvent(datetime.datetime(2022, 12, 1), 100)
    run_simulation([initial_event], system)

    return system
