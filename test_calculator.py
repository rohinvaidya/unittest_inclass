import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        # This method will run before each test case
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)


    def test_subtract(self):
        (self.calc.subtract(5, 2), 3)


    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)


    def test_divide(self):
        # self.assertEqual(self.calc.divide(6, 2), 3)

        # Test division by zero
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

    def test_divide_not_zero(self):
        self.assertEqual(self.calc.divide(6, 2), 3)

    def test_subtract_none(self):
        (self.calc.subtract(None, 2), None)

if __name__ == "__main__":
    unittest.main()