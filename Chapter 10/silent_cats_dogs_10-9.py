# Try It Yourself Exercise - Pg.202
# 10-9 Silent Cats and Dogs
########################################################################################################################
# Modify the except block in Exercise 10-8 to fail silently if either file is missing.
########################################################################################################################

def show_contents(filename):
    """Reads and prints the contents of a file."""
    try:
        with open(filename) as f:
            contents = f.readlines()
    except FileNotFoundError:
        pass
    else:
        print(f"\n{filename} has the following names:")
        for line in contents:
            print(line.strip())


show_contents('dogs.txt')
show_contents('cats.txt')