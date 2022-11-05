from ctypes import cdll
import unittest

calculate = cdll.LoadLibrary('calculate.dll')


class CalculateTest(unittest.TestCase):
    def setUp(self):
        print("This is calculate test from c")

    def testSum(self):
        self.assertEqual(3+3, calculate.sum(3, 3))

    def testMultiply(self):
        self.assertEqual(3*3, calculate.multiply(3, 3))
