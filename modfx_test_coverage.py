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

    # Handling special floating-point values
    if math.isinf(x) or math.isnan(x):
        return x, 0

    integer_part = math.floor(x)
    fractional_part = x - integer_part

    # Precision handling
    fractional_part = round(fractional_part, 10)

    return fractional_part, integer_part


class TestModfFunction(unittest.TestCase):
    """
    A test case for the custom_modf function.
    """

    # Existing test methods...

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
        self.assertTrue(nan_result[1] == 0)


if __name__ == '__main__':
    unittest.main()
