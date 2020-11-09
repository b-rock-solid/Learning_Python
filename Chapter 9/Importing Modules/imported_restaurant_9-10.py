# Try It Yourself Exercise - Pg.180
# 9-10 Imported Restaurant
########################################################################################################################
# Using your latest Restaurant class, store it in a module
# Make a separate file that imports Restaurant
# Make an instance and call one of the methods to show the import working
########################################################################################################################

from restaurant import Restaurant

my_restaurant = Restaurant('bobs burgers', 'gourmet burger bar')
my_restaurant.describe_restaurant()