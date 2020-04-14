# Try It Yourself Exercise - Pg.112
# 6-11 Cities
########################################################################################################################
# Make a dictionary called cities
# Use the names of the cities as the keys of the dictionary
# Create a dictionary of information about each city
# Include information such as Country the city is in, approx population and a fact about the city
# Print the name of each city and all information regarding it
########################################################################################################################

cities = {
    'melbourne': {
        'country': 'australia',
        'population': '4.9 million',
        'fact': 'The tramway system is the largest outside Europe and the fourth largest in the world',
    },
    'tokyo': {
        'country': 'japan',
        'population': '9.2 million',
        'fact': 'Tokyo was formerly known as "Edo" in the 20th century',
    },
    'moscow': {
        'country': 'russia',
        'population': '11.9 million',
        'fact': "The Moscow Kremlin is the world's largest medieval fortress",
    },
}

for city, info in cities.items():
    country = info['country']
    population = info['population']
    fact = info['fact']
    print(f"\nThe city of {city.title()} is located in the country of {country.title()},"
          f" with an approximate population of {population} people.")
    print(f"An interesting fact about {city.title()} is:")
    print(f"{fact}")