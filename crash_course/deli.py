# Crash Course
# Chapter 7 -User input and while loops
# Exercise 7-8. Deli: Make a list called sandwich_orders 
# and fill it with the names of various sandwiches. 
# Then make an empty list called finished_sandwiches. 
# Loop through the list of sandwich orders and 
# print a message for each order, such as I made 
# your tuna sandwich. As each sandwich is made, move 
# it to the list of finished sandwiches. 
# After all the sandwiches have been made, 
# print a message listing each sandwich that was made.

sandwich_order = ['tuna salad', 'chicken salad', 'pastrami', 'egg salad', 'roast beef', 'bacon lettuce and tomato', 'rueben', 'pastrami', 'steak', 'pastrami', 'smoked meat']
finished_sandwiches = []

while 'pastrami' in sandwich_order:
    sandwich_order.remove('pastrami')

while sandwich_order:
    current_sandwich = sandwich_order.pop()

    print(f"I'm making the {current_sandwich.title()} sandwich")
    finished_sandwiches.append(current_sandwich)

# Display all finished sandwiches
print("\nThe following sandwiches were made:")
for finished_sandwich in finished_sandwiches:
    print(f"I made your {finished_sandwich.title()} sandwich!")
