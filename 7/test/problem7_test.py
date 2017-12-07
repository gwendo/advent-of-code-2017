import unittest
from ..problem7 import *

class Problem7Test(unittest.TestCase):
    
    def test_find_base(self):
        self.assertEquals(find_base("./7/test/test_input.txt").n, "tknk")

    def test_find_base_sol(self):
        self.assertEquals(find_base("./7/test/problem7_input.txt").n, "cyrupz")

    def test_find_weight(self):
        self.assertEquals(find_unbalanced(find_progs("./7/test/test_input.txt")), 60)

    def test_find_weight_sol(self):
        self.assertEquals(find_unbalanced(find_progs("./7/test/problem7_input.txt")), 193)
