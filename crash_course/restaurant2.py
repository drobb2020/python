# Crash Course
# Chapter 9 - Classes
# Exercise 9-10

from restaurant import Restaurant

this_restaurant = Restaurant('New Town', 'Chinese')

this_restaurant.describe_restaurant()
this_restaurant.open_restaurant()
this_restaurant.number_served = 10
this_restaurant.served()
this_restaurant.set_number_served(45)
this_restaurant.served()
this_restaurant.increment_number_served(40)
this_restaurant.served()
