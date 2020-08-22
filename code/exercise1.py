#!/usr/bin/env python3

"""Exercise 1
Write Python 3 code that, when run, will do the following:
• Create a list which stores integer numbers. You can choose whatever integer values you
want. But, make sure to add the elements this way
• Elements 0-7 are added at time of initialization
• Element 8 is appended
• Output all 9 elements in the numbers list using the least amount of code (1 line)
• Insert an integer value into element 3
• Change the value of element 1
• Remove a value of your choosing from the list using the “remove” method
• Remove the last element using the pop method
• Output all the elements in the numbers list using the least amount of code (1 line)
• Output element 1 only
• Create a list which stores 3 strings
• Output all 3 elements in the strings list using the least amount of code (1 line)
• Output a short paragraph. The paragraph will use your 3 string values from the strings list.
"""

# Exercise No 1 - Lists

# List of 8 integers elements
my_list = [110, 220, 79, 320, 15, 68, 19, 329]

# One more integer appended to the list
my_list.append(7)

# Outputting all the 9 elements of the list
print(my_list)

# Inserting an integer value into element 3
my_list.insert(2, 29)

# Change the value of element 1
my_list[0] = 35

# Remove the element with value 320
my_list.remove(320)

# The pop method to remove the last element
my_list.pop()

# Outputting all 9 elements of the list
print(my_list)

# Outputting the element 1 of the list
print(my_list[0])

# List of three strings
my_string = ("Hello there!", "My name is", "Harjap Gosal")
print(my_string)

# Outputting a short paragraph using 3 string values from the strings list
my_string2 = ["I love them.", "burgers", "tasty"]
print("What makes a hamburger and other cooked meat so enticing to humans?..."
      "The answers is that the " + my_string2[1] + " are very " + my_string2[2]
      + " and " + my_string2[0])
