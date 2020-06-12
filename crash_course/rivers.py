'''even more dictionaires practice'''
rivers = {
    'mississippi': 'usa',
    'nile': 'egypt',
    'yellow': 'china',
    'rhine': 'germany',
    'thames': 'england',
    'seine': 'france',
}

for river, country in rivers.items():
    if country == 'usa':
        print(f"The {river.title()} river runs through {country.upper()}.")
    else:
        print(f"The {river.title()} river runs through {country.title()}.")

print("\nThe rivers in my dictionary are:")
for river in sorted(rivers.keys()):
    print(f"{river.title()}")

print("\nThe Countries in my dictionary are:")
for country in sorted(rivers.values()):
    if country == 'usa':
        print(f"{country.upper()}")
    else:
        print(f"{country.title()}")
