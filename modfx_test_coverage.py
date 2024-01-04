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
    # Calculate the integer part using math.floor()
    integer_part = math.floor(x)
    # Calculate the fractional part
    fractional_part = x - integer_part
    # Return a tuple containing both parts
    return (fractional_part, integer_part)

class TestModfFunction(unittest.TestCase):
    """
    A test case for the custom_modf function.
    """
    
    def test_modf_positive_number(self):
        """
        Test custom_modf with a positive number.
        """
        self.assertEqual(custom_modf(5.25), (0.25, 5.0))

    def test_modf_negative_number(self):
        """
        Test custom_modf with a negative number.
        """
        self.assertEqual(custom_modf(-3.75), (-0.75, -3.0))

    def test_modf_zero(self):
        """
        Test custom_modf with zero.
        """
        self.assertEqual(custom_modf(0), (0.0, 0.0))

if __name__ == '__main__':
    unittest.main()
