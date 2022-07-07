from item import Item
from phone import Phone

item1 = Item("MyItem", 750, 6)

# Setting an Attribute
item1.name = "OtherItem"

# Getting an Attribute
print(item1.name)


"""     
# Juegamos con la clase   
item1 = Item ("Phone", 100, 1)

item1.apply_discount()
print(item1.price)

item2 = Item ("Laptop", 1000, 3)
item2.pay_rate = 0.7
item2.apply_discount()
print(item2.price)


item3 = Item ("Cable", 10, 5)
item4 = Item ("Mouse", 50, 5)
item5 = Item ("Keyboard", 75, 5)

print(Item.all)
#print(Item.__dict__) # All attributes for Class level
print(item1.__dict__) # All attributes for instance level
"""

Item.instantiate_from_csv() # Class method
print(Item.all)

print(Item.is_integer(9.0)) # Static method


phone1 = Phone("jscPhonev10", 500, 5, 1)
print(phone1.calculate_total_price())
print(Item.all)
print(Phone.all)

item1.apply_increment(0.20)
print(item1.price)

phone1.apply_discount()
print(phone1.price)