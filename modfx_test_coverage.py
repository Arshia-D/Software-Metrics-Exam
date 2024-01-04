import unittest
import math


def custom_modf(x):
    """
    Calculate the integer and fractional parts of a number.

    Args:
        x (float): The input number.

    Returns:
        tuple: A tuple containing the fractional and integer parts.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be a numeric value")

    integer_part = math.floor(x)
    fractional_part = x - integer_part

    # Precision handling (adjust precision as needed)
    fractional_part = round(fractional_part, 10)  

    return fractional_part, integer_part


class TestModfFunction(unittest.TestCase):
    """
    A test case for the custom_modf function.
    """

    def test_modf_positive_number(self):
        """
        Test custom_modf with a positive number.
        """
        self.assertEqual(custom_modf(5.25), (0.25, 5))

    def test_modf_negative_number(self):
        """
        Test custom_modf with a negative number.
        """
        self.assertEqual(custom_modf(-3.75), (-0.75, -3))

    def test_modf_zero(self):
        """
        Test custom_modf with zero.
        """
        self.assertEqual(custom_modf(0), (0.0, 0))

    def test_modf_large_number(self):
        """
        Test custom_modf with a large number.
        """
        self.assertEqual(custom_modf(123456789.123456789), (0.1234567891, 123456789))

    def test_modf_small_number(self):
        """
        Test custom_modf with a small number.
        """
        self.assertEqual(custom_modf(0.000000123456789), (0.0000001235, 0))

    def test_modf_non_numeric_input(self):
        """
        Test custom_modf with a non-numeric input.
        """
        with self.assertRaises(TypeError):
            custom_modf("not a number")

    def test_input_unchanged(self):
        """
        Test to ensure the input value remains unchanged after the function call.
        """
        x = 5.25
        custom_modf(x)
        self.assertEqual(x, 5.25)  # Ensure x is unchanged
        
def test_modf_with_integer(self):
        """
        Test custom_modf with an integer.
        """
        self.assertEqual(custom_modf(10), (0.0, 10))
        
def test_modf_with_float_max(self):
        """
        Test custom_modf with the maximum float value.
        """
        self.assertEqual(custom_modf(float('inf')), (float('inf'), 0))
                        
def test_modf_with_float_min(self):
        """
        Test custom_modf with the minimum float value (negative infinity).
        """
        self.assertEqual(custom_modf(float('-inf')), (float('-inf'), 0))
        
def test_modf_with_nan(self):
        """
        Test custom_modf with NaN (Not a Number).
        """
        nan_result = custom_modf(float('nan'))
        self.assertTrue(math.isnan(nan_result[0]))
        self.assertTrue(math.isnan(nan_result[1]))
        
if __name__ == '__main__':
    unittest.main()
