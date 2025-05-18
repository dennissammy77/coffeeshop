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