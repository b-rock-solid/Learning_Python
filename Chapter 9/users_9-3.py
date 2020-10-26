# Try It Yourself Exercise - Pg.162
# 9-3 Users
########################################################################################################################
# Make a class called User
# Create two attributes called first_name and last_name
# Create several other attributes that are typically stored in a user profile
# Make a method called describe_user() that prints a summary of the user's information
# Make another method called greet_user() that prints a personalized greeting to the user
# Create several instances representing different users and call both methods for each user
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

user01 = User('Jimmy', 'Smith', '25', 'Male', 'Red')
user02 = User('Sara', 'Cummins', '18', 'Female', 'Pink')
user03 = User('Kyle', 'Sans', '40', 'Male', 'Black')
user04 = User('Karen', 'Manager', '45', 'Female', 'Green')

user01.greet_user()
user01.describe_user()
user02.greet_user()
user02.describe_user()
user03.greet_user()
user03.describe_user()
user04.greet_user()
user04.describe_user()