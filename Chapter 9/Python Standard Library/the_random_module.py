########################################################################################################################
# The Python standard library is a set of modules included with every Python installation.
########################################################################################################################

# The random module
# randint() function takes two interger arguments and returns a
# randomly selected integer between (and including) those numbers

from random import randint

print(randint(1, 6))

# The choice() function
# Takes a list or tuple and returns a randomly chosen element

from random import choice

players = ['charles', 'martina', 'michael', 'florence', 'eli']
first_up = choice(players)
print(first_up)

# The random module SHOULDN'T be used when building security-related applications.
# It is good enough for many fun and interesting projects however