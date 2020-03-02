# Try It Yourself Exercise - Pg.65
# 4-10 Slices
# Use a previous program from this chapter and use slices to:
# Print first three items in the list, three items in the middle and the last three items in the list
cubes = []
for value in range(1, 11):
    cubes.append(value**3)
    print(cubes[-1])
print(cubes)

print(f"\nThe first three items in the list are:\n{cubes[0:3]}")
print(f"\nThree items from the middle of the list are:\n{cubes[3:6]}")
print(f"\nThe last three items in the list are:\n{cubes[-3:]}")