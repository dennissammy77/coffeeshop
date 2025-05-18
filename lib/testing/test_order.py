from lib.models import (
    Order,
    Customer,
    Coffee
)
import pytest

def test_order_init():
    """Test Order class initializes with customer, coffee, price"""
    customer = Customer("Dennis")
    coffee = Coffee("Cappucino")
    order = Order(customer, coffee, 10.12)

    assert order._customer == customer
    assert order._coffee == coffee
    assert order._price == 10.12