import unittest
from calculator import add, substract, multiply, divide

class TestCalc(unittest.TestCase):

    # test function should always start with "test"
    def test_add(self):
        self.assertEqual(add(5,10), 15)

        # Check some edge cases
        self.assertEqual(add(-2,2), 0)
        self.assertEqual(add(-1,-5), -6)


    def test_substract(self):
        self.assertEqual(substract(5,-10), 15)
        self.assertEqual(substract(-2,-2), 0)
        self.assertEqual(substract(1,5), -4)


    def test_multiply(self):
        self.assertEqual(multiply(5,-9.0), -45)
        self.assertEqual(multiply(-2,0), 0)
        self.assertEqual(multiply(-10,-5), 50)


    def test_divide(self):
        self.assertEqual(divide(5,2), 2.5)
        # To check if raises value error if 0 is the second argument
        self.assertRaises(ValueError, divide, 10, 0)
        # Context Manager way of doing
        # with self.assertRaises(ValueError):
        #     divide(10,0)



# To run this file from terminal: python -m unittest tests.calc.py
if __name__=="__main__":
    unittest.main()