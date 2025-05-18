from lib.models import (
    Coffee,
    Customer,
    Order
)

def test_coffee_init():
    """Test coffee class initializes with name"""
    coffee = Coffee("Cappuccino")
    assert coffee.name == "Cappuccino"

def test_coffee_string():
    """Test coffee class name initializer is a string"""
    coffee = Coffee("Cappuccino")
    assert isinstance(coffee.name, str) == True

def test_coffee_name_length():
    """Test coffee class name initializer character length is between 1 and 15"""
    coffee = Coffee("Cappuccino")
    assert len(coffee.name) > 3

def test_orders():
    Order.all = []
    """Test orders method returns a list of all orders for that customer. """
    customer = Customer("Dennis")
    coffee = Coffee("Cappucino")
    order = Order(customer, coffee, 10.12)
    
    assert coffee.orders("Cappucino") == [order]

def test_customers():
    Order.all = []
    """Test customers method returns a unique list of all customers for that coffee. """
    customer = Customer("Dennis")
    customer1 = Customer("Alex")
    coffee1 = Coffee("Espresso")
    coffee2 = Coffee("Cappucino")
    order1 = Order(customer, coffee1, 10.12)
    order2 = Order(customer1, coffee2, 10.12)
    order3 = Order(customer, coffee2, 10.12)
    
    assert sorted(coffee2.customers()) == sorted([customer.name, customer1.name])