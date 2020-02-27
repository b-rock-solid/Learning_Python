# Making a list of numbers for the first 10 square numbers
# The square of each integer from 1 through 10
# In Python (**) represents exponents
squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

# To make this code more efficient, we can omit the temporary variable 'square' and append each new value directly to the list:
print("\nSquares using a more efficient code:")
squares = []
for value in range(1, 11):
    squares.append(value**2)

print(squares)

# Either of these methods work, however method 1 using a temporary variable makes it easier to read the code and what it's doing
# Focus on writing code that you understand clearly and does what you want it to do. Then look for more efficient approaches as
# you review your code.

# List comprehension is a more advanced way to generate the same list in one line of code
print("\nSquares using List Comprehension")
squares = [value**2 for value in range(1, 11)]
print(squares)