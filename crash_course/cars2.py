# Crash Course
# Chapter 8 - Functions
# Exercise 8-14. Cars: Write a function 
# that stores information about a car in 
# a dictionary. The function should always 
# receive a manufacturer and a model name. 
# It should then accept an arbitrary number 
# of keyword arguments. Call the function 
# with the required information and two other 
# name-value pairs, such as a color or an optional 
# feature. Your function should work for a call 
# like this one:
# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# Print the dictionary that’s returned to make sure 
# all the information was stored correctly.

def car_builder(make, model_name, **car_info):
    """dictionary information about cars"""
    car_info['manufacturer'] = make
    car_info['model'] = model_name
    return car_info


my_car = car_builder('Toyota', 'RAV4', color='Metalic Blackcurrant', sunroof='yes')
print(my_car)

your_car = car_builder('Ford', 'Escape', color='purple', pinstriping='yes')
print(your_car)
