# Try It Yourself Exercise - Pg.142
# 8-6 City Names
########################################################################################################################
# Write a function called city_country()
# Function should take the name of a city and its country returning a string formatted:
# "Santiago, Chile"
########################################################################################################################

def city_country(city, country):
    """Returns a city and country of origin"""
    print(f"{city.title()}, {country.title()}")

city_country('sydney', 'australia')
city_country('auckland', 'new zealand')
city_country(city='tokyo', country='japan')