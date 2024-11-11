import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add1(self):
        self.assertEqual(self.calc.add(3, 4),7)

    def test_add2(self):
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_subtract1(self):
        self.assertEqual(self.calc.subtract(8, 6), 2)

    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(2, 12), -10)

    def test_multiply1(self):
        self.assertEqual(self.calc.multiply(3, 6), 18)

    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(8, 9), 72)

    def test_divide1(self):
        self.assertEqual(self.calc.divide(21, 7),3)

    def test_divide2(self):
        self.assertEqual(self.calc.divide(9, 2), 4)

    def test_modulo1(self):
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_modulo2(self):
        self.assertEqual(self.calc.modulo(9, 3), 0)

if __name__ == '__main__':
    unittest.main()