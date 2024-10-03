# "I pledge my Honor that I have abided by the Stevens Honor System." - Maximo Ruiz

import unittest
from hw01 import classify_triangle

class TestTriangle(unittest.TestCase):
    
    def testNegative(self):
        a = -1
        b = 2
        c = 3
        self.assertEqual(classify_triangle(a, b, c), "Failed: All sides must be positive lengths!")
        
    def testZero(self):
        a = 0
        b = 4
        c = 5
        self.assertEqual(classify_triangle(a, b, c), "Failed: All sides must be positive lengths!")

    def testInequality(self):
        a = 1
        b = 2
        c = 3
        self.assertEqual(classify_triangle(a, b, c), "Failed: The sum of any two sides needs to be greater than the third (triangle inequality theorem)!")
        
    def testInequality2(self):
        a = 2
        b = 3
        c = 6
        self.assertEqual(classify_triangle(a, b, c), "Failed: The sum of any two sides needs to be greater than the third (triangle inequality theorem)!")

    def testNonInteger(self):
        a = 2
        b = 3
        c = 'a'
        self.assertEqual(classify_triangle(a, b, c), "Failed: All sides must be numeric values!")

    def testNonInteger2(self):
        a = 2
        b = "test"
        c = 6
        self.assertEqual(classify_triangle(a, b, c), "Failed: All sides must be numeric values!")

    def testEquilateral(self):
        a = 3
        b = 3
        c = 3
        self.assertEqual(classify_triangle(a, b, c), "Passed: This triangle is an equilateral triangle!")

    def testEquilateral2(self):
        a = 5
        b = 5
        c = 5
        self.assertEqual(classify_triangle(a, b, c), "Passed: This triangle is an equilateral triangle!")

    def testRightIsosceles(self):
        a = 3
        b = 3
        c = 3 * (2**0.5)
        self.assertEqual(classify_triangle(a, b, c), "Passed: This triangle is a right isosceles triangle!")

    def testRightIsosceles2(self):
        a = 1
        b = 1
        c = (2**0.5)
        self.assertEqual(classify_triangle(a, b, c), "Passed: This triangle is a right isosceles triangle!")

    def testRightScalene(self):
        a = 3
        b = 4
        c = 5
        self.assertEqual(classify_triangle(a, b, c), "Passed: This triangle is a right scalene triangle!")

    def testRightScalene2(self):
        a = 5
        b = 12
        c = 13
        self.assertEqual(classify_triangle(a, b, c), "Passed: This triangle is a right scalene triangle!")

    def testIsosceles(self):
        a = 3
        b = 3
        c = 5
        self.assertEqual(classify_triangle(a, b, c), "Passed: This triangle is an isosceles triangle!")

    def testIsosceles2(self):
        a = 2
        b = 5
        c = 5
        self.assertEqual(classify_triangle(a, b, c), "Passed: This triangle is an isosceles triangle!")

    def testScalene(self):
        a = 3
        b = 4
        c = 6
        self.assertEqual(classify_triangle(a, b, c), "Passed: This triangle is a scalene triangle!")

    def testScalene2(self):
        a = 5
        b = 6
        c = 7
        self.assertEqual(classify_triangle(a, b, c), "Passed: This triangle is a scalene triangle!")

if __name__ == '__main__':
    unittest.main()