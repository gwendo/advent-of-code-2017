import unittest
from ..problem2 import *

class Problem2Tests(unittest.TestCase):

    def test_find_diff(self):
        self.assertEquals(get_diff("5 1 9 5"), 8)
        self.assertEquals(get_diff("7 5 3"), 4)
        self.assertEquals(get_diff("2 4 6 8"), 6)

    def test_calc_checksum(self):
        self.assertEqual(calc_check_sum("./2/test/test_input.txt"), 18)

    def test_calc_checksum2(self):
        self.assertEqual(calc_check_sum("./2/test/test_input2.txt"), 8684)

    def test_evenly_divided(self):
        self.assertEquals(get_evenly_divided_sum("5 9 2 8"), 4)
        self.assertEquals(get_evenly_divided_sum("9 4 7 3"), 3)
        self.assertEquals(get_evenly_divided_sum("3 8 6 5"), 2)

    def test_calc_even_checksum(self):
        self.assertEquals(calc_even_sum("./2/test/test_input3.txt"), 9)
