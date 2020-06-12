'''More dictionary fun'''
numbers = {
    'nick': 44,
    'robert': 19,
    'mark': 99,
    'david': 42,
    'bryan': 9,
}

print(numbers)

for key, value in numbers.items():
    print(key, ' : ', value)

print('\n')
for key in numbers:
    print(key, ' : ', numbers[key])

print('\n')
[print(key, value) for key, value in numbers.items()]
