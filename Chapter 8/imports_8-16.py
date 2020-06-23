# Try It Yourself Exercise - Pg.155
# 8-16 Imports
########################################################################################################################
# Using a program you wrote that has one function in it, store that in a separate file.
# Import the function into your main program file using the different approaches
########################################################################################################################

import cars_function

car = cars_function.make_car('subaru', 'outback',
               colour = 'blue',
               tow_package=True)

print(car)



from cars_function import make_car

car = make_car('subaru', 'outback',
               colour = 'red',
               tow_package=False)

print(car)



from cars_function import make_car as mc

car = mc('subaru', 'outback',
               colour = 'purple',
               extras_package=True)

print(car)



import cars_function as cf

car = cf.make_car('subaru', 'outback',
               colour = 'black',
               extras_package=False)

print(car)



from cars_function import *

car = make_car('subaru', 'outback',
               colour = 'space grey',
               tow_package=True)

print(car)