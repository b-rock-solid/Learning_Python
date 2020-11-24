# Try It Yourself Exercise - Pg.181
# 9-15 Lottery Analysis
########################################################################################################################
# You can use a loop to see how hard it might be to win the kind of lottery you just modeled.
# Make a list or tuple called my_ticket
# Write a loop that keeps pulling numbers until your ticket wins.
# Print a message reporting how many times the loop had to run to give you a winning ticket.
########################################################################################################################

from random import choice

lottery_numbers = [1, 21, 55, 13, 11, 7, 19, 28, 88, 10, 'A', 'Z', 'T', 'G', 'M']
winning_ticket = []
my_ticket = 21

while my_ticket not in winning_ticket:
    pulled_ticket = choice(lottery_numbers)
    if pulled_ticket not in winning_ticket:
        print(f"Ticket {pulled_ticket} has been pulled. Congratulations!")
        winning_ticket.append(pulled_ticket)

draw_count = len(winning_ticket)
print(f"\nIt took {draw_count} draws to pull your ticket.")