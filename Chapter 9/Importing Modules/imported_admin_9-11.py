# Try It Yourself Exercise - Pg.180
# 9-11 Imported Admin
########################################################################################################################
# Using your code from exercise 9-8
# Store the classes User, Privileges and Admin in one module
# Create a separate file, make an Admin instance and call show_privileges() to show it working
########################################################################################################################

import user

admin_user = user.Admin('brock', 'solid', '30', 'male', 'blue')
admin_user.describe_user()

# Make a list of privileges to add to the admin user
admin_user_privileges = ['can add post',
                    'can delete post',
                    'can ban user'
                    ]

# Add privileges to the user
admin_user.privileges.privileges = admin_user_privileges

# Show privileges
admin_user.privileges.show_privileges()
