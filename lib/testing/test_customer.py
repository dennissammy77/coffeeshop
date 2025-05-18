from lib.models import (
    Order,
    Coffee,
    Customer
)
import pytest

def test_customer_init():
    """Test Customer class initializes with name"""
    customer = Customer("Dennis")
    assert customer.name == "Dennis"

def test_customer_string():
    """Test Customer class name initializer is a string"""
    customer = Customer("Dennis")
    assert isinstance(customer.name, str) == True

def test_customer_name_length():
    """Test Customer class name initializer character length is between 1 and 15"""
    customer = Customer("Dennis")
    assert len(customer.name) > 1 and len(customer.name) < 25

def test_orders():
    """Test orders method returns a list of all orders for that customer. """
    customer = Customer("Dennis")
    coffee = Coffee("Cappucino")
    order = Order(customer, coffee, 10.12)
    assert Customer.orders() == [order]