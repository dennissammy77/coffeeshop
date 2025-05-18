#!/usr/bin/env python3
from lib.models import (
    Order,
    Coffee,
    Customer
)
if __name__ == "__main__":
    print("GHello World")
    customer = Customer("Dennis")
    coffee = Coffee("Cappucino")
    order = Order(customer, coffee, 10.12)

    print(customer.coffees("Dennis"))