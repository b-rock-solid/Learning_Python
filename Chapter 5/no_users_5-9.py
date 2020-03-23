# Try It Yourself Exercise - Pg.89
# 5-9 No Users
########################################################################################################################
# Add an if test to the previous hello_admin.py to check the list is not empty
# If the list is empty, print, "We need to find some users!"
# Remove all users from the list and check the program
########################################################################################################################

users = []

if users:
    for user in users:
        if user == 'admin':
            print(f"Welcome back {user.title()}, would you like to see the latest status report?")
        else:
            print(f"Hello {user.title()}, thank you for logging in again")
else:
    print("We need to find some users!")