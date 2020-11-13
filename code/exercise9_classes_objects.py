#!/usr/bin/env python3

"""Exercise 9
Write Python 3 code that, when run, will do the following:
-Explore use of classes and objecys in Python
"""

# Create two classes defined as ‘Car1’ and ‘Car2’
# Set ‘Car1’ class variables to be a red convertible worth $60,000 with a name of Fer
# Additionally, include in Car1 a function that outputs a message
# Set ‘Car2’ to be a blue van named Jump worth $10,000
class Car1:
    name = "Fer"
    price = 60000
    color = "red"
    def car1Function(self):
        message = "This message is from inside the first class (Car1)."
        return message

class Car2:
    name = "Jump"
    price = 10000
    color = "blue"

# Assign 2 objects, called myCar1 and myCar2 to the Car1 and Car2 classes
myCar1 = Car1()
myCar2 = Car2()

# Output the name and cost of the ‘Car1’ class by calling on the class variables and by
# accessing them using the myCar1 object
print("The name of the first car is " +myCar1.name + " and the price is $"+str(myCar1.price) +".")

# Assign a new cost to ‘Car1’ class and output it.
Car1.price = 50000
print("The name of the first car is " +myCar1.name + " and the new price is $"+str(myCar1.price) +".")

# Output the name of the ‘Car2’ class
print("The name of the second car is " +myCar2.name +".")

# Assign a new name to the ‘Car2’ class and output it.
Car2.name = "Mustang"
print("The changed name of the second car is " +myCar2.name +".")

# Output the message you defined in the function in the Car1 class - and remember you can
# only call on a class function by using an object in that same class (in this case, the myCar1# object)
print(myCar1.car1Function())
