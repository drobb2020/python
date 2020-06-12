
# --------------------------------------------
# Write a program that given two numbers a, b print
# divisible if one of the two numbers divides the other
# a, b = int(input("a = ")), int(input("b = "))
# if a % b == 0 or b % a == 0:
#    print("The numbers are divisible")

# --------------------------------------------
# Given input a, b print a/b if b is not equal to zero

# a, b = int(input("a = ")), int(input("b = "))
# if b != 0:
#    print(a/b)
# if not(b == 0):
#    print(a/b)

# --------------------------------------------
# Write a program that given three names prints "equal"
# if all three names are equal to each other when lowercase
name1 = input("name1: ")
name2 = input("name2: ")
name3 = input("name3: ")

if name1.lower() == name2.lower() == name3.lower():
    print("The three names are equal")
