"""Lecture 31 Examples: Data Analysis on the Food Delivery System

Notes:
    - This requires the Python library "pandas" to be installed.
"""
from food_delivery_system import FoodDeliverySystem
from entities import Order

import pandas


def get_orders_dataframe(system: FoodDeliverySystem) -> pandas.DataFrame:
    """Return a pandas DataFrame containin a record of all orders in the system.
    """
    all_orders = [process_order(order) for order in system.get_orders()]

    return pandas.DataFrame(all_orders)


def process_order(order: Order) -> dict:
    """Return a dict representation of the given order.

    Simplifies data:
       - only records the name of each customer, vendor, and food item
       - only records the total number of food items ordered
    """
    result = {
        'customer': order.customer.name,
        'vendor': order.vendor.name,
        'food_items': sum(order.food_items[food] for food in order.food_items),
        'start_time': order.start_time
    }

    if order.courier is None:
        result['courier'] = None
    else:
        result['courier'] = order.courier.name

    if order.end_time is None:
        result['end_time'] = None
    else:
        result['end_time'] = order.end_time

    return result


if __name__ == '__main__':
    from simulation import run_example_simulation

    my_system = run_example_simulation()

    order_data = get_orders_dataframe(my_system)
    print(order_data)
