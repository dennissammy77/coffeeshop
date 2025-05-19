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

    def orders(self):
        from .order import Order
        return [order for order in Order.all if order.coffee.name == self.name]

    def customers(self):
        from .order import Order
        return list(set(
            order.customer.name for order in Order.all if order.coffee.name == self.name
        ))
    
    def num_orders(self):
        # from .order import Order
        # total = 0
        # for order in Order.all:
        #     if order.coffee.name == self.name:
        #         total +=1
        
        # return total
        return len(self.orders())
    
    def average_price(self):
        from .order import Order
        total = 0
        total_price = 0
        for order in Order.all:
            if order.coffee.name == self.name:
                total += 1
                total_price += order.price
        
        return total_price/total
