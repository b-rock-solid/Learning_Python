########################################################################################################################
#                                                 Keyword Arguments                                                   #
########################################################################################################################

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# You can directly associate the name and the value within the argument
# This way there is no confusion and it doesn't matter what order they're in
describe_pet(animal_type='hamster', pet_name='harry')