import unittest
import math

def custom_modf(x):
    # Calculate the integer part using math.floor()
    integer_part = math.floor(x)
    # Calculate the fractional part
    fractional_part = x - integer_part
    # Return a tuple containing both parts
    return (fractional_part, integer_part)

class TestModfFunction(unittest.TestCase):
    
    def test_modf_positive_number(self):
        self.assertEqual(custom_modf(5.25), (0.25, 5.0))

    def test_modf_negative_number(self):
        self.assertEqual(custom_modf(-3.75), (-0.75, -3.0))

    def test_modf_zero(self):
        self.assertEqual(custom_modf(0), (0.0, 0.0))
        
        if __name__ == '__main__':
            unittest.main()        