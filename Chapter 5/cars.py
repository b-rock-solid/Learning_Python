# Using if statements
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# A single '=' is a statement; code at line 2 "Set the value of cars to the listed values"
# A double '==' asks a question: "Is the value of car equal to 'bmw'?"

# Testing for equality is case sensitive in Python. E.g, two values with different capitalization
# is not considered equal:
# car = 'Audi'
# car == 'audi'
# This would return a false instead of the intended true

# If case matters, this behaviour is advantages. If it doesn't matter, you can convert the variable to lowercase:
# car = 'Audi'
# car.lower() == 'audi'
# This would return True