pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
    }

#summerize the order
print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings: ")

for topping in pizza['toppings']:
    print(f"\t{topping}")

# pizza = ['canadian', 'hawaiian', 'pepperoni', 'meat lovers']

# for pie in pizza:
#     print(f"The best pizza is {pie.title()}!")

# print("I guess I really love pizza, huh.")

# animals = ['dog', 'cat', 'bird', 'fish']

# for pet in animals:
#     print(f"A {pet} would make a great companion.")

# print("Any of these animals wound make a great pet!")
