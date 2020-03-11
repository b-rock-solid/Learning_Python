# Try It Yourself Exercise - Pg.85
# 5-5 Alien Colours #3
########################################################################################################################
# Turn your if-else chain from exercise 5-4 into an if-elif-else chain
# If alien colour is green, print a message that the player earned 5 points
# If alien colour is yellow, print a message that the player just earned 10 points
# If alein colour is red, print a message that the player just earned 15 points
# Write three versions that run each different message for the different colour alien
########################################################################################################################

# Green version
alien_colour = 'green'

if alien_colour == 'green':
    points = 5
elif alien_colour == 'yellow':
    points = 10
elif alien_colour == 'red':
    points = 15

print(f"Nice shot! You just scored {points} points!")

# Yellow version
alien_colour = 'yellow'

if alien_colour == 'green':
    points = 5
elif alien_colour == 'yellow':
    points = 10
elif alien_colour == 'red':
    points = 15

print(f"Nice shot! You just scored {points} points!")

# Red version
alien_colour = 'red'

if alien_colour == 'green':
    points = 5
elif alien_colour == 'yellow':
    points = 10
elif alien_colour == 'red':
    points = 15

print(f"Nice shot! You just scored {points} points!")