# Crash Course
# Chapter 9 - Classes
# Exercise 9-10. Imported Restaurant: 
# Using your latest Restaurant class, 
# store it in a module. 
# Make a separate file that imports Restaurant. 
# Make a Restaurant instance, and call one of 
# Restaurant’s methods to show that the import 
# statement is working properly.

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
        print(f"{self.name} is a {self.cuisine} restaurant.")


    def open_restaurant(self):
        print(f"{self.name} is open at this time!")


    def served(self):
        print(f"\t{self.name} served {self.number_served} customers today.")

    def set_number_served(self, customers):
        if customers >= self.number_served:
            self.number_served = customers

    def increment_number_served(self, all_customers):
        self.number_served += all_customers
