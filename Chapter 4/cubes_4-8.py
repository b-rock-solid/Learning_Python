# Try It Yourself Exercise - Pg.60
# 4-8 Cubes
# Make a list of the first 10 cubes (each integer from 1 through 10)
# Use a for loop to print out the value of each cube
cubes = []
for value in range(1, 11):
    cubes.append(value**3)
    print(cubes[-1])
print(cubes)