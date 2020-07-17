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
#
# Exercise 9-7. Admin: 
# An administrator is a special kind of user. 
# 1. Write a class called Admin that inherits from the User class 
# you wrote. 
# Add an attribute called privileges, that stores a list of 
# strings like "can add post", "can delete post", "can ban user", 
# and so on. Write a method called show_privileges() 
# that lists the administrator’s set of privileges. 
# Create an instance of Admin, and call your method.
# 
# Exercise 9-8. Privileges: 
# Write a separate Privileges class. 
# The class should have one attribute, privileges, that stores a 
# list of strings as described in Exercise 9-7. 
# Move the show_privileges() method to this class. 
# Make a Privileges instance as an attribute in the Admin class. 
# Create a new instance of Admin and use your method to show 
# its privileges.

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


class Admin(User):
    """Special user class with additional rights"""

    def __init__(self, first, last, location, profession, experience):
        """Initialize attributes of the parent class."""
        super().__init__(first, last, location, profession, experience)
        self.priviledges = ['can add post', 'can delete post',
                            'can add user', 'can ban user', 'can edit post']
    
    def show_priviledges(self):
        print("As administrator you have the following priviledges:")
        for priviledge in self.priviledges:
            print(priviledge)


new_user = User('david', 'robb', 'ottawa', 'solution support engineer', 22)

new_user.profile()
new_user.greet_user()
# new_user.increment_login_attempts(1)
# new_user.increment_login_attempts(1)
# new_user.increment_login_attempts(1)
# new_user.increment_login_attempts(1)
# new_user.increment_login_attempts(1)
# new_user.reset_login_attempts()
print("")

admin_user = Admin('excession', 'administrator', 'ottawa', 'Network administrator', 50)

admin_user.profile()
admin_user.greet_user()
# admin_user.priviledges.show_priviledges()
admin_user.show_priviledges()
