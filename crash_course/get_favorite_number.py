# Python Crash Course 2e
# Chapter 10 - Files and Exceptions
# favorite_number.py
# Exercise 10-11 Favorite Number:
# Write a program that prompts for the user’s favorite number. 
# Use json.dump() to store this number in a file. Write a separate 
# program that reads in this value and prints the message, 
# “I know your favorite number! It’s _____.”

import json

fav_number = input("Enter your favorite number: ")

filename = 'fav_num.json'
with open(filename, 'w') as f:
    json.dump(fav_number, f)
    print(f"Your number has been stored in a safe place!")
