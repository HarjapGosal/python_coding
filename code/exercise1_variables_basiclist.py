#!/usr/bin/env python3

"""Exercise 2
Write Python 3 code that, when run, will do the following:
• Use of the variables in Python
• Explore basics of lists in Python
"""

#Exercise 1a Variables
my_integer = 30
my_float = 15.7
my_string = "Hi my name is Harjap"

#This will print variables in different lines
print(my_integer)
print(my_float)
print(my_string)

#This will print all variables in one line
print(my_integer,my_float,my_string)

another_float = 20.5
new_result = (my_integer + my_float) * another_float
print("Here we will mix my text and this variable value: " + str(new_result))


#Exercise 1b, Lists fundamentals

#List of 8 integers elements
mylist = [110,220,79,320,15,68,19,329]
#One more integer appended to the list
mylist.append(7)
#Outputting all the 9 elements of the list
print(mylist)

#Inserting an integer value into element 3
mylist.insert(2,29)
#Change the value of element 1
mylist[0] = 35
#Remove the element with value 320
mylist.remove(320)
#The pop method to remove the last element
mylist.pop()
#Outputting all 9 elements of the list
print(mylist)

#Outputting the element 1 of the list
print(mylist[0])

#List of three strings
mystring = ("Hello there!", "My name is","Harjap Gosal")
print(mystring)

#Outputting a short paragraph using 3 string values from the strings list
mystring2 = ["I love them.", "burgers","tasty"]
print("What makes a hamburger and other cooked meat so enticing to humans?..."
      "The answers is that the "+ mystring2[1] + " are very " + mystring2[2]
      + " and "+mystring2[0])



