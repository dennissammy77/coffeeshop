#!/usr/bin/env python3
from lib.models import (
    Order,
    Coffee,
    Customer
)

if __name__ == "__main__":
    c1 = Customer("Alice")
    c2 = Customer("Bob")

    latte = Coffee("Latte")
    mocha = Coffee("Mocha")

    c1.create_order(latte, 3.5)
    c1.create_order(latte, 3.5)
    c1.create_order(mocha, 4.0)
    c1.create_order(mocha, 4.0)
    c2.create_order(latte, 5.0)
    c2.create_order(latte, 5.0)

    print('*************Customer*****************')
    print(c1.coffees())
    for order in c1.orders():
        print({"coffee": order.coffee.name, "price": order.price})
    
    most_aficionado = Customer.most_aficionado(latte)
    print(None if None else most_aficionado.name)
    # Coffee
    print('*************Coffee*****************')
    print('coffee number of orders:',latte.num_orders())
    print('coffee orders:')
    for order in latte.orders():
        print({"customer": order.customer.name,"coffee": order.coffee.name, "price": order.price})
    
    print('coffee customers:',latte.customers())
    print('coffeeaverage price:',latte.average_price())

    print('*************Orders*****************')
    for order in Order.all:
        print({"customer": order.customer.name,"coffee": order.coffee.name, "price": order.price})