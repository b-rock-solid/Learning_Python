# Try It Yourself Exercise - Pg.181
# 9-14 Lottery
########################################################################################################################
# Make a list or tuple containing a series of 10 numbers and 5 letters.
# Randomly select four numbers or letters from the list
# Print a message saying that any ticket matching these four numbers or letters wins a prize
########################################################################################################################

from random import choice

lottery_numbers = [1, 21, 55, 13, 11, 7, 19, 28, 88, 10, 'A', 'Z', 'T', 'G', 'M']
winning_ticket = []

while len(winning_ticket) < 4:
    pulled_ticket = choice(lottery_numbers)
    if pulled_ticket not in winning_ticket:
        print(f"Ticket {pulled_ticket} has been pulled. Congratulations!")
        winning_ticket.append(pulled_ticket)
