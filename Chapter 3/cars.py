# Sorting the list permanently using the sort() method. Once sorted, it cannot be reverted
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

# Sorting the list in reverse alphabetical order. Again, this permanently changes the order of the list
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

# Temporarily sorting a list is done using the sorted() method
# The sorted method can also accept the reverse=True argument
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

# Printing a list in reverse order
# Using reverse() also changes the list permanently, but easily reverted by applying reverse() again
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("\nPrinting a list in reverse:")
print(cars)
cars.reverse()
print(cars)

# Finding the length of a list using the len() method
cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)
print(len(cars))