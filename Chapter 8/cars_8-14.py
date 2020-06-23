# Try It Yourself Exercise - Pg.150
# 8-14 Cars
########################################################################################################################
# Write a function that stores information about a car in a dictionary
# The function should aways receive a manufacturer and a model name
# It should then accept an arbitrary number of keyword arguments
########################################################################################################################

def make_car(make, model, **car_info):
    """Build a dictionary with info on a car"""
    car_info['manufacturer'] = make
    car_info['model'] = model
    return car_info

car = make_car('subaru', 'outback',
               colour = 'blue',
               tow_package=True)

print(car)

car = make_car('ford', 'mustang',
               colour = 'space grey',
               year = 2017)

print(car)