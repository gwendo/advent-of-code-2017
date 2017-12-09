import unittest
from ..problem9 import *

class Problem9Test(unittest.TestCase):

    def test_find_groups(self):
        self.assertEquals(find_groups("{}"), (1,0))
        self.assertEquals(find_groups("{{<a!>},{<a!>},{<a!>},{<ab>}}"), (3, 17))
        self.assertEquals(find_groups("{{<ab>},{<ab>},{<ab>},{<ab>}}"), (9, 8))
        self.assertEquals(find_groups(read_file("./9/test/problem9_input.txt")[0]), (12803, 6425))

    def test_find_garbage(self):
        self.assertEquals(find_groups("<>"), (0,0))
        self.assertEquals(find_groups("<random characters>"), (0,17))
        self.assertEquals(find_groups("<random characters>"), (0,17))
        self.assertEquals(find_groups("<<<<>"), (0,3))
        self.assertEquals(find_groups("<{!>}>"), (0,2))
        self.assertEquals(find_groups("<!!>"), (0,0))
        self.assertEquals(find_groups("<!!!>>"), (0,0))
        self.assertEquals(find_groups("<{oai!a,<{i<a>"), (0,10))
         
        