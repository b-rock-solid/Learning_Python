########################################################################################################################
#                                          Importing Specific Functions                                                #
########################################################################################################################

# You can also import a specific function from a module. Below is the general syntax:
# from module_name import function_name

# You can import as many functions as you want by separating each function's name with a comma:
# from module_name import function_0, function_1, function_2

from pizza_module import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')