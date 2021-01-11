# Read an entire file
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
print(contents.rstrip())

# Telling python the file path for the open() function
# To look in a sub-directory of the current working directory, you would use the below:
# with open('text_files/filename.txt') as file_object:
# NOTE: You can use / slashes even if running on Windows in your code

# Using absolute paths it may be a good idea to first assign it to a variable as they are usually long
# file_path = "D:/python_work/Chapter 10/pi_digits.txt"
# with open(file_path) as file_object:

# NOTE: If using \ slashes, use 2 '\\'.
# This is because a single \ in Python is seen as an escape character.
# E.g.
#   file_path = "D:\\python_work\\Chapter 10\\pi_digits.txt"

# Reading Line by Line
filename = 'pi_digits.txt'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())


# Making a List of Lines from a File
filename = 'pi_digits.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())