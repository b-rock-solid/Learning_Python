# Try It Yourself Exercise - Pg.208
# 10-12
########################################################################################################################
# Combine the two programs from 10-11 into one.
# If the number is already stored, report the favourite number.
# If not, prompt the user and store it in a file.
########################################################################################################################

import json

def get_stored_number():
    """Gets stored favourite number if available."""
    filename = 'fav_num10-12.json'
    try:
        with open(filename) as f:
            fav_number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return fav_number

def get_new_number():
    """Prompt the user for their favourite number."""
    while True:
        try:
            fav_number = float(input("What's your favourite number? "))
        except ValueError:
            print("Please enter a number.")
        else:
            filename = 'fav_num10-12.json'
            with open(filename, 'w') as f:
                json.dump(fav_number, f)
            return fav_number

def favourite_number():
    """Tell the user their favourite number."""
    fav_number = get_stored_number()
    if fav_number:
        print(f"I know your favourite number! It's {fav_number}!")
    else:
        fav_number = get_new_number()
        print(f"We'll remember your favourite number {fav_number} for next time.")

favourite_number()