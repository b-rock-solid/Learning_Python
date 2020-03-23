# Try It Yourself Exercise - Pg.89
# 5-8 Hello Admin
########################################################################################################################
# Make a list of five or more usernames, including the name 'admin'
# Loop through the list and print a greeting to each user
# If the user is 'admin' print a special greeting
# Otherwise print a generic greeting
########################################################################################################################

users = ['admin', 'brock', 'carl', 'emily', 'ainslee', 'dave', 'shreya']

for user in users:
    if user == 'admin':
        print(f"Welcome back {user.title()}, would you like to see the latest status report?")
    else:
        print(f"Hello {user.title()}, thank you for logging in again")