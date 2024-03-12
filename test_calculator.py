
from calc import Calculator
import unittest


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(4, 7), 11)

    def test_subtract(self):
        self.assertEqual(self.calculator.subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(self.calculator.multiply(3, 3), 9)

    def test_divide(self):
        self.assertEqual(self.calculator.divide(4, 2), 2)
