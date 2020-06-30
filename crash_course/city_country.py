# Crash Course
# Chapter 8 - Functions
# Exercise 8-6. City Names: Write a function 
# called city_country() that takes in the name 
# of a city and its country. The function should 
# return a string formatted like this:
# "Santiago, Chile"
# Call your function with at least three city-country 
# pairs, and print the values that are returned.

def city_country(city, country):
    """Function to format a city and country into a neat string."""
    c_c = (f"{city}, {country}")
    return c_c.title()


while True:
    print("\nPlease provide a city and the country:")
    print("(enter 'q' at any time to quit)")
    ci_name = input("City: ")
    if ci_name == 'q':
        break
    co_name = input("Country: ")
    if co_name == 'q':
        break

    formatted_name = city_country(ci_name, co_name)
    print(f"\nHello, {formatted_name}!")
