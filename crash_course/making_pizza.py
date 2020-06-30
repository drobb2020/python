# Crash Course
# Chapter 8 - Functions

# imports the pizza3.py function
import pizza3
# sets an alias of p for pizza3
import pizza3 as p
# imports only the make_pizza function
from pizza3 import make_pizza
# imports all functions in pizza3, 
# but you don't need to preface pizza3 on the command
from pizza3 import *
# import only make_pizza and set an alias of pizza
from pizza3 import make_pizza as pizza

pizza3.make_pizza(16, 'pepperoni')
pizza3.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
pizza3.make_pizza(8, 'pepperoni', 'bacon', 'mushrooms')
pizza3.make_pizza(20, 'pepperoni', 'bacon', 'ham', 'sausage', 'ground beef', 'salami', 'extra cheese')

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
make_pizza(8, 'pepperoni', 'bacon', 'mushrooms')
make_pizza(20, 'pepperoni', 'bacon', 'ham', 'sausage', 'ground beef', 'salami', 'extra cheese')

pizza(16, 'pepperoni')
pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
pizza(8, 'pepperoni', 'bacon', 'mushrooms')
pizza(20, 'pepperoni', 'bacon', 'ham', 'sausage', 'ground beef', 'salami', 'extra cheese')
