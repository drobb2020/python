# Crash Course
# Chapter 9 - Classes
# Exercise 9-3. Users: 
# Make a class called User. 
# Create two attributes called first_name and last_name, 
# and then create several other attributes that are 
# typically stored in a user profile. 
# Make a method called describe_user() 
# that prints a summary of the user’s information. 
# Make another method called greet_user() that 
# prints a personalized greeting to the user.

class User():
    """A exercise class for defining a user."""

    def __init__(self, first, last, location, profession, experience):
        """Initialize the user class attributes"""
        self.first = first
        self.last = last
        self.location = location
        self.profession = profession
        self.experience = experience
    
    def profile(self):
        """Everything we know about a user."""
        print(f"Username: {self.first.title()} {self.last.title()}")
        print(f"Location: {self.location.title()}")
        print(f"Profession: {self.profession.title()}")
        print(f"Experience: {self.experience} years")

    
    def great_user(self):
        """Greet the user"""
        print(f"Hello {self.first.title()} {self.last.title()}, welcome to Excession Systems.")
        print(f"Your {self.experience} years of experience will be a great benefit to the company.")

new_user = User('david', 'robb', 'ottawa', 'solution support engineer', 22)

new_user.profile()
new_user.great_user()
