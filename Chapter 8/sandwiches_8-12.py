# Try It Yourself Exercise - Pg.150
# 8-12 Sandwiches
########################################################################################################################
# Write a function that accepts a list of items a person wants on a sandwich
# The function should have one parameter that collects as many items as the function call provides
# It should print a summary of the sandwich that's being ordered
########################################################################################################################

def make_sandwich(bread, *fillings):
    """Creates a sandwich with the requested fillings from a customer."""
    print(f"\nMaking a sandwich on {bread} bread, with the following fillings:")
    for filling in fillings:
        print(f"- {filling.title()}")

make_sandwich('white', 'salami', 'lettuce', 'tomato', 'onion')
make_sandwich('rye', 'beef', 'tomato')
make_sandwich('wholemeal', 'butter', 'chicken', 'spinach')