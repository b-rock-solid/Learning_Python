# Checking whether a value is in a list
# Use the 'in' or 'not in' statements
# This could be used to check whether a new username already exists in a list of current usernames

requested_toppings = ['mushrooms', 'onions', 'pineapple']
if 'mushrooms' in requested_toppings:
    print("Mushrooms are a valid topping")

if 'pepperoni' not in requested_toppings:
    print("Pepperoni is not a valid choice")