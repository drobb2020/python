# Python Crash Course 2e
# Chapter 10 - Files and Exceptions
# cats_and_dogs-silent.py
# Exercise 10-9 - cats and dogs silently:
# Modify your except block in Exercise 10-8 to fail silently 
# if either file is missing.

filename1 = 'cats.txt'
filename2 = 'dogs.txt'

print("---Cats---")
try:
    with open(filename1) as file_object:
        lines = file_object.readlines()
except FileNotFoundError:
    pass
else:
    for line in lines:
        print(line.rstrip())

print("---Dogs---")
try:
    with open(filename2) as file_object:
        lines = file_object.readlines()
except FileNotFoundError:
    pass
else:
    for line in lines:
        print(line.rstrip())
