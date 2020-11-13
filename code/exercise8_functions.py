#!/usr/bin/env python3

"""Exercise 8
Write Python 3 code that, when run, will do the following:
-Explore use of functions in Python
"""


# Create a function that returns a tuple of your favorite foods. This function does not receive
# any arguments.

def my_favoorite_foods():
    return 'chicken wings', 'chicken burgars', 'pizza', 'fries', 'fried fish'

# Create a second function that returns the text “--food item-- is one of my favorite foods.”
# Make sure this function includes one argument which will be the food item and remember
# to use this argument with the return text.

def my_favoorite_food(food_item):
    my_favoorite_food_item = food_item + ' is one of my favorite foods.'
    return my_favoorite_food_item


# Create a third function that has two parts:
# A line of code that creates a new reference to the first function you made, the favorite
# foods list (a reference is like creating a shortcut to the function and the reason you do this
# is that you are not able to directly loop a function but you can loop a reference to the function)
# And a loop that assigns the value of the loop (remember it’s going loop through the list of
# foods) to what will become an argument...because inside the loop is:
# A single print command which calls on the second function (outputs favorite foods) you
# made and passes the argument from the loop to it. The second function will return the
# text, with the included argument value, back to the print command.

def name_my_favorite_foods():
    list_of_favorite_foods = my_favoorite_foods()
    for food_item in list_of_favorite_foods:
        print (my_favoorite_food(food_item))

# A call on the third function
name_my_favorite_foods()