# Try It Yourself Exercise - Pg.167
# 9-5 Login Attempts
########################################################################################################################
# Start with your program from 9-3
# Add an attribute called login_attempts to your User class
# Write a method called increment_login_attempts() that increments the value of login_attempts by 1
# Write another method called reset_login_attempts() that resets the value of login_attempts to 0
########################################################################################################################

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

user01 = User('Jimmy', 'Smith', '25', 'Male', 'Red')
user02 = User('Sara', 'Cummins', '18', 'Female', 'Pink')
user03 = User('Kyle', 'Sans', '40', 'Male', 'Black')
user04 = User('Karen', 'Manager', '45', 'Female', 'Green')

print(f"{user01.first_name} currently has {user01.login_attempts} login attempts")
user01.increment_login_attempts()
user01.increment_login_attempts()
print(f"\n{user01.first_name} now has {user01.login_attempts} login attempts")
user01.reset_login_attempts()
print(f"\nAfter resetting {user01.first_name}'s login attempts. "
      f"{user01.first_name} now has {user01.login_attempts} login attempts")