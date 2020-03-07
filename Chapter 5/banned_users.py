# Checking Whether a value is not in a list

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(f"{user.title()}, you can post a response if you wish.")

# NOTE: Throughout programming you'll hear the term 'Boolean expression'
# A Boolean expression is another name for a conditional test
# A 'Boolean value' is either 'True' or 'False'
# Boolean values are often used to keep track of certain conditions, such as whether a game is running
# or whether a user can edit a certain content on a website:
# game_active = True
# can_edit = False