########################################################################################################################
#                                                   Default Values                                                     #
########################################################################################################################

# You can define a default value for each parameter within the function
# If no argument for a parameter is passed to Python, it will use the default argument value
# In this example, we have defined a default value of 'dog' to animal_type

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# You can directly associate the name and the value within the argument
# This way there is no confusion and it doesn't matter what order they're in
describe_pet(pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

########################################################################################################################
#                                                        NOTE                                                          #
# When you use default values, any parameter with a default value needs to be listed after all the parameters
# that don't have default values. This allows Python to continue interpreting positional arguments correctly.
########################################################################################################################