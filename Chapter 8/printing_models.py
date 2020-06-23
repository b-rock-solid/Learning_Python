########################################################################################################################
#                                         Modifying a List in a Function                                               #
########################################################################################################################

## Example of code prior to adding functions ##

## Start with some designs that need to be printed ##
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []

## Simulate printing each design, until none are left ##
## Move each design to completed_models after printing ##
# while unprinted_designs:
#     current_design = unprinted_designs.pop()
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)

## Display all completed models ##
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#     print(completed_model)


## Code using functions for the same job

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until none are left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing model: {current_design}")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# If you wanted to leave the original list in tact, you can pass a copy of the list to the function
# This way, the original list won't be touched
# Keep in mind, that you would try and work with original lists where possible as it's more efficient
# However, if there's a reason to keep a list from being altered, you can
# To achieve this, you can call the function 'print_models' as below
########################################################################################################################
# print_models(unprinted_designs[:], completed_models)                                                                 #
########################################################################################################################