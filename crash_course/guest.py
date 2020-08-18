# Python Crash Course 2e
# Chapter 10 - Files and Exceptions
# guest.py
# Exercise 10-3: Guest
#  Write a program that prompts the user 
# for their name. When they respond, write 
# their name to a file called guest.txt.

from write_message import file_object


filename = 'guest.txt'

name = input("What is your name: ")

with open(filename, 'w') as file_object:
    file_object.write(f"{name}\n")
