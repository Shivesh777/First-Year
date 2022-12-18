"""Lecture 29 (Food Delivery System)
"""
import datetime
from typing import Optional


from entities import Courier, Customer, Order, Vendor


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

    ###########################################################################
    # Lecture Exercises
    ###########################################################################
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
        if vendor.name in self._vendors:  # Vendor with the same name already exists
            return False
        else:    # Vendor doesn't already exist
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
            self._couriers[courier.name] = courier
            return True

    def place_order(self, order: Order) -> bool:
        """Add an order to this system.

        Do NOT add the order if no couriers are available (i.e., are already assigned orders).

        - If a courier is available, add the order and assign it a courier, and return True.
        - Otherwise, do not add the order, and return False.
        """
        # Find an available courier and assign them to the order.
        # If there are no couriers available, None is returned.
        courier = self._assign_courier(order)

        if courier is None:
            return False
        else:
            # Only add the order if it was assigned a courier.
            self._orders.append(order)
            return True

    def _assign_courier(self, order: Order) -> Optional[Courier]:
        """Find an available courier and assign the order to them.

        Return the courier assigned to the order, or None if no courier was
        available.

        Note that this is a private method: it is only meant to be used as a helper
        method for place_order.
        """
        for name in self._couriers:
            courier = self._couriers[name]
            if courier.current_order is None:
                order.courier = courier
                courier.current_order = order

                return courier

        return None

    # NOTE: this method does not use "self", so technically could be a top-level function.
    def complete_order(self, order: Order, timestamp: datetime.datetime) -> None:
        """Record that the given order has been delivered successfully at the given timestamp.

        Make the courier who was assigned this order available to take a new order.

        Preconditions:
            - order in self._orders
            - order.end_time is None
            - order.start_time < timestamp
        """
        # Set the courier's current order back to None
        order.courier.current_order = None

        # Alternate version:
        # assigned_courier = order.courier
        # assigned_courier.current_order = None

        # Set the order's end time.
        order.end_time = timestamp

    ###########################################################################
    # Additional methods used for events
    ###########################################################################
    def get_vendors(self) -> list[Vendor]:
        """Return a list of all vendors registered with this system."""
        return list(self._vendors.values())

    def get_customers(self) -> list[Customer]:
        """Return a list of all customers registered with this system."""
        return list(self._customers.values())

    ###########################################################################
    # Additional methods used for example runners
    ###########################################################################
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

    # print(f'Order placed for {order.customer.name} from {order.vendor.name} at {order.start_time}. '
    #       f'Assigned to {order.courier.name}.')
