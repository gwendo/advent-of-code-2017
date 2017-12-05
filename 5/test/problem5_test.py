import unittest
from ..problem5 import *


class Problem5Test(unittest.TestCase):

    def test_solve_for_string(self):
        self.assertEquals(solve_for_string("0 3  0  1  -3"), 5)

    def test_solve_for_string_strange_jump(self):
        self.assertEquals(solve_for_string_with_strange_jump("0 3  0  1  -3"), 10)

    def test_solve_for_file(self):
        self.assertEquals(solve_for_file("./5/test/test_input.txt"), 354121)

    #def test_solve_for_file_with_strange_jump(self):
    #    self.assertEquals(solve_for_file_with_strange_jump("./5/test/test_input.txt"), 27283023)
