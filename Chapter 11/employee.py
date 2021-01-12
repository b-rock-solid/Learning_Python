# Try It Yourself Exercise - Pg.221
# 11-3 Employee
########################################################################################################################
# Write a class called Employee. The __init__() method should take a first name, last name and an annual salary.
# Store each of these as attributes.
# Write a method called give_raise() that adds $5,000 to the annual salary by default.
# Also allow it to accept a different raise amount.
# Write a test case for Employee. Write two test methods:
# test_give_default_raise() & test_give_custom_raise().
# Use the setUp() method so you don't have to create a new employee instance in each test method.
########################################################################################################################

class Employee:
    """Create a base interpretation of an employee."""

    def __init__(self, first_name, last_name, salary):
        """Initialise employee details."""
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def give_raise(self, salary_raise=5000):
        """Gives a raise to the employee."""
        self.salary += salary_raise


me = Employee('Brock', 'Allen', 70000)
print(me.salary)
me.give_raise(10000)
print(me.salary)