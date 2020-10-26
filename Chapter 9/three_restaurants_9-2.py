# Try It Yourself Exercise - Pg.162
# 9-2 Three Restaurants
########################################################################################################################
# Start with your class from 9-1
# Create 3 different instances from the class
# call describe_restaurant() for each instance
########################################################################################################################

class Restaurant:
    """A simple attempt at representing a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type of a restaurant"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Indicates the restaurants name and cuisine type"""
        print(f"\n{self.restaurant_name} primarily cooks {self.cuisine_type} food.")

    def open_restaurant(self):
        """Simulates opening the restaurant"""
        print(f"{self.restaurant_name} is now open for orders!")

restaurant01 = Restaurant('Spicy Noodle House', 'Asian')
restaurant02 = Restaurant('Yummy Yum Cha', 'Chinese')
restaurant03 = Restaurant('Sticky Rib Joint', 'American BBQ')

restaurant01.describe_restaurant()
restaurant02.describe_restaurant()
restaurant03.describe_restaurant()

