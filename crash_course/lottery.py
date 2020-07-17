# Crash Course
# Chapter 9 - Classes
# Exercise 9-14. Lottery: 
# Make a list or tuple containing 
# a series of 10 numbers and five letters. 
# Randomly select four numbers or letters 
# from the list and print a message saying 
# that any ticket matching these four numbers 
# or letters wins a prize.

import random

class Lottery():
    """lottery simulator."""
    def __init__(self):
        self.list = (4, 10, 16, 24, 34, 58, 39, 22, 75, 61, 'd', 'a', 'v', 'e', 'r')
    
    def generate_combo(self):
        self.value = 1+random.randrange(self.list)
        return self.value

    def getValue(self):
        return self.value
    

ticket = Lottery()

for n in range(4):
    print('I you have the following combination of numbers and letters, you are a winner!')
    print(ticket.generate_combo())
