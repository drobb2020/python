# Crash Course
# Chapter 9 - Classes
# Exervise 9-11, 9-12

from user import User
from admin import Admin

admin_user = Admin('excession', 'administrator',
                   'ottawa', 'Network administrator', 50)

admin_user.profile()
admin_user.greet_user()
admin_user.priviledges.show_priviledges()
