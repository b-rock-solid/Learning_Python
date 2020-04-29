# Try It Yourself Exercise - Pg.137
# 8-3 T-Shirt
########################################################################################################################
# Write a function called make_shirt()
# The function should accept a size and the text of a message that should be printed on the shirt
# It should print a sentence summarizing the size of the shirt and the message to be printed on it
# Call the function a second time using keyword arguments
########################################################################################################################

def make_shirt(size, print_message):
    """Display info on shirt size and desired printed message"""
    print(f"The size of the shirt requested is {size}, with the requested message of '{print_message}'.")

make_shirt(14, 'This is da way')
make_shirt(size='L', print_message='No, this is the way')