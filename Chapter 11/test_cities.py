# Try It Yourself Exercise - Pg.215
# 11-1 City, Country
########################################################################################################################
# Write a function that accepts two parameters: a city name and a country name.
# The function should return a single string of the form City, Country e.g. Santiago, Chile
# Create a file called test_cities.py that tests the function
# Write a method called test_city_country() to verify the results
########################################################################################################################

import unittest
from city_functions import get_city_country

class CitiesTestCase(unittest.TestCase):
    """Tests for 'city_functions.py'"""

    def test_city_country(self):
        """Do city country combos like 'Santiago, Chile' work?"""
        city_country = get_city_country('santiago', 'chile')
        self.assertEqual(city_country, 'Santiago, Chile')

    def test_city_country_population(self):
        """Does city, country and population like 'Santiago, Chile, 5000000' work?"""
        city_country_population = get_city_country('santiago', 'chile', 5000000)
        self.assertEqual(city_country_population, 'Santiago, Chile - population 5000000')

if __name__ == '__main__':
    unittest.main()