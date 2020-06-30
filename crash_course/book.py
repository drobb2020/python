# Crash Course
# Chapter 8 - Functions
# Exercise 8-2. Favorite Book: 
# Write a function called favorite_book() 
# that accepts one parameter, title. 
# The function should print a message, 
# such as One of my favorite books is 
# Alice in Wonderland. Call the function, 
# making sure to include a book title 
# as an argument in the function call.

def favorite_book(b_title):
    """This is my favorite book
    """
    print(f"My favorite book is '{b_title.title()}'!")

favorite_book('a tale of two cities')
