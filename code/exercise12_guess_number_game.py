#!/usr/bin/env python3

"""Exercise 12
Write Python 3 code that, when run, will do the following:
- A game - "Guess the number" in Python
"""

import random

# Method to test whether value input is within the conditions
# (not a number, or a value outside the 1 and 100 boundaries)
def test_value(value_sent):
    if value_sent.isdigit() and 1 <= int(value_sent) <=100:
        return True
    else:
        return False


# Main function to do the task
def main():
    # Generate and store as a variable a random number between 1 and 100
    random_number = random.randint(1,100)

    print("WELCOME TO THE GUESS GAME!")
    print("DO YOU WANT TO GUESS WHAT NUMBER IS IN MY MIND?\n")

    guess = str(input('Please guess a number between 1 and 100: (Enter 999 to quit early) \n'))
    print ("You have guessed this number "+str(guess))

    guessed_number = False
    attempt_count = 0
    while not guessed_number:
        attempt_count += 1

        if int(guess) == 999:
            print("Sorry to see you go early...")
            exit()
        if not test_value(guess) :   # Tests if the user entered an invalid value
            guess = str(input('Please input only digits. Try again: '))
            continue
        if int(guess) > random_number:
            print("Sorry! Your number is too high...")
            guess = str(input('Try again: '))
            continue
        elif int(guess) < random_number:
            print("Sorry! Your number is too Low...")
            guess = str(input('Try again: '))
            continue

        else:
            guessed_number = True
    # Tells the how many guesses they took to guess correctly
    print("You have tried "+str(attempt_count) + " times to guess correctly")

    # Tells the how many guesses they took to guess correctly
    if attempt_count < 3:
        print("CONGRATS! YOU HAVE have WON A JACKPOT ...")


# Call on the function called main to make the program run
if __name__ == "__main__":
    main()