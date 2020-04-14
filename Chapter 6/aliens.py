# Nesting Items
# Sometimes you'll want to store multiple dictionaries in a list,
# or a list of items as a value in a dictionary.
# You can nest dictionaries inside a list, a list of items inside a dictionary,
# or even a dictionary inside another dictionary

# A list of Dictionaries

alien_0 = {'colour': 'green', 'points': 5}
alien_1 = {'colour': 'yellow', 'points': 10}
alien_2 = {'colour': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# A more realistic version of this code would be more than 3 aliens
# Below we automatically generate 30 aliens using the range() method

# Make an empty list for storing aliens
aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'colour': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print('...')

# Show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")


# These aliens all have the same characteristics, by Python considers each one a separate object
# This allows us to modify each alien individually
# When we want to change the aliens colour and moving faster,
# we can use a for loop and an if statement to change the colour of aliens.

# Starting with the same code as before:

# Make an empty list for storing aliens
aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'colour': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# Change first 3 aliens from green to yellow
# Added elif function, if alien colour is yellow, turn it to red
for alien in aliens[:3]:
    if alien['colour'] == 'green':
        alien['colour'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['colour'] == 'yellow':
        alien['colour'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)
print('...')

# Show how many aliens have been created
print(f"Total number of aliens: {len(aliens)}")