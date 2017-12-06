import unittest
from ..problem6 import *

class Problem6Test(unittest.TestCase):

    def test_redistribute(self):
        self.assertEquals(find_first_duplicate(map(lambda x: int(x), "0 2 7 0".split(None)))[0], 5)
        self.assertEquals(find_first_duplicate(map(lambda x: int(x), "2	8	8	5	4	2	3	1	5	5	1	2	15	13	5	14".split(None)))[0], 3156)

    def test_redistribute_twice(self):
        self.assertEquals(redistribute_twice("2 4 1 2"), 4)
        self.assertEquals(redistribute_twice("2	8	8	5	4	2	3	1	5	5	1	2	15	13	5	14"), 1610)
