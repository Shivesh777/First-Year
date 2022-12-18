"""Lecture 30 (Food delivery system and simulation examples)
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

        # Create the order
        new_order = Order(
            customer=customer,
            vendor=vendor,
            food_items={'Chocolate': random.randint(0, 10)},
            start_time=datetime.datetime(2022, 12, 1)
        )
        system.place_order(new_order)

    return system
