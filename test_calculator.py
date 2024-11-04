import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        # This method will run before each test case
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 3), 5)


    def test_subtract(self):
        # (self.calc.subtract(input1, input2), output)
        pass


    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)


    def test_divide(self):
        # (self.calc.divide(input1, input2), output)
        pass

        
        # Test division by zero
        with self.assertRaises(ValueError):
            self.calc.divide(10, 0)

if __name__ == "__main__":
    unittest.main()