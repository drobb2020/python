# Crash Course
# Chapter 7 - User input and while loops

# current_number = 1

# while current_number <= 5:
#    print(current_number)
#    current_number += 1

current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue


    print(current_number)

# avoiding infinite loops, incrementing x avoids a loop!
x = 1
while x <= 5:
    print(x)
    x += 1

# This loop runs forever and prints the value of x (1)!
x = 1
while x <= 5:
    print(x)
