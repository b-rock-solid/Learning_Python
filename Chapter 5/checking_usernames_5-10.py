# Try It Yourself Exercise - Pg.89
# 5-10 Checking Usernames
########################################################################################################################
# Make a list of 5 or more usernames called current_users
# Make another list of 5 called new_users
# Make sure 1 or 2 items are also in current_users
# Loop through new_users and see if the username already exists
# If it has, print a message that the person will need to enter a new username
# Otherwise print a message saying the username is available
# Ensure the comparison is case sensitive. Ie. 'John' is used 'JOHN' can't be accepted
# To do this, make a copy of current_current users containing all lowercase versions
########################################################################################################################

current_users = ['brock', 'carl', 'Ainslee', 'Dave', 'BrUno', 'LEIA']
new_users = ['Emily', 'Shreya', 'ainslEE', 'dAvE', 'john']
user_check = []

for c_user in current_users:
    user_check.append(c_user.lower())

for user in new_users:
    if user.lower() in user_check:
        print(f"Sorry, the username '{user}' is unavailable, please choose another")
    else:
        print(f"The username '{user}' is available!")