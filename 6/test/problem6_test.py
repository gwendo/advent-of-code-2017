import unittest
from ..problem6 import *

class Problem6Test(unittest.TestCase):

    def test_redistribute(self):
        self.assertEquals(redistribute("0 2 7 0"), 5)