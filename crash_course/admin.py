# Crash Course
# Chapter 9 - Classes
# Exercise 9-12. Multiple Modules: 
# Store the User class in one module, 
# and store the Privileges and Admin 
# classes in a separate module. 
# In a separate file, create an Admin 
# instance and call show_privileges() 
# to show that everything is still 
# working correctly.

from user import User

class Priviledges():
    """Priviledges granted to administrators"""

    def __init__(self, priviledges=['- can add post', '- can delete post', '- can add user', '- can ban user', '- can edit post']):
        #self.priviledges = ['- can add post', '- can delete post', '- can add user', '- can ban user', '- can edit post']
        self.priviledges = priviledges

    def show_priviledges(self):
        print("As administrator you have the following priviledges:")
        for priviledge in self.priviledges:
            print(priviledge)


class Admin(User):
    """Special user class with additional rights"""

    def __init__(self, first, last, location, profession, experience):
        """Initialize attributes of the parent class."""
        super().__init__(first, last, location, profession, experience)
        self.priviledges = Priviledges()
