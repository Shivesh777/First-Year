"""CSC110 Fall 2022: Food Delivery Simulation

Module Description
==================

This contains code for running the discrete-event simulation. We've provided
two functions of the main simulation loop:

1. A top-level function called run_simulation, paired with a run_example function
   to demonstrate how it can be used.
2. A class called FoodDeliverySimulation (not to be confused with FoodDeliverySystem),
   which contains a run method that's analogous to run_simulation, but also has additional
   methods for starting up the simulation and running it.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC110 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited. For more information on copyright for CSC110 materials,
please consult our Course Syllabus.

This file is Copyright (c) 2022 David Liu and Mario Badr.
"""
import datetime
import random

from entities import Courier, Customer, Vendor, Order
from food_delivery_system import FoodDeliverySystem
from events import Event, GenerateOrdersEvent
from event_queue import EventQueue, EventQueueList, EventQueueHeap


###############################################################################
# Function version of simulation
###############################################################################
def run_simulation(initial_events: list[Event],
                   system: FoodDeliverySystem) -> None:
    """Main function for running a simulation."""
    # events = EventQueueList()
    events = EventQueueHeap()
    for event in initial_events:
        events.enqueue(event)

    while not events.is_empty():
        event = events.dequeue()

        new_events = event.handle_event(system)
        for new_event in new_events:
            events.enqueue(new_event)


def run_example_simulation() -> FoodDeliverySystem:
    """Run an example simulation. Return the final food delivery system.
    """
    system = FoodDeliverySystem()

    # Add 100 random customers, vendors, and couriers
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

    # Create a single GenerateOrdersEvent to start the simulation
    initial_event = GenerateOrdersEvent(datetime.datetime(2022, 12, 1), 100)
    run_simulation([initial_event], system)

    return system


if __name__ == '__main__':
    # Demo with logging module!
    import logging
    logging.basicConfig(level='INFO')
    run_example_simulation()
