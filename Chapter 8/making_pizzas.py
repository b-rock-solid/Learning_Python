########################################################################################################################
#                                           Importing an Entire Module                                                 #
########################################################################################################################

# Simply writing import fowllowed by the name of the module, makes every function from the module available
# If you use this kind of import statement, each function in the module is available through the following syntax:
# module_name.function_name()

import pizza_module

pizza_module.make_pizza(16, 'pepperoni')
pizza_module.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')