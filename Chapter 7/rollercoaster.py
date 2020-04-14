# Using int() to Accept Numerical Input
# Using the input() function, Python interprets everything the user enters as a string
# If you need to use the input as an integer, use the int() function

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little taller.")