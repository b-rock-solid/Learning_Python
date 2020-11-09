# Try It Yourself Exercise - Pg.173
# 9-6 Ice Cream Stand
########################################################################################################################
# Write a class called IceCreamStand that inherits from the Restaurant class from 9-4
# Add an attribute called flavours that stores a list of ice cream flavours
# Write a method that displays these flavours.
# Create an instance of IceCreamStand, and call this method
########################################################################################################################
class Restaurant:
    """A simple attempt at representing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type of a restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Indicates the restaurants name and cuisine type"""
        print(f"{self.restaurant_name} primarily cooks {self.cuisine_type} food.")

    def open_restaurant(self):
        """Simulates opening the restaurant"""
        print(f"{self.restaurant_name} is now open for orders!")

    def set_number_served(self, customer_number):
        """Sets the number of customers served"""
        self.number_served = customer_number

    def increment_number_served(self, increment_number):
        """Increments the number of customers served"""
        self.number_served += increment_number

class IceCreamStand(Restaurant):
    """Represents aspects of a restaurant, specific to an Ice Cream Stand."""

    def __init__(self, restaurant_name, cuisine_type):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavours = ['chocolate', 'strawberry', 'vanilla', 'raspberry']

    def show_flavours(self):
        """Print a statement showing the flavours available."""
        print(f"The flavours currently available are:\n{self.flavours}")


my_icecreamstand = IceCreamStand('IcyCreamz', 'Dessert')

my_icecreamstand.describe_restaurant()
my_icecreamstand.show_flavours()