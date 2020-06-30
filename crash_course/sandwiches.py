# Crash Course
# Chapter 8 - Functions
# Exercise 8-12. Sandwiches: Write a function 
# that accepts a list of items a person wants 
# on a sandwich. The function should have one 
# parameter that collects as many items as the 
# function call provides, and it should print 
# a summary of the sandwich that’s being ordered. 
# Call the function three times, using a different 
# number of arguments each time.

def sandwich_builder(*toppings):
    """Build a sandwich to the customers specification
    """
    print(f"\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print(f" - {topping.title()}")
    print("Your sandwich will be ready in 5 minutes!")

sandwich_builder('tuna', 'lettuce', 'cheese', 'mayo')
sandwich_builder('bacon', 'lettuce', 'tomato', 'mayo')
sandwich_builder('turkey', 'bacon', 'romaine', 'tomato', 'mayo')
