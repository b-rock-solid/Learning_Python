# Try It Yourself Exercise - Pg.137
# 8-4 Large Shirts
########################################################################################################################
# Modify the make_shirt() function so that shirts are Large by default and a message of 'I love Python'
# Make a large shirt and a medium shirt with the default message
# Make a shirt of any size with a different message
########################################################################################################################

def make_shirt(size='Large', print_message='I love Python'):
    """Display info on shirt size and desired printed message"""
    print(f"\nThe size of the shirt requested is {size}, with a requested message of '{print_message}'.")

# Large shirt with default message
make_shirt()

# Medium shirt with default message
make_shirt(size='Medium')

# Shirt with different size and message
make_shirt(size='Small', print_message='This is the way')