# Crash Course
# Chapter 8 - Functions
# Exercise 8-1. Message: Write a function called 
# display_message() that prints one sentence 
# telling everyone what you are learning about 
# in this chapter. Call the function, and make 
# sure the message displays correctly.

def display_message(user):
    """Simple function to display a message telling people what I'm studying"""
    print(f"\nHello, my name is {user.title()}.")
    print("I'm teaching myself Python.")
    print("In this chapter I'm learning all about functions.")


display_message('david')
