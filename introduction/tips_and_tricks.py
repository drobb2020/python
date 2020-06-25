# Corey Schafer
# 10 python tips and tricks for writing better code

# #1
"""If condition is True, x = 1, else x = 0"""

# condition = True
from getpass import getpass
condition = False

if condition:
    x = 1
else:
    x = 0

print(x)

"""Can be written on one line to achieve the same results"""
x = 1 if condition else 0

print(x)

# #2
"""Working with large numbers is difficult to read, 
but you cannot use commas, however, you can use an 
underscore without affecting the code"""

# num1 = 10000000000
# num2 = 100000000
"""Can be written"""
num1 = 10_000_000_000
num2 = 100_000_000

total = num1 + num2

print(total)
"""To include separators in the output use an f string"""
print(f'{total:,}')

# #3
"""Common bad practice. Opening and closing files!"""
"""Common way"""
# f = open('test.txt', 'r')
# file_contents = f.read()
# f.close()

"""Use a context manager"""
# with open('test.txt', 'r') as f:
#    file_contents = f.read()

#words = file_contents.split(' ')
#word_count = len(words)
# print(word_count)

# #4
"""Enumerate function"""
names = ['Corey', 'Chris', 'Dave', 'Travis']

index = 0
for name in names:
    print(index, name)
    index += 1

for index, name in enumerate(names, start=1):
    print(index, name)

# #5
"""Enumerate over two lists at the same time"""
"""Typical"""
names1 = ['Peter Parker', 'Clark Kent', 'Wade Wilson', 'Bruce Wayne']
heroes = ['Siderman', 'Superman', 'Deadpool', 'Batman']
universes = ['Marvel', 'DC', 'Marvel', 'DC']

for index, name in enumerate(names1):
    hero = heroes[index]
    print(f'{name} is actually {hero}')

"""Better Suggestion"""
for name, hero in zip(names1, heroes):
    print(f'{name} is actually {hero}')

# to add a third list
for name, hero, universe in zip(names1, heroes, universes):
    print(f'{name} is actually {hero} from {universe}')

# #6
# Unpacking
# normal
items = (1, 2)

print(items)

# Unpacking
a, b = (1, 2)

print(a)
print(b)

c, d, *e, f = (1, 2, 3, 4, 5)

print(c)
print(d)
print(e)
print(f)

# #7
# Setting and getting attributes


class person():
    pass


person = person()

person.first = "David"
person.last = "Robb"

# print(person.first)
# print(person.last)

first_key = 'first'
first_val = 'David'

setattr(person, first_key, 'David')

first = getattr(person, first_key)

print(person.first)
print(first)

person_info = {'first': 'David', 'last': 'Robb'}

for key, value in person_info.items():
    setattr(person, key, value)

# print(person.first)
# print(person.last)
for key in person_info.keys():
    print(getattr(person, key))

# #8
# Inputting secret information (passwords)

username = input('Username: ')
password = input('Password: ')

print('Logging In...')


username = input('Username: ')
password = getpass('Password: ')

print('Logging In...')

# #9
# sys. path
"""General information about using the -m switch with python,
and using the help function to find additional information."""
# Using help
# execute an import on a module
import smtpd
# now print the help - better in an interactive python terminal
print(help(smtpd))

# Using dir
# On the imported module type - better in an interactive python terminal
print(dir(smtpd))
