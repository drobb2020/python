# Python Crash Course 2e
# Chapter 10 - Files and Exceptions
# addition.py
# Exercise 10-6 - Addition:
# One common problem when prompting for numerical input occurs when 
# people provide text instead of numbers. When you try to convert the 
# input to an int, you’ll get a ValueError. Write a program that prompts 
# for two numbers. Add them together and print the result. Catch the 
# ValueError if either input value is not a number, and print a friendly 
# error message. Test your program by entering two numbers and then by 
# entering some text instead of a number.

try:
    x = input("\nGive me a number: ")
    x = int(x)

    y = input("\nGive me another number: ")
    y = int(y)
    
except ValueError:
    print("Sorry, I really need two numbers to add!")
else:
    sum = x + y
    print(f"The sum of {x} and {y} is {sum}.")
