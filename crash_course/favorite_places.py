# Crash Course
# Exercise 6.9 - faviroite places

favorite_places = {
    'david': ['edinburgh', 'paris', 'newport'],
    'joan': ['glasgow', 'new york', 'toronto'],
    'bill': ['detroit', 'fort lauderdale', 'tampa'],
    'john': ['dallas', 'salt lake city', 'las vegas'],
    'jennifer': ['halifax', 'vancouver', 'edmonton'],
    'erin': ['berlin', 'munich', 'bern'],
    'brianna': ['rio de jeneiro', 'bogota', 'macu pikcu'],
}

# print(favorite_places)
for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are: ")
    for place in places:
        print(f"\t{place.title()}")
