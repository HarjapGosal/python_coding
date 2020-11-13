#!/usr/bin/env python3

"""Exercise 5
Write Python 3 code that, when run, will do the following:
-Explore use of placeholders in Python
"""

#Using the older placeholders method(modulo %) output “Clayton has 4 excellent basketball
# players this season.” - where 4 is a digit placeholder and ‘basketball’ is a string
print("Clayton has %d excellent basketball players this season." % (4))

# Using the older placeholders method (modulo %) to output the following
print("%10.2f"%(45.23))
print("%10.2f"%(3.03))
print("%10.2f"%(139.80))
print("%10.2f"%(2948.09))

print("%+14d"% 54,"%16.4e"% (652.16))

print("The current temperature outside the {0:s} airport is {1:5.1f} celsius".format("Vancouver",5.6))

print("The population of {city:s},Columbia is {population:5.3f} millions".format(city="Bogata", population=6.763))

city =  "Phoenix"
population = 4.574
print("The population of  {0} Arizona is {1} millions".format(city, population))

print("{0:>20s} {1:>15s} {2:>15s} {3:<9.2f}".format('Laptop:', 'MacbookPro','Cost:',1579))
print("{0:>20s} {1:>15s} {2:>15s} {3:<9.2f}".format('Laptop:', 'Surface Pro 4','Cost:',1439))
