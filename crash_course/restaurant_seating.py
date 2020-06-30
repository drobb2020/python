# Crash Course
# Chapter 7 - User input and while loops
# Exercise 7-2. Restaurant Seating: Write a program that 
# asks the user how many people are in their dinner group. 
# If the answer is more than eight, print a message saying 
# they’ll have to wait for a table. Otherwise, report that 
# their table is ready.

welcome = "Hello and welcome to Chez Pierre, the finest French restaurant in Ottawa."
welcome += " How many are in your party: "

guests = input(welcome)

guests = int(guests)
if guests <=8:
    print("A table is available for your party right away, please follow me.")
else:
    print(f"With {guests} guests you will have to wait for a table. Please follow me to the bar.")
