# Crash Course
# Exercise 6.11 Cities

"""Cities: Make a dictionary called cities. 
Use the names of three cities as keys in your dictionary. 
Create a dictionary of information about each city and 
include the country that the city is in, its approximate 
population, and one fact about that city. The keys for each 
city’s dictionary should be something like country, 
population, and fact. Print the name of each city and all 
of the information you have stored about it.
    """

cities = {
    'toronto': {
        'country': 'canada',
        'population': 6.19,
        'fact': 'largets city in Canada'
    },
    'ottawa': {
        'country': 'canada',
        'population': 1.39,
        'fact': 'capital of Canada'
    },
    'montreal': {
        'country': 'canada',
        'population': 4.22,
        'fact': 'largest french speaking population outside of France.'
    }
}

# print(cities)

for city, city_info in cities.items():
    # print(f"\nThe city of {city.title()}")
    country = city_info['country']
    population = city_info['population']
    fact = city_info['fact']

    print(f"The city of {city.title()} is located in {country.title()}. ")
    print(f"{city.title()} has a population of {population} million.")
    print(f"{city.title()} is the {fact}")
    print("")
