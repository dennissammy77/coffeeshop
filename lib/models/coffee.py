class Coffee:
    def __init__(self,name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        if not isinstance(value,str):
            raise Exception
        if not len(value) > 3:
            raise Exception
        self._name = value

    def orders(self,name):
        from .order import Order
        return [order for order in Order.all if order.coffee.name == name]

    def customers(self):
        from .order import Order
        return list(set(
            order.customer.name for order in Order.all if order.coffee.name == self.name
        ))
