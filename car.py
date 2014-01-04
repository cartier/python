#!/usr/bin/python
  
       # define the Vehicle class
class Vehicle:
    name = ""
    kind = "car"
    color = ""
    value = 100.00
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str
    
    def __init__(self, name=None, color=None, kind='car', value=100):
		self.name = name
		self.color = color
		self.kind = kind
		self.value = value
    
# your code goes here

# test code

car1 = Vehicle ('Fer', 'red', 'convertible', 60000)

car2= Vehicle ('Jump', 'blue', 'van', 10000)


print car1.description()
print car2.description()



