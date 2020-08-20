# Python Crash Course 2e
# Chapter 11 - Testing your code
# city_function.py
# Exercise 11-1 City, Country:
# Write a function that accepts two parameters:
# a city name and a country name. The function should return
# a single string of the form City, Country, such as Santiago, Chile.
# Store the function in a module called city_functions.py.Create a file
# called test_cities.py that tests the function you just wrote
# (remember that you need to import unittest and the function you want
# to test). Write a method called test_city_country() to verify that
# calling your function with values such as 'santiago' and 'chile' results
# in the correct string. Run test_cities.py, and make sure test_city_country()
# passes.

import unittest
from city_functions import city_country


class NamesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'."""

    def test_city_country(self):
        """Do names like Toronto, Canada"""
        formatted_name = city_country('toronto', 'canada')
        self.assertEqual(formatted_name, 'Toronto, Canada')


    def test_city_country_population(self):
        """Test city names with their population"""
        formatted_name = city_country('toronto', 'canada', '6197000')
        self.assertEqual(formatted_name, 'Toronto, Canada - Population 6197000')

if __name__ == '__main__':
    unittest.main()
