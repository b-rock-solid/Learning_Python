# Using Underscores in Numbers to make large numbers more readable
universe_age = 14_000_000_000
# Python will see this and the below as the exact same number, no matter where the underscore is
universal_age = 1_4_000_000_00_0
print(universe_age)
print(universal_age)

# Assign multiple values to more than one variable using a single line
x, y, z = 0, 8, 5
print(x, y, z)

# Constants are like variables whose value stays the same throughout the life of the program
# To indicate a variable should be treated as a constant, CAPITALIZE the letters
MAX_CONNECTIONS = 5000