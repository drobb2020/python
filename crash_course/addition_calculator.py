# Python Crash Course 2e
# Chapter 10 - Files and Exceptions
# addition_caclulator.py
# Exercise 10-7 - Addition_calculator:
# Wrap your code from Exercise 10-6 in a while loop so the 
# user can continue entering numbers even if they make a mistake 
# and enter text instead of a number.

print("Enter 'q' to quit at anytime.")

while True:
    try:
        x = input("\nGive me a number: ")
        if x == 'q':
            break

        x = int(x)

        y = input("\nGive me another number: ")
        if y == 'q':
            break
        y = int(y)

    except ValueError:
        print("Sorry, I really need two numbers to add!")
    else:
        sum = x + y
        print(f"The sum of {x} and {y} is {sum}.")
