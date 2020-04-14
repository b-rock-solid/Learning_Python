# Try It Yourself Exercise - Pg.112
# 6-10 Favourite Numbers
########################################################################################################################
# Start with program from exercise 6-2
# Modify the program so each person can have more than 1 favourite number
# Print each person's name, along with their favourite numbers
########################################################################################################################

favourite_numbers = {
    'kevin': [69, 11],
    'jim': [21, 7],
    'pam': [11, 55, 99],
    'dwight': [80],
    'michael': [32, 1],
}

for name, numbers in favourite_numbers.items():
    if len(numbers) > 1:
        print(f"\n{name.title()}'s favourite numbers are:")
        for number in numbers:
            print(f"\t{number}")
    else:
        print(f"\n{name.title()}'s favourite number is:")
        for number in numbers:
            print(f"\t{number}")