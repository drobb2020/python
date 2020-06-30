# Crash Course
# Chapter 8 - Functions

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    """Print the list of toppings that have been requested."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f" - {topping}")
    print("Your pizza will be ready in 20 minutes!")

make_pizza(16, 'pepperoni', 'extra cheese')
make_pizza(12, 'mushrooms', 'green peppers', 'black olives', 'extra cheese')
make_pizza(8, 'pepperoni', 'bacon', 'mushrooms')
make_pizza(20, 'pepperoni', 'ham', 'bacon', 'salami', 'ground beef', 'sausage', 'extra cheese')
