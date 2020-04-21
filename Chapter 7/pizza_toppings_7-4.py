# Try It Yourself Exercise - Pg.123
# 7-4 Pizza Toppings
########################################################################################################################
# Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value
# As they enter each topping, print a message saying the topping will be added to their pizza
########################################################################################################################

prompt = ("\nPlease enter the topping you wish to add to your pizza.")
prompt += ("\nEnter 'done' when you have finished entering your toppings. ")

active = True

while active:
    message = input(prompt)

    if message == 'done':
        active = False
    else:
        print(f"Thank you, we will add {message.title()} to your pizza!")