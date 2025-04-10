# https://github.com/Ife-A/lab10-IA-AU
# Partner 1: Ifeanyichukwu Alutu
# Partner 2: Ayan Uzzaman

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    def test_add(self): # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 5), 5)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(5, 2), 3)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(3, 3), 0)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(3,4), 12)
        self.assertAlmostEqual(mul(3.01,4), 12.04)
        self.assertEqual(mul(-2,4), -8)


    def test_divide(self): # 3 assertions
        self.assertEqual(div(3,12),4)
        self.assertEqual(div(3,-12), -4)
        self.assertAlmostEqual(div(3,363), 121)
    # ##########################


    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)
    #     fill in code

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(10, 100), 2.0)
        self.assertAlmostEqual(logarithm(2, 8), 3.0)
        self.assertAlmostEqual(logarithm(5, 25), 5.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(-2, 8)

    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        with self.assertRaises(ValueError):
            logarithm(0, 5)

    def test_hypotenuse(self): # 3 assertions
        self.assertAlmostEqual(hypotenuse(3,4), 5)
        self.assertAlmostEqual(hypotenuse(0,5), 5)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5)

    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
        with self.assertRaises(ValueError):
            square_root(-9)
    #     # Test basic function
        self.assertAlmostEqual(square_root(16),4)
        self.assertAlmostEqual(square_root(0),0)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()