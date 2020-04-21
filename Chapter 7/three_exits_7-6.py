# Try It Yourself Exercise - Pg.123
# 7-6 Three Exits
########################################################################################################################
# Write different versions of either exercise 7-4 / 7-5 that do each of the following at least once
# Use a conditional test in the while statement to stop the loop
# Use an active variable to control how long the loop runs
# Use a break statement to exit the loop when the user enters a 'quit' value
########################################################################################################################

# This program uses both a conditional test and the active variable to stop the loop
prompt = ("\nPlease enter the topping you wish to add to your pizza.")
prompt += ("\nEnter 'done' when you have finished entering your toppings. ")

active = True
while active:
    message = input(prompt)

    if message == 'done':
        active = False
    else:
        print(f"Thank you, we will add {message.title()} to your pizza!")


# This program uses the break statement to exit the loop
prompt = ("\nPlease enter the topping you wish to add to your pizza.")
prompt += ("\nEnter 'break' when you have finished entering your toppings. ")

while True:
    message = input(prompt)

    if message == 'break':
        break
    else:
        print(f"Thank you, we will add {message.title()} to your pizza!")