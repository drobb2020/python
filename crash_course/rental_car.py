# Crash Course
# Chapter 7 - User input and while loops
# Exercise 7-1. Rental Car: Write a program that asks the user 
# what kind of rental car they would like. Print a 
# message about that car, such as 
# “Let me see if I can find you a Subaru.”

question_1 = "Hello, what is your name: "
question_2 = "welcome to weRentCars! What kind of vehicle would you like to rent: "

name = input(question_1)
car = input(question_2)

print(f"{name.title()}. Let me check if we have a {car.title()} available.")
question_3 = (f"If we don't have a {car.title()} ready. What other kind of car would you like: ")
alt_car = input(question_3)
print(f"{name.title()}, we definitely have a {alt_car.title()} available.")
