import unittest
from sources.calculator import add, substract, multiply

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(5,10), 15)
        self.assertEqual(add(-2,2), 0)
        self.assertEqual(add(-1,-5), -6)
        self.assertEqual(add("a",-5), "a-5.0")


    def test_substract(self):
        self.assertEqual(substract(5,-10), 15)
        self.assertEqual(substract(-2,-2), 0)
        self.assertEqual(substract(1,5), -4)
        with self.assertRaises(TypeError):
            substract("a",5)


    def test_multiply(self):
        self.assertEqual(multiply(5,-9.0), -45)
        self.assertEqual(multiply(-2,0), 0)
        self.assertRaises(TypeError, multiply, "a", 6)
        self.assertRaises(TypeError, multiply, "a", "o")



# To run this file from terminal: python -m unittest tests.calc.py
if __name__=="__main__":
    unittest.main()
