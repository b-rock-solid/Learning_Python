# A Simple Dictionary
# alien_0 stores the colour and points value for this particular alien
# it is then accessed as seen with the print commands


alien_0 = {'colour': 'green', 'points': 5}

print(alien_0['colour'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just earned {new_points} points!")

print(alien_0)

# Adding new Key-Value Pairs to dictionaries
# Lets add two new pieces of info to alien_0: the alien's x- and y- coordinates

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# You are able to start with an empty dictionary and add each new item to it
print("\nStarting With an Empty Dictionary")

alien_0 = {}

alien_0['colour'] = 'green'
alien_0['points'] = 5

print(alien_0)

# Modifying Values in a Dictionary
print("\nModifying Values in a Dictionary:")

alien_0 = {'colour': 'green'}
print(f"The alien is {alien_0['colour']}.")

alien_0['colour'] = 'yellow'
print(f"The alien is now {alien_0['colour']}.")

# Lets track the position of an alien that can move at different speeds
# Start by storing the alien's current speed, then use this to determine how far to the right it should move
print("\nTracking an Alien's Position Example:")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': "medium"}
print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

# The new position is the old position plus the increment
alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

# Removing Key-Value Pairs
# All the 'del' command needs is the name of the dictionary and the key you want to remove
print(f"\nRemoving Key-Value Pairs:")

alien_0 = {'colour': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)