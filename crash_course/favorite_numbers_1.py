# Crash Course
# Exwecise 6.10 - modified favorite numbers
'''More dictionary fun'''
numbers = {
    'nick': [44, 10, 99, 10],
    'robert': [19, 11, 26, 66],
    'mark': [99, 7, 45, 19],
    'david': [42, 7, 63, 57],
    'bryan': [9, 11, 15, 17]
}

# print(favorite_numbers)
for name, num in numbers.items():
    print(f"\n{name.title()}'s favorite numbers are: ")
    for number in num:
        print(f"\t{number}")
