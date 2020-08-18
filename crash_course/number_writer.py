# Python Crash Course 2e
# Chapter 10 - Files and Exceptions
# number_writer.py

import json

numbers = [2, 3, 5, 7, 11, 13, 17]

filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)
