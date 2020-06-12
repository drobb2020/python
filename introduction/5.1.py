# for loop
s = "hello world"
a = [4, 6, 9]

print(5 in a)
print(4 in a)
print("ello" in s)

for number in [2, 4, 6, 8, 10]:
    print(number)

odds = [1, 3, 5, 7, 9, 11]
for odd_numbers in odds:
    print(odd_numbers)

print(range(len(odds)))
for index in range(len(odds)):
    print("Index: {:d}, odd numbers: {:d}".format(index, odds[index]))
