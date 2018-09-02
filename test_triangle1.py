import unittest
import math
from triangle import classify_triangle

class test_cases(unittest.TestCase):
    def test_Triangle(self):
        self.assertEqual(classify_triangle(2,6,5),"Scalene triangle")
        self.assertEqual(classify_triangle(4,2,3),"Scalene triangle")
        self.assertEqual(classify_triangle(3,2,2),"Isoceles triangle")
        self.assertEqual(classify_triangle(78,78,55),"Isoceles triangle")
        self.assertEqual(classify_triangle(3,3,3),"Equilateral triangle")
        self.assertEqual(classify_triangle(23,23,23),"Equilateral triangle")
        self.assertEqual(classify_triangle(0,1,0), "InvalidInput")
        self.assertEqual(classify_triangle(1,-2,-2), "InvalidInput")
        self.assertEqual(classify_triangle(1,5,0), "InvalidInput")
        self.assertEqual(classify_triangle(1,40,9), "Not a Triangle")
        self.assertEqual(classify_triangle(78,2,3), "Not a Triangle")
        self.assertEqual(classify_triangle(1,1,98), "Not a Triangle")


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)