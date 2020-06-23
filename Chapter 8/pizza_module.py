########################################################################################################################
#                                      Importing an Entire Module - Module                                             #
########################################################################################################################

# Sometimes you won't know ahead of time how many arguments a function needs to accept
# For example, a function that builds a pizza

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")