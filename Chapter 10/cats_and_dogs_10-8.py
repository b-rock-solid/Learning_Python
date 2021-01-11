# Try It Yourself Exercise - Pg.202
# 10-8 Cats and Dogs
########################################################################################################################
# Make two files, cats.txt and dogs.txt. Store at least three names in each file.
# Write a program that tries to read these files and print the contents of the file to the screen.
# Wrap your code in a try-except block to catch the FileNotFound error, and print a user friendly error message.
########################################################################################################################

def show_contents(filename):
    """Reads and prints the contents of a file."""
    try:
        with open(filename) as f:
            contents = f.readlines()
    except FileNotFoundError:
        print(f"Sorry, we can't find the file {filename}.")
    else:
        print(f"\n{filename} has the following names:")
        for line in contents:
            print(line.strip())


show_contents('dogs.txt')
show_contents('cats.txt')