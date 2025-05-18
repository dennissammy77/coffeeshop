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
    Order(customer, coffee1, 10.12)
    Order(customer1, coffee2, 10.12)
    Order(customer, coffee2, 10.12)
    
    assert sorted(coffee2.customers()) == sorted([customer.name, customer1.name])

def test_num_orders_returns_total_orders_for_coffee():
    Order.all = []
    """Test that num_orders method returns the correct total number of orders for a given Coffee instance."""
    customer = Customer("Dennis")
    customer1 = Customer("Alex")
    coffee1 = Coffee("Espresso")
    coffee2 = Coffee("Cappucino")
    Order(customer, coffee1, 10.12)
    Order(customer1, coffee2, 10.12)
    Order(customer, coffee2, 10.12)
    Order(customer1, coffee1, 10.12)
    Order(customer, coffee1, 10.12)

    assert coffee2.num_orders() == 2
    assert coffee1.num_orders() == 3

def test_average_price_returns_correct_average_for_coffee():
    Order.all = []
    """Test that average_price method returns the correct average price of all orders for a given Coffee instance."""

    customer = Customer("Dennis")
    coffee2 = Coffee("Cappucino")
    Order(customer, coffee2, 10.12)
    Order(customer, coffee2, 10.12)

    assert coffee2.average_price() == 10.12