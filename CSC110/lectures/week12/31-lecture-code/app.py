"""Lecture 31: Example Webserver for our food delivery system

NOTES:
    - This requires the Python library "flask" to be installed.

Example web server for our food delivery system
"""
import datetime
import random

from flask import Flask, redirect, render_template, Response, request, url_for

from food_delivery_system import FoodDeliverySystem
from entities import Courier, Customer, Order, Vendor

app = Flask(__name__)

# Note: This is a top-level global variable, which we have generally discouraged in this course.
# We're using it here as a convenient way to keep track of data across multiple requests,
# but in practice this would be done with a database.
SYSTEM = FoodDeliverySystem()


@app.route('/')
def home() -> str | Response:
    """Display the home page."""
    return render_template('home.html')


@app.route('/vendors')
def vendors() -> str | Response:
    """Display all vendors."""
    return render_template('vendors.html', vendors=SYSTEM.get_vendors())


@app.route('/orders')
def orders() -> str | Response:
    """Display all orders."""
    return render_template('orders.html', orders=SYSTEM.get_orders())


@app.route('/place_order', methods=['GET', 'POST'])
def place_order() -> str | Response:
    """Handle users placing orders."""
    if request.method == 'GET':
        vendor_name = request.args.get('vendor')
        vendor = SYSTEM.get_vendor(vendor_name)
        app.logger.warning(vendor)
        return render_template('place_order.html', vendor=vendor)
    else:
        # Process the form data
        vendor_name = request.form['vendor-name']
        vendor = SYSTEM.get_vendor(vendor_name)
        customer_name = request.form['customer-name']
        try:
            customer = SYSTEM.get_customer(customer_name)
        except KeyError:
            # Create a new customer with a random location
            customer = Customer(name=customer_name,
                                location=(random.uniform(42.0, 44.0), random.uniform(78.0, 80.0)))
        food_items = {}
        for food in vendor.menu:
            quantity = int(request.form[f'{food}-quantity'])
            if quantity > 0:
                food_items[food] = quantity

        new_order = Order(customer=customer, vendor=vendor, food_items=food_items,
                          start_time=datetime.datetime.now())

        SYSTEM.place_order(new_order)
        return redirect(url_for('home'))


###############################################################################
# Helper function for populating the food delivery system with some fake data
###############################################################################
def populate_system(system: FoodDeliverySystem) -> None:
    """Populate the system with fake vendors and couriers."""
    for i in range(0, 100):
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


if __name__ == '__main__':
    populate_system(SYSTEM)

    app.run()
