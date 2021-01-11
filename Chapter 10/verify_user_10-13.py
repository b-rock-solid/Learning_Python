# Try It Yourself Exercise - Pg.208
# 10-13
########################################################################################################################
# Before printing a welcome back message in greet_user(), ask the user if this is the correct username.
# If it's not, call get_new_username() to get the correct username.
########################################################################################################################

import json

def get_stored_username():
    """Get stored username if available."""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def verify_user():
    """Verify the user stored is the current user."""
    username = get_stored_username()
    verify = input(f"Is this you {username} (y/n)? ")
    if verify == 'y':
        return None
    else:
        get_new_username()

def greet_user():
    """Greet the user by name."""
    verify_user()
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back. {username}!")

greet_user()
