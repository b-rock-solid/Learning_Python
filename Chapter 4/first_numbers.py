# Using the range() function
# Use the range() function to generate a series of numbers
print("Range provided (1, 5):")
for value in range(1, 5):
    print(value)
# Because of the 'off-by-one' behaviour of some programming languages, it prints the numbers 1-4 not the expected 1-5
# Python counts from the first value provided and stops when it reaches the second value.
# Because it stops, the output doesn't contain the final value, which would have been 5
# To print numbers 1-5, you would use range(1, 6)
print("\nCorrect range provided:")
for value in range(1, 6):
    print(value)
# You can pass range() with one argument. It will start the sequence of numbers from 0
# Example, range(6) would return numbers 0-5

# Using range() function to create a list of numbers
# Wrap the list() around a call to the range() function, the output will be a list
print("\nList of Numbers:")
numbers = list(range(1, 6))
print(numbers)

