#  ARRANGE
#  ACT
#  ASSERT

###  ---------------------------- ###
###  ---------- ARRANGE --------- ###
###  ---------------------------- ###
import unittest
# importing unittest  - python's in-built test module.
from src.calculator import *
# importing the source code we are looking to test

# define the test class (Test+whatever we are testing) and assigning it a superclass to inherit from
# utilising the functionaility provided by python's in built unittest module
class TestCalculator(unittest.TestCase):
    

# next we set up the test using the format 
# test_ + the function/method that we are testing. 
###  ---------------------------- ###
###  ----------   ACT   --------- ###
###  ---------------------------- ###
    def test_add(self):
# we use assertEqual (which again comes from unittest) 
# to compare the expected result with actual result
###  ---------------------------- ###
###  ---------- ASSERT ---------- ###
###  ---------------------------- ###
        self.assertEqual(5, add(2,3))

# this can also be written: 

    # def test_add(self):
    #     expected = 5
    #     actual = add(2,3)
    #     self.assertEqual(expected, actual)

#  ARRANGE
#  ACT
#  ASSERT

    def test_subtract(self):
        self.assertEqual(3, subtract(10,7))

    def test_divide(self):
        self.assertEqual(5, divide(25,5))

    def test_multiply(self):
        expected = 100
        actual = multiply(10,10)
        self.assertEqual(expected, actual)
