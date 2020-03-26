# Try It Yourself Exercise - Pg.105
# 6-5 Rivers
########################################################################################################################
# Make a dictionary containing three major rivers and the country each river runs through
# Use a loop to print a sentence about each river
# Use a loop to print the name of each river included in the dictionary
# Use a loop to print the name of each country included in the dictionary
########################################################################################################################
rivers = {
    'nile': 'egypt',
    'murray': 'australia',
    'mississippi': 'united states',
    'mekong': 'cambodia',
}

for river, country in rivers.items():
    print(f"The {river.title()} river runs through the country {country.title()}.")

print("\nThe name of rivers mentioned are:")
for river in rivers.keys():
    print(river.title())

print("\nThe name of countries mentioned are:")
for country in rivers.values():
    print(country.title())