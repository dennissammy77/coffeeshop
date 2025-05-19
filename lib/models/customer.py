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

    def orders(self):
        from .order import Order
        return [order for order in Order.all if order.customer.name == self.name]

    def coffees(self):
        from .order import Order
        return list(set(
            order.coffee.name for order in self.orders()
        ))
    
    def create_order(self, coffee, price):
        from .order import Order
        Order(self,coffee,price)

    def most_aficionado(coffee):
        from .coffee import Coffee
        customers_dict={}
        max_customer = None
        max_spent = 0
        for order in coffee.orders():
            if order.customer.name in customers_dict:
                customers_dict[order.customer.name] += order.price
                if customers_dict[order.customer.name] > max_spent:
                    max_spent = customers_dict[order.customer.name]
                    max_customer = order.customer
            else:
                customers_dict.update({order.customer.name : order.price})
        return max_customer if max_spent > 0 else None
