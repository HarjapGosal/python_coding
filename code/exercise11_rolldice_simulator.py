#!/usr/bin/env python3

"""Exercise 11
Write Python 3 code that, when run, will do the following:
- A roll dice simulator in Python
"""

# Define a function called “roll” that assigns a random integer number between 1 and 6 to a variable.
import random
def roll (num_sides):
    random_number = random.randint(1,num_sides)
    return random_number

# main function which contains: a variable that stores the number of sides,

def main ():
    number_of_side = 6
    rolling = True
    # rolling is a Boolean variable which, when true, keeps the loop running
    while rolling:
    # rolling is true, to have the loop begin
        roll_again = input("Press return to roll or press q to quit")
        if roll_again.lower()!="q":
            print("\nWait while the roll is being diced......\n")
            result = roll(number_of_side)
            print("The number you got on this roll ==> "+str(result)+"\n")
        else:
            print("\nThanks for playing, Have a good day!")
            rolling = False

if __name__ == "__main__":
    main()