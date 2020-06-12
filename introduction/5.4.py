alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
vowels = 'aeiouAEIOU'
my_string = "Packt publishing rocks!"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Sum even numbers
total = 0
for n in numbers:
    if n % 2 == 0:
        total += n
print(total)

characters = []
for ch in my_string:
    if ch not in vowels and ch in alpha:
        characters.append(ch)
consonants = ''.join(characters)
print(consonants)
