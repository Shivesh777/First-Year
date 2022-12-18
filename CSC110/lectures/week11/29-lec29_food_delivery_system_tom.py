from __future__ import annotations

import datetime

# This is the Python module containing the individual entity data classes.
from lec29_entities_tom import Vendor, Customer, Courier, Order

class FoodDeliverySystem:
    """A system that maintains all entities (vendors, customers, couriers, and orders).

    Representation Invariants:
        - self.name != ''  # note - name not set anywhere! will fix
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
        if vendor.name in self._vendors:
            return False
        else:
            self._vendors[vendor.name] = vendor
            return True

    def add_customer(self, customer: Customer) -> bool:
        """Add the given customer to this system.

        Do NOT add the customer if one with the same name already exists.

        Return whether the customer was successfully added to this system.
        """
        # Similar implementation to add_vendor
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
        # Similar implementation to add_vendor
        if courier.name in self._couriers:
            return False
        else:
            self._couriers[courier.name] = courier
            return True


    def place_order(self, order: Order) -> bool:
        """Add an order to this system.

        Do NOT add the order if no couriers are available
        (i.e., are already assigned orders).

        - If a courier is available, add the order and assign
          it a courier, and return True.
        - Otherwise, do not add the order, and return False.
        """
        # for k in self._couriers:
        #     courier = self._couriers[k]
        #     ...
        # for courier in self._couriers.values():
        #     ...
        for _, courier in self._couriers:
            # this iterates over all key-value pairs in the dict
            # but only makes use of the value (a Courier)
            if courier.order is None:
                self._orders.append(order)
                order.courier = courier
                courier.order = order

                return True

        return False


    def complete_order(self, order: Order,
                       timestamp: datetime.datetime) -> None:
        """Record that the given order has been delivered
        successfully at the given timestamp.

        Make the courier who was assigned this order available
        to take a new order.

        Preconditions:
            - order in self._orders
            - order.end_time is None
            - order.start_time < timestamp
        """
        # Implementation note: it is possible to implement this method without
        # using the "self" at all, which is okay.
        order.courier.order = None
        order.end_time = timestamp
