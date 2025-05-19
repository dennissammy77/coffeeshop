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
    Order.all = []
    """Test orders method returns a list of all orders for that customer. """
    customer = Customer("Dennis")
    coffee = Coffee("Cappucino")
    order = Order(customer, coffee, 10.12)
    
    assert customer.orders("Dennis") == [order]

def test_coffees():
    Order.all = []
    """Test coffees method returns a unique list of all coffees for that customer. """
    customer = Customer("Dennis")
    customer1 = Customer("Alex")
    coffee1 = Coffee("Cappucino")
    coffee2 = Coffee("Espresso")
    order1 = Order(customer, coffee1, 10.12)
    order2 = Order(customer, coffee2, 10.12)
    order3 = Order(customer1, coffee2, 10.12)
    
    assert sorted(customer.coffees()) == sorted([coffee2.name,coffee1.name])

def test_create_order():
    Order.all = []
    """Test that create_order method creates a new Order with the specified Coffee and price,
    and associates it with the correct Customer."""
    customer = Customer("Dennis")
    coffee = Coffee("Cappucino")
    customer.create_order(coffee,12.0)
    assert Order.all[0].customer.name == customer.name

def test_most_aficionado_returns_customer_who_spent_most_on_coffee():
    Order.all = []
    Customer.all = []
    """Test that most_aficionado method returns the Customer who spent the most money on a given Coffee instance,
    and returns None if no orders exist for that coffee."""
    customer = Customer("Dennis")
    customer1 = Customer("Alex")
    coffee = Coffee("Cappucino")
    customer.create_order(coffee,12.0)
    customer1.create_order(coffee,12.0)
    customer.create_order(coffee,12.0)

    assert Customer.most_aficionado(coffee) == customer
