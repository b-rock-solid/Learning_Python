########################################################################################################################
#                                      Using as to Give a Function an Alias                                            #
########################################################################################################################

# If the name of a function you're importing might conflict with an existing name in your program,
# or if the function name is long, you can use a short, unique alias
# The general syntax for providing an alias is:
# from module_name import function_name as fn

# Here we give the function make_pizza() an alias, mp(), by importing make_pizza as mp.

from pizza_module import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')


########################################################################################################################
#                                       Using as to Give a Module an Alias                                             #
########################################################################################################################

# You can also provide an alias for a module name
# General syntax for this approach is:
# import module_name as mn

import pizza_module as p

p.make_pizza(15, 'pepperoni')
p.make_pizza(10, 'mushrooms', 'green peppers')


########################################################################################################################
#                                      Importing All Functions in a Module                                             #
########################################################################################################################

# You can tell Python to import every function in a module by using the asterisk (*) operator:
# from module_name import *

from pizza_module import *

make_pizza(5, 'meatlovers')
make_pizza(4, 'vegetarian')