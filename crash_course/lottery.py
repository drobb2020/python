# Crash Course
# Chapter 9 - Classes
# Exercise 9-14. Lottery: 
# Make a list or tuple containing 
# a series of 10 numbers and five letters. 
# Randomly select four numbers or letters 
# from the list and print a message saying 
# that any ticket matching these four numbers 
# or letters wins a prize.

from random import choice

possibilities = [4, 10, 16, 24, 34, 58, 39, 22, 75, 61, 'd', 'a', 'v', 'e', 'r']

winning_ticket = []

print("Let's see what the winning ticket is today...")

while len(winning_ticket) <4:
    random_draw = choice(possibilities)

    if random_draw not in winning_ticket:
        print(f" We pulled: {random_draw}!")
        winning_ticket.append(random_draw)
