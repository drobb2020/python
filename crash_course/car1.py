# Crash Course
# Chapter 8 - Functions
# Exercise 8-16. Imports:
# Using a program you wrote that
# has one function in it, store
# that function in a separate file.
# Import the function into your main
# program file, and call the function
# using each of these approaches:
# import module_name
# from module_name import function_name
# from module_name import function_name as fn
# import module_name as mn
# from module_name import *

def car_builder(make, model_name, **car_info):
    """dictionary information about cars"""
    car_info['manufacturer'] = make
    car_info['model'] = model_name
    return car_info
