# Python Crash Course 2e
# Chapter 11 - Testing your code
# name_function.py

def get_formatted_name(first, last, middle=''):
    """generate a neatly formatted full name."""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()
