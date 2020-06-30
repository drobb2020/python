# Crash Course
# Chapter 7 - User input and while loops

number = input("Enter a number, and I'll tell you if it's even or odd: ")

number = int(number)

if number % 2 == 0:
    print(f"\n>>>\tThe number {number} is even.\n")
else:
    print(f"\n>>>\tThe number {number} is odd.\n")
