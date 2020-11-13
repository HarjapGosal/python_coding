#!/usr/bin/env python3

"""Exercise 4
Write Python 3 code that, when run, will do the following:
-Use of conditions in Python
"""

#Exercise 4 - Conditions

# Create three variables. Two of them store numbers and one stores text.
your_age = 16
your_grade = 11
your_city = "Surrey"

# Use the “and” operator to test the values in at least two of the the
# variables and output some text if the logical requirements are met
if your_city == "Surrey" and your_age < 20:
    print ("You live in Surrey and you are still not in your twenties." )

# Use the “or” operator to test the values in at least two of the the
# variables and output some text if the logical requirements are met
if your_grade == 11 or your_age == 16:
    print ("Either you study in grade 11 or you are 16 years old" )

# In a single statement, use the “in” operator to test your text variable
# against three possible matches
if your_city in ["Surrey", "Delta", "Richmond"]:
    print ("Your live in either of these cities: Surrey, Delta or Richmond.")

# Write and format properly a complete if, elif, else statement which
# contains appropriate tests and outputs.
your_marks = 85
if your_marks >= 85:
    print ("You will be assigned an A grade.")
elif your_marks >= 73 and  your_marks < 85:
    print("You will be assigned a B grade.")
else:
    print ("You will be assigned a grade below than B grade." )