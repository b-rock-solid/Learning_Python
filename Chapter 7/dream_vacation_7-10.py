# Try It Yourself Exercise - Pg.127
# 7-10 Dream Vacation
########################################################################################################################
# Write a program that polls users about their dream vacation
# Include a block of code that prints the results of the poll
########################################################################################################################

responses = {}

polling_active = True

while polling_active:
    name = input("What is your name? ")
    response = input("If you could visit one place in the world, where would you go? ")

    responses[name] = response

    repeat = input("Is anybody else completing this poll (yes / no): ")
    if repeat == 'no':
        polling_active = False

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would love to visit {response.title()}.")