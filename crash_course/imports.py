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

import car
from car import car_builder
from car import car_builder as cb
import car as auto
from car import *

print("Import car")
my_car = car.car_builder(
    'Toyota', 'RAV4', color='Metalic Blackcurrant', sunroof='yes')
print(my_car)

your_car = car.car_builder('Ford', 'Escape', color='purple', pinstriping='yes')
print(your_car)

print("from car import car_builder")
my_car = car_builder(
    'Toyota', 'RAV4', color='Metalic Blackcurrant', sunroof='yes')
print(my_car)

your_car = car_builder('Ford', 'Escape', color='purple', pinstriping='yes')
print(your_car)

print("from car import car_builder as cb")
my_car = cb(
    'Toyota', 'RAV4', color='Metalic Blackcurrant', sunroof='yes')
print(my_car)

your_car = cb('Ford', 'Escape', color='purple', pinstriping='yes')
print(your_car)

print("import car as auto")
my_car = auto.car_builder(
    'Toyota', 'RAV4', color='Metalic Blackcurrant', sunroof='yes')
print(my_car)

your_car = auto.car_builder('Ford', 'Escape', color='purple', pinstriping='yes')
print(your_car)

print("from car import *")
my_car = car_builder(
    'Toyota', 'RAV4', color='Metalic Blackcurrant', sunroof='yes')
print(my_car)

your_car = car_builder('Ford', 'Escape', color='purple', pinstriping='yes')
print(your_car)
