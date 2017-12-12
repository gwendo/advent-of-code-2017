import unittest
from ..problem10 import *
from operator import xor

class Problem10Test(unittest.TestCase):

    def test_twist(self):
        self.assertEquals(twist(5, "3, 4, 1, 5"), 12)
        self.assertEquals(twist(256, "88,88,211,106,141,1,78,254,2,111,77,255,90,0,54,205"), 11375 )

    def test_twist2(self):
        self.assertEquals(twist2(256, ""), "a2582a3a0e66e6e86e3812dcb672a272" )    
        self.assertEquals(twist2(256, "AoC 2017"), "33efeb34ea91902bb2f59c9920caa6cd" )    
        self.assertEquals(twist2(256, "1,2,3"), "3efbe78a8d82f29979031a4aa0b16a9d" )   
        self.assertEquals(twist2(256, "88,88,211,106,141,1,78,254,2,111,77,255,90,0,54,205"), "e0387e2ad112b7c2ef344e44885fe4d8" )
        
