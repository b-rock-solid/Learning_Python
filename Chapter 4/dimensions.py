# Tuples
# A tuple is a list of items that cannot change.
# Python refers to values that cannot change as immutable, and an immutable list is called a tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# NOTE: Tuples are technically defined by the presence of a comma. If you want to define a tuple with one element,
# you need to include a trailing comma: my_tupple = (3,)

# Looping Through All Values in a Tuple
# You can loop over values in a tuple the same as a normal list
for dimension in dimensions:
    print(dimension)

# You can't modify a tuple, however you can assign a new value to a variable representing a tuple
print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)