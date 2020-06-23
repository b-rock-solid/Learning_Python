# Try It Yourself Exercise - Pg.131
# 8-2 Favourite Book
########################################################################################################################
# Write a function called favourite_book() that accepts one parameter, title
# The function should print a message such as "One of my favourite books is Alice in Wonderland"
# Call the function making sure to include a book title as an argument in the function call
########################################################################################################################

def favourite_book(title):
    """Print a message for someone's favourite book"""
    print(f"One of my favourite books is {title.title()}")

favourite_book('alice in wonderland')