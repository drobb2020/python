# Crash Course
# Chapter 7 - User input and while loops
# Exercise 7-4. Pizza Toppings: 
# Write a loop that prompts the user to enter
# a series of pizza toppings until they enter 
# a 'quit' value. As they enter each topping, 
# print a message saying you’ll add that 
# topping to their pizza.

print("\nWe have the following toppings available today")
meat_toppings = ('pepperoni', 'bacon', 'ham', 'salami', 'ground beef', 'chicken')
veg_toppings = ('green pepper', 'mushrooms', 'green olives', 'black olives',)
fruit_toppings = ('pineapple', 'tomatoes')
cheese_toppings = ('mozarella', 'feta', 'parmesan', 'extra cheese')

for meat in meat_toppings:
    print(meat)

for veg in veg_toppings:
    print(veg)

for fruit in fruit_toppings:
    print(fruit)

for cheese in cheese_toppings:
    print(cheese)

prompt = "What toppings would you like on your pizza: "
prompt += "When you have finished selecting your toppings type quit. "

while True:
    pizza = input(prompt)

    if pizza == 'quit':
        break
    else:
        print(f"{pizza.title()} will be added to your pizza!")
