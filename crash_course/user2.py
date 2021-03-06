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
# Exercise 9-5. Login Attempts: 
# Add an attribute called login_attempts to your User class 
# from Exercise 9-3. 
# 1. Write a method called increment_login_attempts() that 
# increments the value of login_attempts by 1. 
# 2. Write another method called reset_login_attempts() that 
# resets the value of login_attempts to 0.
# 
# Make an instance of the User class and call 
# increment_login_attempts() several times. 
# Print the value of login_attempts to make sure it was 
# incremented properly, and then call reset_login_attempts(). 
# Print login_attempts again to make sure it was reset to 0.

class User():
    """A exercise class for defining a user."""

    def __init__(self, first, last, location, profession, experience):
        """Initialize the user class attributes"""
        self.first = first
        self.last = last
        self.location = location
        self.profession = profession
        self.experience = experience
        self.login_attempts = 0
    
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


    def increment_login_attempts(self, attempt):
        """for each attempt, increment by 1"""
        self.login_attempts = self.login_attempts + attempt
        print(f"{self.first.title()} you have attempted to login {self.login_attempts} times.")


    def reset_login_attempts(self):
        """reset the login_attempts to 0"""
        self.login_attempts = 0
        print(f"Login attempts have been reset to {self.login_attempts}")


new_user = User('david', 'robb', 'ottawa', 'solution support engineer', 22)

new_user.profile()
new_user.great_user()
new_user.increment_login_attempts(1)
new_user.increment_login_attempts(1)
new_user.increment_login_attempts(1)
new_user.increment_login_attempts(1)
new_user.increment_login_attempts(1)
new_user.reset_login_attempts()
