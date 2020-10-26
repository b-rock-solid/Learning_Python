# Try It Yourself Exercise - Pg.167
# 9-4 Number Served
########################################################################################################################
# Start with program fro 9-1
# Add an attribute called number_served with a default value of 0
# Create an instance called restaurant from this class
# Print the number of customers served, change this value and print it again
# Add a method called set_number_served() that lets you set the number of customers that have been served
# Call this method and print the value again
# Add a method called increment_number_served() that lets you increment the number served
# Call this method with a number that could represent how many customers were served in a day
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

restaurant = Restaurant('Spicy Noodle House', 'Asian')

print(f"The new restaurant {restaurant.restaurant_name} is opening soon.")
print(f"It will specialise primarily in {restaurant.cuisine_type} type foods.")

restaurant.describe_restaurant()
restaurant.open_restaurant()

print(f"\nThe current number of customers served is {restaurant.number_served}")
restaurant.number_served = 5
print(f"The number of customers served now is {restaurant.number_served}")

restaurant.set_number_served(8)
print(f"\nThe new number of customers served now is {restaurant.number_served}")

restaurant.increment_number_served(80)
print(f"\nThe total number of customers served is {restaurant.number_served}")