# Socratica tutorial
# Sets

example = set()

example.add(42)
example.add(False)
example.add(3.14159)
example.add("Thorium")

print(example)

example.add(42)

print(example)
print(len(example))

example.remove(42)
print(example)

# example.remove(50)
example.discard(50)

example2 = set([28, True, 2.718281828, "Helium"])
print(example2)
print(len(example2))
example2.clear()
print(len(example2))

odds = set([1, 3, 5, 7, 9])
evens = set([2, 4, 6, 8, 10])
primes = set([2, 3, 5, 7])
composites = set([4, 6, 8 , 9, 10])
print(odds.union(evens))
print(evens.union(odds))
print(odds.intersection(primes))
print(evens.intersection(primes))
print(primes.union(composites))

print(2 in primes)
print(6 in odds)
