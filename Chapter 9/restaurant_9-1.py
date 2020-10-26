# Try It Yourself Exercise - Pg.162
# 9-1 Restaurant
########################################################################################################################
# Make a class called Restaurant
# Restaurant should store two attributes 'restaurant_name' and 'cuisine_type'
# Make a method called describe_restaurant() that prints these two pieces of information
# Make a method called open_restaurant() that prints a message indicating the restaurant is open
# Make an instance called restaurant from your class. Print the two attributes individually
# Call both methods
########################################################################################################################

class Restaurant:
    """A simple attempt at representing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type of a restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Indicates the restaurants name and cuisine type"""
        print(f"{self.restaurant_name} primarily cooks {self.cuisine_type} food.")

    def open_restaurant(self):
        """Simulates opening the restaurant"""
        print(f"{self.restaurant_name} is now open for orders!")

restaurant = Restaurant('Spicy Noodle House', 'Asian')

print(f"The new restaurant {restaurant.restaurant_name} is opening soon.")
print(f"It will specialise primarily in {restaurant.cuisine_type} type foods.")

restaurant.describe_restaurant()
restaurant.open_restaurant()

