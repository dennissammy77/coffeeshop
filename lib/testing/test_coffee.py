from lib.models import Coffee

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