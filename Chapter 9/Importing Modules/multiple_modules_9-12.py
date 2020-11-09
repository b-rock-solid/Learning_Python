# Try It Yourself Exercise - Pg.180
# 9-12 Multiple Modules
########################################################################################################################
# Store the User class in one module and store the Privileges and Admin in another
# In a separate file, create an Admin instance and call show_privileges() to show it still works
########################################################################################################################

import user_priv

admin_user = user_priv.Admin('brock', 'solid', '30', 'male', 'blue')
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