# Crash Course
# Chapter 7 - User input and while loops
# Exerciese 7-3. Multiples of Ten: Ask the user for a number,
# and then report whether the number is a multiple of 10 or not.

number_x = "\nPlease enter any number you want and I'll let you know if it is a multiple of 10:  "

num = input(number_x)

num = int(num)

if num % 10 == 0:
    print(f"\n>>>\tThe number {num} is multiple of 10.\n")
else:
    print(f"\n>>>\tThe number {num} is not a multiple of 10.\n")
