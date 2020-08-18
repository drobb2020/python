# Python Crash Course 2e
# Chapter 10 - Files and Exceptions
# guest.py
# Exercise 10-4: Guest Book
# Write a while loop that prompts users for their name. 
# When they enter their name, print a greeting to the 
# screen and add a line recording their visit in a file 
# called guest_book.txt. Make sure each entry appears on 
# a new line in the file.

from write_message import file_object

filename = 'guest_book.txt'

print("Enter 'quit' when you are finished.")
while True:
    name = input("\nPlease enter your name for our guest book: ")
    if name == 'quit':
        break
    else:
        with open(filename, 'a') as f:
            f.write(f"{name}\n")
        print(f"Hi {name}, you've been added to the guest book.")
