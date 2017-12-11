import unittest
from ..problem11 import *

class Problem11Test(unittest.TestCase):

    def test_find_path(self):
        self.assertEquals(find_path("ne,ne,ne"), 3)
        self.assertEquals(find_path("ne,ne,sw,sw"), 0)
        self.assertEquals(find_path("ne,ne,s,s"), 2)
        self.assertEquals(find_path("se,sw,se,sw,sw"), 3)

    def test_solve(self):
        self.assertEquals(find_path(read_file("./11/test/problem11_input.txt")[0]), 834)
        self.assertEquals(max_dist(read_file("./11/test/problem11_input.txt")[0]), 834)