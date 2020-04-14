# Try It Yourself Exercise - Pg.112
# 6-7 People
########################################################################################################################
# Start with the program from exercise 6-1
# Make two new dictionaries representing 2 more people
# Store all 3 dictionaries in a list called 'people'
# Loop through the list and print everything we know about them
########################################################################################################################

person_0 = {'first_name': 'pam', 'last_name': 'beesley', "age": 26, 'city': 'scranton'}
person_1 = {'first_name': 'jim', 'last_name': 'halpert', "age": 28, 'city': 'scranton'}
person_2 = {'first_name': 'jan', 'last_name': 'levingston', "age": 42, 'city': 'new york'}

people = [person_0, person_1, person_2]

for person in people:
    print(f"{person['first_name'].title()} {person['last_name'].title()} is {person['age']} "
          f"and lives in the city of {person['city'].title()}.")