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
# Exercise 9-4. Number Served: 
# Start with your program from Exercise 9-1. 
# 1. Add an attribute called number_served with a default 
#    value of 0. Create an instance called restaurant from this 
#    class. Print the number of customers the restaurant has served, 
#    and then change this value and print it again. 
# 2. Add a method called set_number_served() that lets you set the 
#    number of customers that have been served. Call this method with 
#    a new number and print the value again.
# 3. Add a method called increment_number_served() that lets 
#    you increment the number of customers who’ve been served. Call this 
#    method with any number you like that could represent how many 
#    customers were served in, say, a day of business.
# Exercise 9-6. Ice Cream Stand: 
# An ice cream stand is a specific kind of restaurant. 
# 1. Write a class called IceCreamStand that inherits from the 
#    Restaurant class you wrote in Exercise 9-4. 
#    Add an attribute called flavors that stores a list of ice cream flavors. 
#    Write a method that displays these flavors. 
#    Create an instance of IceCreamStand, and call this method.

class Restaurant():
    """Simple class showing if a restaurant is open or closed and what kind of food it serves"""

    def __init__(self, name, cuisine):
        """Initialize the name and type of restaurant."""
        self.name = name
        self.cuisine = cuisine
        self.number_served = 0


    def describe_restaurant(self):
        """Name and type of food servered."""
        # print(f"The name of the restaurant is {self.name}.")
        # print(f"this restaurant serves {self.cuisine}.")
        print(f"{self.name.title()} is a {self.cuisine.title()} restaurant.")


    def open_restaurant(self):
        print(f"{self.name.title()} is open at this time!")


    def served(self):
        print(f"\t{self.name.title()} served {self.number_served} customers today.")

    def set_number_served(self, customers):
        if customers >= self.number_served:
            self.number_served = customers

    def increment_number_served(self, all_customers):
        self.number_served += all_customers


class IceCreamStand(Restaurant):
    """A special type of restaurant"""


    def __init__(self, name, cuisine):
        """Initialize attributes of the parent class."""
        super().__init__(name, cuisine)
        self.flavors = ['vanilla', 'chocolate', 'pistachio', 'run raisin', 'tuti fruiti', 'peanut butter swirl', 'banana split']


    def menu(self):
        """Print the menu of flavors"""
        print(f"{self.name.title()} has the following flavors:")
        for flavor in self.flavors:
            print(flavor.title())


my_icecream = IceCreamStand('sugar mountain', 'ice cream')
my_icecream.describe_restaurant()
my_icecream.open_restaurant()
my_icecream.menu()
