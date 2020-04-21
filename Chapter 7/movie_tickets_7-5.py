# Try It Yourself Exercise - Pg.123
# 7-5 Movie Tickets
########################################################################################################################
# A movie theatre charges different ticket prices depending on a person's age
# Write a loop, asking for the person's age
# Tell the user the price of their ticket depending on their age
# Under age 3 = free
# Ages 3 - 12 = $10
# Ages 13 up = $15
########################################################################################################################

age = input("Please enter your age to obtain your ticket: ")
age = int(age)

if age < 3:
    ticket_price = 0
elif age < 13:
    ticket_price = 10
else:
    ticket_price = 15

print(f"The price of your ticket is ${ticket_price}.")