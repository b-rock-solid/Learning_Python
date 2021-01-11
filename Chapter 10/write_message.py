# Writing to an Empty File

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming. \n")
    file_object.write("I love creating new games. \n")

# You can open files in different ways:
# read mode - 'r'
# write mode - 'w'
# append mode - 'a'
# read/write mode - 'r+'

# By default, Python opens files in read only mode
# Python can only write strings to a text file.
# If you want to store numerical data in a text file, you'll have to convert the data to string format first.
# Use the str() function to achieve this.


# Appending to a File

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets. \n")
    file_object.write("I love creating apps that can run in a browser. \n")