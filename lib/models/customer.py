class Customer:
    def __init__(self,name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        if not isinstance(value,str):
            raise Exception
        if not (len(value) > 1 and len(value) < 25):
            raise Exception
        self._name = value

    def orders(self,name):
        from .order import Order
        return [order for order in Order.all if order.customer.name == name]

    def coffees(self):
        from .order import Order
        return list(set(
            order.coffee.name for order in Order.all if order.customer.name == self.name
        ))
    
    def create_order(self, coffee, price):
        from .order import Order
        Order(self,coffee,price)

