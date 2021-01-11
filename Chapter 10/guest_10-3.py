# Try It Yourself Exercise - Pg.193
# 10-3 Guest
########################################################################################################################
# Write a program that prompts the user for their name.
# When they respond, write their name to a file called guest.txt
########################################################################################################################

guest = input("Please enter your name: ")

filename = 'guest.txt'

with open (filename, 'w') as file_object:
    file_object.write(guest)