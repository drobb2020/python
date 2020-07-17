# Crash Course
# Chapter 9 - Classes
# Exercise 9-13. Dice: 
# Make a class Die with one attribute called sides, 
# which has a default value of 6. Write a method called 
# roll_die() that prints a random number between 1 and 
# the number of sides the die has. Make a 6-sided die and 
# roll it 10 times.Make a 10-sided die and a 20-sided die. 
# Roll each die 10 times.

# from random import randint as rd
import random

class d6():
    """A simple die simulator for a 6 sided die"""

    def __init__(self):
        self.sides = 6
        self.roll_die()
    
    def roll_die(self):
        self.value = 1+random.randrange(self.sides)
        return self.value
    
    def getValue(self):
        return self.value


class d10():
    """A simple die simulator for a 10 sided die"""

    def __init__(self):
        self.sides = 10
        self.roll_die()

    def roll_die(self):
        self.value = 1+random.randrange(self.sides)
        return self.value

    def getValue(self):
        return self.value


class d20():
    """A simple die simulator for a 20 sided die"""

    def __init__(self):
        self.sides = 20
        self.roll_die()

    def roll_die(self):
        self.value = 1+random.randrange(self.sides)
        return self.value

    def getValue(self):
        return self.value


# Roll the die
d1 = d6()
d2 = d10()
d3 = d20()

print('- 6 sided die roll.')
for n in range(10):
    print(d1.roll_die())

print('- 10 sided die roll.')
for n in range(10):
    print(d2.roll_die())

print('- 20 sided die roll.')
for n in range(10):
    print(d3.roll_die())
