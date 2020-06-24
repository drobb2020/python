# Socratica tutorial
# sorting

# Alkaline earth metals
earth_metals = ["Beryllium", "Magnesium",
                "Calcium", "Strontium", "Barium", "Radium"]

sorted_earth_metals = sorted(earth_metals)
print(sorted_earth_metals)
print(earth_metals)

# earth_metals.sort()
# print(earth_metals)

# earth_metals.sort(reverse = True)
# print(earth_metals)


planets = [
    ("Mercury", 2440, 5.43, 0.395),
    ("Venus", 6052, 5.24, 0.73),
    ("Earth", 6378, 5.52, 1.000),
    ("Mars", 3396, 3.93, 1.530),
    ("Jupiter", 71492, 1.33, 5.210),
    ("Saturn", 60268, 0.69, 9.551),
    ("Uranus", 25559, 1.27, 19.213),
    ("Neptune", 24764, 1.64, 30.070)
]


def size(planet): return planet[1]


planets.sort(key=size, reverse=True)
print(planets)


def density(planet): return planet[2]


planets.sort(key=density, reverse=True)
print(planets)
