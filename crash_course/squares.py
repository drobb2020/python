squares = []
for value in range(1, 11):
    #    square = value ** 2
    squares.append(value ** 2)
print(squares)

squares2 = [value**2 for value in range(1, 11)]
print(squares2)

for value in range(1, 21):
    print(value)

million = []
# for num in range(1, 1000001):
#    million.append(num)
# print(million)

# print(min(million))
# print(max(million))
# print(sum(million))

odd_numbers = list(range(1, 21, 2))
print(odd_numbers)

threes = [value*3 for value in range(3, 31)]
print(threes)

cubes = []
for value in range(1, 11):
    cubes.append(value ** 3)
print(cubes)

cubes2 = [value**3 for value in range(1, 11)]
print(cubes2)
