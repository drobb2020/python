# Crash Course
# Chapter 9 - Classes
# Exercise 9-11. Imported Admin: 
# Start with your work from Exercise 9-8. 
# Store the classes User, Privileges, and Admin 
# in one module. Create a separate file, make an 
# Admin instance, and call show_privileges() to show 
# that everything is working correctly.

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


    def greet_user(self):
        """Greet the user"""
        print(
            f"Hello {self.first.title()} {self.last.title()}, welcome to Excession Systems.")
        print(
            f"Your {self.experience} years of experience will be a great benefit to the company.")


    def increment_login_attempts(self, attempt):
        """for each attempt, increment by 1"""
        self.login_attempts = self.login_attempts + attempt
        print(
            f"{self.first.title()} you have attempted to login {self.login_attempts} times.")


    def reset_login_attempts(self):
        """reset the login_attempts to 0"""
        self.login_attempts = 0
        print(f"Login attempts have been reset to {self.login_attempts}")


