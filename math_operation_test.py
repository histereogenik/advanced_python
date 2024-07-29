import unittest

from math_operations import addition_operation, subtraction_operation

class TestMathOperations(unittest.TestCase):
    def test_addition_operation(self):
        math_addition_result = addition_operation(5, 10)
        self.assertEqual(math_addition_result, 15)

    def test_subtraction_operation(self):
        math_subtraction_result = subtraction_operation(10, 10)
        self.assertEqual(math_subtraction_result, 0)

if __name__ == '__main__':
    unittest.main()