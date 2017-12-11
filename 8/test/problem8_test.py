import unittest
from ..problem8 import *

class Problem8Test(unittest.TestCase):

    def test_problem(self):
        self.assertEquals(find_largest_input("./8/test/test_input8.txt"), (1, 10))
        self.assertEquals(find_largest_input("./8/test/problem8_input.txt"), (5946, 1))