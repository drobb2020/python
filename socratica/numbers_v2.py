# Socratica tutorial
# numbers in python v2
# Use python 2.7.x to run this script
# Types of numbers: int, long, float, complex
# whole numbers: int, long
import sys

a = 28
b = 2147483647
c = 2147483648
d = -sys.maxint - 1
e = -2147483649

print(type(a))
print(a)
print(type(b))
print(b)
print(type(c))
print(c)
print(type(d))
print(d)
print(type(e))
print(e)

f = 2.718281828
print(type(f))
print(f)

z = 3 + 5.7j
print(type(z))
print(z)
print(z.real)
print(z.imag)
