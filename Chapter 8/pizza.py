########################################################################################################################
#                                  Passing an Arbitrary Number of Arguments                                            #
########################################################################################################################

# Sometimes you won't know ahead of time how many arguments a function needs to accept
# For example, a function that builds a pizza

def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

########################################################################################################################
#                                   Mixing Positional and Arbitrary Arguments                                          #
########################################################################################################################

# If you want to accept several different kinds of arguments, the parameter that accepts an arbitrary number of
#   arguments must be placed last in the function definition
# For example, if the function needs to take in a size for the pizza

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")


make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')