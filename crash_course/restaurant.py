# Crash Course
# Chapter 9 - Classes
# Exercise 9-1. Restaurant: 
# Make a class called Restaurant. 
# The __init__() method for Restaurant 
# should store two attributes: a restaurant_name 
# and a cuisine_type. Make a method called 
# describe_restaurant() that prints these two 
# pieces of information, and a method called 
# open_restaurant() that prints a message 
# indicating that the restaurant is open.
# Make an instance called restaurant from your class. 
# Print the two attributes individually, 
# and then call both methods.
# Exercise 9-2. Three Restaurants: 
# Start with your class from Exercise 9-1. 
# Create three different instances from the 
# class, and call describe_restaurant() 
# for each instance.

class Restaurant():
    """Simple class showing if a restaurant is open or closed and what kind of food it serves"""

    def __init__(self, name, cuisine):
        """Initialize the name and type of restaurant."""
        self.name = name
        self.cuisine = cuisine


    def describe_restaurant(self):
        """Name and type of food servered."""
        # print(f"The name of the restaurant is {self.name}.")
        # print(f"this restaurant serves {self.cuisine}.")
        print(f"{self.name} is a {self.cuisine} restaurant.")


    def open_restaurant(self):
        print(f"{self.name} is open at this time!")


this_restaurant = Restaurant('New Town', 'Chinese')

this_restaurant.describe_restaurant()
this_restaurant.open_restaurant()

that_restaurant = Restaurant('222 Lyon', 'Spanish Tapas')

that_restaurant.describe_restaurant()
that_restaurant.open_restaurant()

another_restaurant = Restaurant('Lone Star', 'Tex Mex')

another_restaurant.describe_restaurant()
another_restaurant.open_restaurant()
