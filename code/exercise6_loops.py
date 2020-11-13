#!/usr/bin/env python3

"""Exercise 6
Write Python 3 code that, when run, will do the following:
-Explore use of loops in Python
"""


# Store a list of numbers, loop through and output each of these numbers
mylist = [3,7,9,11,13,15,17,19]
for number1 in mylist:
    print(number1)

# Using a loop and the range function output the following (output will be on separate lines):
#  0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
print("===================================================================")
for number2 in range(16):
    print(number2)

# Using a loop and the range function output the following (output will be on separate lines):
# 55 56 57 58 59
print("===================================================================")
for number3 in range(55,60):
    print(number3)

# Using a loop and the range function output the following (output will be on separate lines):
#  4 7 10 13 16
print("===================================================================")
for number4 in range(4,17,3):
    print(number4)

# Use a while loop to output the following (output will be on separate lines):
#  76 77 78 79 80 81 82 83 84 85 86 87 88 89 90
print("===================================================================")
number5 = 76
while number5 < 91:
    print(number5)
    number5 += 1

# Use a while loop to output the following (output will be on separate lines):
#  87 89 91 93 95 97
print("===================================================================")
number6 = 87
while number6 < 98:
    print(number6)
    number6 += 2

# Use a while loop that outputs ever-increasing numerical values but that breaks out at a specified value
print("===================================================================")
number7 = 0
while True:
    number7 += 3
    if number7 >= 22:
        break
    print(number7)

# Use a while loop that successfully uses the continue command
print("===================================================================")
print("It will skip value 12")
number8 = 0
while True:
    number8 += 3
    if number8 == 12:
        continue
    elif number8 >= 22:
        break
    print(number8)

# Use a while loop that outputs ever-increasing numbers, then meets the condition to end which ends the loop
# and then executes an else statement which outputs something like “The loop has ended because the condition has been met.”
print("===================================================================")
number9 = 0
while number9 < 22:
    print(number9)
    number9 += 3
else:
    print("The loop has ended because the condition has been met.")

# Create a for loop which outputs ever-increasing numerical values. The loop will contain an if
# statement which contains a break command with a condition that will be met, thereby ensuring that the loop
# ends. It will also contain an else statement, similar to the example in the tutorial, that will not be executed.
print("===================================================================")
for number10 in range(5,76,5):
    if number10 == 50:
        print("It is breaking after this statement as the condition is met for break and it will not print else statement")
        break
    print(number10)
else:
    print("This is not printed because for loop is terminated because of break but not due to fail in condition.")