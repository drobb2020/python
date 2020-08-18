# Python Crash Course 2e
# Chapter 10 - Files and Exceptions
# division_calculator.py

# print(5/0) # results in a ZeroDivisionError

try:
    print(5/0)
except ZeroDivisionError:
    print("you can't divide by zero!")

print("Give me two numbers, and I will divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("\nSecond number: ")
    if second_number == 'q':
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You cannot divide by zero!")
    else:
        print(answer)
