# Try It Yourself Exercise - Pg.193
# 10-4 Guest Book
########################################################################################################################
# Write a while loop that prompts users for their name.
# When they enter their name, print a greeting to the screen and add a line recording their visit.
# Record their visit to a file called guest_book.txt
# Make sure each entry appears on a new line in the file.
########################################################################################################################

filename = 'guest_book.txt'

while True:
    guest = input("Please enter your name (Type 'exit' to quit): ")
    if guest == 'exit':
        break
    else:
        with open (filename, 'a') as file_object:
            print(f"Thank you {guest} for attending the party :)")
            file_object.write(f"{guest}\n")