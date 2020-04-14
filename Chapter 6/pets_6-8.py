# Try It Yourself Exercise - Pg.112
# 6-8 Pets
########################################################################################################################
# Make several dictionaries, where each dictionary represents a different pet
# Each dictionary must include the kind of animal and the owner's name
# Store the dictionaries in a list called 'pets'
# Loop through your list and print everything you know about each pet
########################################################################################################################

bruno = {
    'name': 'bruno',
    'animal': 'german shepherd',
    'owner_first': 'brock',
    'owner_last': 'solid',
}
walter = {
    'name': 'walter',
    'animal': 'golden retriever',
    'owner_first': 'carl',
    'owner_last': 'guyson',
}
ringo = {
    'name': 'ringo',
    'animal': 'ringneck parrot',
    'owner_first': 'shauna',
    'owner_last': 'smithfield',
}

pets = [bruno, walter, ringo]

for pet in pets:
    print(f"\nPet name: {pet['name'].title()}")
    print(f"\tAnimal: {pet['animal'].title()}")
    print(f"\tOwner: {pet['owner_first'].title()} {pet['owner_last'].title()}")