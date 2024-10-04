# -*- coding: utf-8 -*-
"""
Updated Oct 3, 2024

@author: mr
"""

"""
Below features all of the test cases I've used for this assignment.
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(5, 12, 13), 'Right', '5,12,13 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(8, 15, 17), 'Right', '8,15,17 is a Right triangle')
            
    def testEquilateralTrianglesA(self): 
        self.assertEqual(classifyTriangle(3, 3, 3), 'Equilateral', '3,3,3 should be Equilateral')

    def testEquilateralTrianglesB(self): 
        self.assertEqual(classifyTriangle(4, 4, 4), 'Equilateral', '4,4,4 should be Equilateral')

    def testZeros(self): 
        self.assertEqual(classifyTriangle(0, 0, 1), 'InvalidInput', '0,0,1 should be invalid input')

    def testNegative(self): 
        self.assertEqual(classifyTriangle(-1, 1, 1), 'InvalidInput', '-1,1,1 should be invalid input')

    def test200(self): 
        self.assertEqual(classifyTriangle(200, 200, 1), 'InvalidInput', '200,200,1 should be invalid input')

    def test201(self): 
        self.assertEqual(classifyTriangle(201, 201, 1), 'InvalidInput', '201,201,1 should be invalid input')

    def test199(self): 
        self.assertEqual(classifyTriangle(199, 199, 199), 'Equilateral', '199,199,199 should be Equilateral')

    def testScaleneTriangleA(self): 
        self.assertEqual(classifyTriangle(4, 5, 6), 'Scalene', '4,5,6 is a Scalene triangle')

    def testScaleneTriangleB(self): 
        self.assertEqual(classifyTriangle(10, 11, 12), 'Scalene', '10,11,12 is a Scalene triangle')

    def testIsoscelesTriangleA(self): 
        self.assertEqual(classifyTriangle(7, 7, 4), 'Isosceles', '7,7,4 is an Isosceles triangle')

    def testIsoscelesTriangleB(self): 
        self.assertEqual(classifyTriangle(10, 10, 8), 'Isosceles', '10,10,8 is an Isosceles triangle')
        
    def testFloats(self): 
        self.assertEqual(classifyTriangle(1.1, 1.1, 1.1), 'InvalidInput', '1.1,1.1,1.1 should be invalid input')

    def testLetters(self): 
        self.assertEqual(classifyTriangle('x', 'y', 'z'), 'InvalidInput', 'x,y,z should be invalid input')

    def testBooleans(self): 
        self.assertEqual(classifyTriangle(False, True, False), 'InvalidInput', 'False,True,False should be invalid input')


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

