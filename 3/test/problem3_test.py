import unittest
from ..problem3 import *

class Problem3Test(unittest.TestCase):

    def test_find_distance(self):
        self.assertEquals(find_distance(1), 0)
        self.assertEquals(find_distance(12), 3)
        self.assertEquals(find_distance(23), 2)
        self.assertEquals(find_distance(1024), 31)
        

    def test_distance(self):
        self.assertEquals(distance((0, 1)), 1)
        self.assertEquals(distance((4, 5)), 9)

    def test_find_sum_adjecent(self):
        self.assertEquals(find_sum_larger_than_input(5), 10)
        
    #def test_generate(self):
    #    self.assertEquals(build_coordinate_system(20), "")
        