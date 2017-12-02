import unittest
from ..problem1 import *

class TestProblem(unittest.TestCase):

    def test_add_if_equal(self):
        self.assertEqual(return_if_equal((1, 2)), 0)
        self.assertEqual(return_if_equal((1, 1)), 1)

    def test_circle_sum(self):
        self.assertEqual(circle_sum_next("1122"), 3)
        self.assertEqual(circle_sum_next("1111"), 4)
        self.assertEqual(circle_sum_next("1234"), 0)
        self.assertEqual(circle_sum_next("91212129"), 9)

    def test_circle_sum(self):
        self.assertEqual(circle_sum_half("1212"), 6)
        self.assertEqual(circle_sum_half("1221"), 0)
        self.assertEqual(circle_sum_half("123425"), 4)
        self.assertEqual(circle_sum_half("123123"), 12)    
        self.assertEqual(circle_sum_half("12131415"), 4)    