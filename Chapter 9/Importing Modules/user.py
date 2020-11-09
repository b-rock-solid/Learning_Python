"""Stores classes related to a user."""

class User:
    """Creating user profile"""

    def __init__(self, first_name, last_name, age, gender, favourite_colour):
        """Initialize a user's profile details"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        self.favourite_colour = favourite_colour
        self.login_attempts = 0

    def describe_user(self):
        """Prints a summary of the user's profile"""
        print(f"The following information is what we currently have on your account:"
              f"\nName: {self.first_name} {self.last_name}"
              f"\nAge: {self.age}"
              f"\nGender: {self.gender}"
              f"\nFavourite Colour: {self.favourite_colour}")

    def greet_user(self):
        """Prints a personalized greeting to the user"""
        print(f"\nWelcome back {self.first_name}!")

    def increment_login_attempts(self):
        """Increments the login attempt number by 1"""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Resets the login attempts number back to 0"""
        self.login_attempts = 0


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