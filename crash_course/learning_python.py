# Python Crash Course 2e
# Chapter 10 - Files and Exceptions
# learning_python.py
# Exercise 10.1 - Learning Python:
# Open a blank file in your text editor 
# and write a few lines summarizing what 
# you’ve learned about Python so far. Start 
# each line with the phrase In Python you can. 
# ... Save the file as learning_python.txt in the 
# same directory as your exercises from this chapter. 
# Write a program that reads the file and prints what 
# you wrote three times. Print the contents once by 
# reading in the entire file, once by looping over the 
# file object, and once by storing the lines in a list 
# and then working with them outside the with block.

# 1 print via reading the contents
with open('learning_python.txt') as file_object:
    contents = file_object.read()
    print("Print the contents of the file by reading the file.")
    print(contents.rstrip())

#2 printing via a loop
filename = 'learning_python.txt'
print("")
print("Print the contents using a for loop.")
with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

#3 Printing a list
filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

print("")
print("Print the contents from a list.")
for line in lines:
    print(line.rstrip())
