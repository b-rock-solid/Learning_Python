# Try It Yourself Exercise - Pg.215
# 11-1 City, Country
########################################################################################################################
# Write a function that accepts two parameters: a city name and a country name.
# The function should return a single string of the form City, Country e.g. Santiago, Chile
# Create a file called test_cities.py that tests the function
# Write a method called test_city_country() to verify the results
########################################################################################################################

def get_city_country(city, country, population=''):
    """Generate a neatly formatted city and country string."""
    city_country = f"{city.title()}, {country.title()}"
    if population:
        city_country += f" - population {population}"
    return city_country