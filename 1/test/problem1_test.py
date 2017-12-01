import unittest
from ..problem1 import returnIfEqual
from ..problem1 import pairwise
from ..problem1 import circleSum

class TestProblem(unittest.TestCase):

    def test_add_if_equal(self):
        self.assertEqual(returnIfEqual((1, 2)), 0)
        self.assertEqual(returnIfEqual((1, 1)), 1)

    def test_circle_sum(self):
        self.assertEqual(circleSum("1122"), 3)
        self.assertEqual(circleSum("1111"), 4)
        self.assertEqual(circleSum("1234"), 0)
        self.assertEqual(circleSum("91212129"), 9)
        
        
    