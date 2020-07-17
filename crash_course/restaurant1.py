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
# Restaurant class you wrote in Exercise 9-1 or Exercise 9-4. 
# Either version of the class will work; just pick the one you like better.
# Add an attribute called flavors that stores a list of ice cream flavors. 
# Write a method that displays these flavors. 
# Create an instance of IceCreamStand, and call this method.

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


this_restaurant = Restaurant('New Town', 'Chinese')

this_restaurant.describe_restaurant()
this_restaurant.open_restaurant()
this_restaurant.number_served = 10
this_restaurant.served()
this_restaurant.set_number_served(45)
this_restaurant.served()
this_restaurant.increment_number_served(40)
this_restaurant.served()


that_restaurant = Restaurant('222 Lyon', 'Spanish Tapas')

that_restaurant.describe_restaurant()
that_restaurant.open_restaurant()
that_restaurant.number_served = 10
that_restaurant.served()
that_restaurant.set_number_served(20)
that_restaurant.served()
that_restaurant.increment_number_served(10)
that_restaurant.served()

another_restaurant = Restaurant('Lone Star', 'Tex Mex')

another_restaurant.describe_restaurant()
another_restaurant.open_restaurant()
another_restaurant.number_served = 100
another_restaurant.served()
another_restaurant.set_number_served(400)
another_restaurant.served()
another_restaurant.increment_number_served(350)
another_restaurant.served()
