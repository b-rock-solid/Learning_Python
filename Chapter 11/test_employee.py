import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """Tests for the class 'Employee'."""

    def setUp(self):
        """Create an employee and it's associated data."""
        self.bibbity = Employee('Bibbity', 'Bobbity', 60000)

    def test_give_default_raise(self):
        """Tests giving an employee the default raise amount."""
        self.bibbity.give_raise()
        self.assertEqual(self.bibbity.salary, 65000)

    def test_give_custom_raise(self):
        """Tests giving an employee a custom raise amount."""
        self.bibbity.give_raise(10000)
        self.assertEqual(self.bibbity.salary, 70000)

if __name__ == '__main__':
    unittest.main()