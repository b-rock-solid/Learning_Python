"""Stores the Admin and Privileges class for users."""

from user_user import User

class Admin(User):
    """Creating an Admin Profile"""
    def __init__(self, first_name, last_name, age, gender, favourite_colour):
        super().__init__(first_name, last_name, age, gender, favourite_colour)
        # Initialize an empty set of privileges.
        self.privileges = Privileges()


class Privileges:
    """Stores the sets of admin privileges."""

    def __init__(self, privileges=[]):
        self.privileges = privileges


    def show_privileges(self):
        print(f"The user currently has the following privileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("- This user has no privileges.")
