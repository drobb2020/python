motorcycles = ["Honda", "Suzuki", "Yamaha"]
print(motorcycles)

# motorcycles[0] = "Ducati"
# print(motorcycles)

motorcycles.append('Ducati')
print(motorcycles)

motorcycles.append('BMW')
print(motorcycles)

motorcycles.insert(5, 'Norton')
print(motorcycles)

del motorcycles[0]
print(motorcycles)

motorcycles.insert(0, 'Honda')
print(motorcycles)

motorcycles2 = ['honda', 'yamaha', 'suzuki']
print(motorcycles2)
popped_motorcycle = motorcycles2.pop()
print(motorcycles2)
print(popped_motorcycle)

first_owned = motorcycles2.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")
