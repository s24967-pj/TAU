import unittest
import calculator

class Tests(unittest.TestCase):
    def setUp(self):
        self.calculator = calculator.Calculator()

    def test_sum(self):
        self.assertEqual(self.calculator.sum(3, 5), 8)
        self.assertEqual(self.calculator.sum(-1, -1), -2)

    def test_difference(self):
        self.assertEqual(self.calculator.difference(5, 2), 3)

    def test_multiply(self):
        self.assertEqual(self.calculator.product(3, 5), 15)

    def test_division(self):
        self.assertEqual(self.calculator.quotient(4, 2), 2)

    def test_sum_with_strings(self):
        with self.assertRaises(TypeError):
            self.calculator.sum("x", 5)
        with self.assertRaises(TypeError):
            self.calculator.sum(5, "y")

    def test_quotient_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.quotient(2, 0)

    def test_negative_multiply(self):
        self.assertEqual(self.calculator.product(-1, -1), 1)
        self.assertEqual(self.calculator.product(-1, 1), -1)
    
    def test_convert(self):
        self.assertEqual(self.calculator.convert_operation(1), "+")

    def test_convert_wrong_operation(self):
        self.assertIsNone(self.calculator.convert_operation(5))
        

if __name__ == '__main__':
    unittest.main()