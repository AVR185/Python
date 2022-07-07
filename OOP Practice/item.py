import csv

class Item:
    pay_rate = 0.8 #The pay rate after 20% discount
    all = []
    
    def __init__ (self, name: str, price: float, quantity = 0):
        # Run validations to the received arguments
        assert price >= 0, f"Price {price} is not greater than or equal to zero!"
        assert quantity >= 0, f"Quantity {quantity} is not greater or equal to zero!" 
        
        #Assign to self object
        self.__name = name  # Private attribute
        self.__price = price
        self.quantity = quantity
        
        #Actions to execute
        Item.all.append(self)
        
    @property
    # Property Decorator = Read-Only Attribute // Getter
    def name(self):
        return self.__name

    @name.setter 
    def name(self, value):
        if len(value) > 10:
            raise Exception("The name is too long!")
        else:
            self.__name = value
            
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price (self, value):
        if value <= 0:
            raise Exception("The new price must be greater than or equal to zero!")
        else:
            self.__price = value
        
    def calculate_total_price(self):
        return self.__price * self.quantity
    
    def apply_increment (self, increment_value):
        self.__price += self.__price * increment_value
    
    def apply_discount(self):
        self.__price = self.__price * self.pay_rate
        
    @classmethod
    def instantiate_from_csv(cls):
        with open("OOP Practice\items.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
            
        for item in items:
            Item (
                name = item.get('name'),
                price =  int(item.get('price')) if Item.is_integer(float(item.get('price'))) else float(item.get('price')),
                quantity = int(item.get('quantity'))
            )
    
    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # For i.e: 5.0, 10.0
        if isinstance(num, float):
            # Count out the floats that are point zero
            return num.is_integer() # False
        elif isinstance(num, int):
            return True
        else:
            return False
        
    def __repr__(self):
        return f"{self.__class__.__name__}('{self.__name}', {self.__price}, {self.quantity}{', ' + str(self.broken_phones) if self.__class__.__name__ == 'Phone' else ''})"
    
    
    # Abstraction
    def __connect(self, smpt_server):
        pass
    
    def __preprare_body(self):
        return f"""
            Hello Someone.
            We have {self.__name} {self.quantity} times
            Regards,
            Alvaro VR"""
    
    def __send(self):
        pass
    
    def send_email(self):
        self.__connect('')
        self.__preprare_body
        self.__send