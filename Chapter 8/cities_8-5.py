# Try It Yourself Exercise - Pg.137
# 8-5 Cities
########################################################################################################################
# Write a function called describe_city() that accepts the name of a city and its country
# Print a simple sentence
# Give the parameter for country a default value
# Call your function 3 times for 3 different cities, one of which not in the default country
########################################################################################################################

def describe_city(city, country='australia'):
    """Describes a city and it's country of origin"""
    print(f"\n{city.title()} is in {country.title()}")

describe_city('melbourne')
describe_city('perth', country='australia')
describe_city(city='auckland', country='new zealand')