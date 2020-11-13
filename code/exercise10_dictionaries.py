#!/usr/bin/env python3

"""Exercise 10
Write Python 3 code that, when run, will do the following:
-Explore use of dictionaries in Python
"""


# Create a dictionary of the 13 provinces (territories) of Canada and their capital cities
capitals =  {
    'Newfoundland and Labrador':'St. John\'s',
    'Northwest Territories':'Yellowknife',
    'Nova Scotia':'Halifax',
    'Alberta':'Edmonton',
    'British Columbia':'Victoria',
    'Manitoba':'Winnipeg',
    'New Brunswick':'Fredericton',
    'Nunavut':'Iqaluit',
    'Ontario':'Toronto',
    'Prince Edward Island':'Charlottetown',
    'Quebec':'Québec',
    'Saskatchewan':'Regina',
    'Yukon':'Whitehorse'
    }

# Output the dictionary keys and values in a loop
# ...remember for the loop! for key, value in listname.items()':'
for province, capital in capitals.items():
    print("{} has the capital {}".format(province, capital))


# Create a new value and key
capitals['Canada'] = 'Ottawa'

# Delete a key, value
del capitals['Saskatchewan']


# Output the dictionary keys and values again using a loop, this time sorted alphabetically by key
# remember for the following the the loop':' for key, value in sorted (listname.items())':'
print("-" * 60)
for province_or_country, capital in sorted(capitals.items()):
    print("{} has the capital {}".format(province_or_country, capital))