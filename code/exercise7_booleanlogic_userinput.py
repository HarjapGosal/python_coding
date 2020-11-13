#!/usr/bin/env python3

"""Exercise 7
Write Python 3 code that, when run, will do the following:
-Explore boolean logic and user input in Python
"""

# Program which demonstrates boolean logic

# Part 1
age = input("Your age? ")
income = input("Your income? ")
your_age = int(age)
your_income = int(income)

if your_age >= 14 and your_income >= 500:
    print ("You are old enough to work and made enough money.")
elif your_age >= 14 and your_income < 500:
    print("You are old enough to work, but you did not make enough money.")
elif your_age < 14 and your_income >= 500:
    print("You made enough money but you aren't old enough to work!")
else:
    print ("You are not old enough to work, nor did you earn much money." )


# Part 2
input_text = input("Please enter your input ")
print("The entered input by you is: "+input_text)

result1 = input_text.isalnum()
if result1:
    print ("Parsing all characters for only digits and alphabetic characters: "+ str(result1))
else:
    print("Parsing all characters for only digits and alphabetic characters: " + str(result1))

result2 = input_text.isalpha()
if result2:
    print ("Parsing all characters for only alphabetic characters: "+ str(result2))
else:
    print("Parsing all characters for only alphabetic characters: " + str(result2))

result3 = input_text.isdigit()
if result3:
    print ("Parsing all characters for only digit characters: "+ str(result3))
else:
    print("Parsing all characters for only digit characters: " + str(result3))

result4 = input_text.istitle()
if result4:
    print ("Parsing all characters for first word(s) capitalization: "+ str(result4))
else:
    print("Parsing all characters for first word(s) capitalization: " + str(result4))

result5 = input_text.isupper()
if result5:
    print ("Parsing only alphabetic characters for only upper-case characters: "+ str(result5))
else:
    print("Parsing only alphabetic characters for only upper-case characters: " + str(result5))

result6 = input_text.islower()
if result6:
    print ("Parsing only alphabetic characters for only lower-case characters: "+ str(result6))
else:
    print("Parsing only alphabetic characters for only lower-case characters: " + str(result6))

result7 = input_text.isspace()
if result7:
    print ("Parsing all characters for only spaces: "+ str(result7))
else:
    print("Parsing all characters for only spaces: " + str(result7))

result8 = input_text.endswith('d')
if result8:
    print ("Parsing the last character entered, looking for 'd': "+ str(result8))
else:
    print("Parsing the last character entered, looking for 'd': " + str(result8))

result9 = input_text.istitle()
if result9:
    print ("Parsing the first character entered, looking for 'H': "+ str(result9))
else:
    print("Parsing the first character entered, looking for 'H': " + str(result9))
