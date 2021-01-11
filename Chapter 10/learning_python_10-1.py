# Try It Yourself Exercise - Pg.191
# 10-1 Learning Python
########################################################################################################################
# Create a text file and write a few lines summarizing what you've learned in Python so far.
# Start each line with 'In Python you can....'
# Write a program that reads the file and prints what you wrote 3 times.
# Print the contents once by reading the entire file, once by looping over the file object
# and once by storing the lines in a list and then working with them outside the with block.
########################################################################################################################

file = 'learning_python.txt'

print("Reading entire file:")
with open(file) as file_object:
    contents = file_object.read()

print(contents.strip())

print("\nLooping over the file object:")
with open(file) as file_object:
    for line in file_object:
        print(line.strip())

print("\nStoring lines in a list:")
with open(file) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())

