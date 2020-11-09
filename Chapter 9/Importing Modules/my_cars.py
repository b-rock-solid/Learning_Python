from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())
########################################################################################################################
#                                          Importing an Entire Module                                                  #
########################################################################################################################
# import car

# my_beetle = car.Car('volkswagen', 'beetle', 1995)
# print(my_beetle.get_descriptive_name())

# my_tesla = car.ElectricCar('tesla', 'roadster', 2021)
# print(my_tesla.get_descriptive_name())

# You can import every class from a module using the following syntax
# from module_name import *

########################################################################################################################
#                                                 Using Aliases                                                        #
########################################################################################################################

# from electric_car import ElectricCar as EC
# my_tesla = EC('tesla', 'roadster', 2019)