import unittest
from my_program import Calculator  # Importing the Calculator class

class TestCalculator(unittest.TestCase):  # Defines a test case
    def test_add(self):  # The test method
        calc = Calculator()  # Create an instance of Calculator
        self.assertEqual(calc.add(1, 2), 3)  # Test for the add method
        self.assertEqual(calc.add(-1, 1), 0)  # Additional test
        self.assertEqual(calc.add(0, 0), 0)  # Additional test

if __name__ == '__main__':
    unittest.main()  # Run the tests



def test_integration():
    calc = Calculator()  # Create an instance of Calculator
    result = calc.add(3, 4)  # Combine overall operation
    assert result == 7  # Check the final outcome
