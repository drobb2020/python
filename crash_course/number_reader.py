# Python Crash Course 2e
# Chapter 10 - Files and Exceptions
# number_reader.py

import json

filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)

print(numbers)
