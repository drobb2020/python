# Python Crash Course 2e
# Chapter 10 - Files and Exceptions
# cats_and_dogs.py
# Exercise 10-8 - cats and dogs:
# Make two files, cats.txt and dogs.txt. Store at least three names of cats 
# in the first file and three names of dogs in the second file. Write a program 
# that tries to read these files and print the contents of the file to the 
# screen. Wrap your code in a try-except block to catch the FileNotFound 
# error, and print a friendly message if a file is missing. Move one of 
# the files to a different location on your system, and make sure the code 
# in the except block executes properly.

filename1 = 'cats.txt'
filename2 = 'dogs.txt'

print("---Cats---")
try:
    with open(filename1) as file_object:
        lines = file_object.readlines()
except FileNotFoundError:
    print("OOPS, I can't seem to find that file...")
else:
    for line in lines:
        print(line.rstrip())

print("---Dogs---")
try:
    with open(filename2) as file_object:
        lines = file_object.readlines()
except FileNotFoundError:
    print("OOPS, I can't seem to find that file...")
else:
    for line in lines:
        print(line.rstrip())
