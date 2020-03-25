# Looping through a Dictionary
# Dictionaries can be looped through in several different ways:
# Loop all key-value pairs, through its keys or through its values

# Looping Through All Key-Value Pairs
user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# At line 12 you create names (key & value) for the 2 variables that will hold the key and value in each key-value pair.
# The name of the dictionary is followed by the method 'items()'
# This returns a list of key-value pairs. The for loop then assigns each of these pairs to the two variables provided.