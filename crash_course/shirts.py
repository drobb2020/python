# Crash Course
# Chapter 8 - Functions
# Exercise 8-3. T-Shirt: Write a function
# called make_shirt() that accepts a size
# and the text of a message that should be
# printed on the shirt. The function should
# print a sentence summarizing the size of
# the shirt and the message printed on it.
# Call the function once using positional
# arguments to make a shirt. Call the function
# a second time using keyword arguments.

def make_shirt(size='large', label='i love python'):
    """Make a shirt of a particular size with a customized label"""
    print("Thank you for placing a shirt order.")
    print(
        f"Your shirt will be size {size.title()}, with a custom label of '{label.title()}'.")

make_shirt()
make_shirt()
make_shirt('extra large', 'micro focus software')
make_shirt(size='small', label='bell canada')
