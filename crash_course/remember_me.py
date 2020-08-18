# Python Crash Course 2e
# Chapter 10 - Files and Exceptions
# remember_me.py

import json


username = input("What is your name? ")

filename = 'username.json'
with open(filename, 'w') as f:
    json.dump(username, f)
    print(f"We will remember you when you come back, {username}!")
