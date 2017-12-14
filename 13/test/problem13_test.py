import unittest
from ..problem13 import *

class Problem13Test(unittest.TestCase):

    def test_find_severity(self):
        self.assertEquals(find_severity(read_file("./13/test/test_input.txt")), 24)
        self.assertEquals(find_severity(read_file("./13/test/problem13_input.txt")), 1300)

    def test_find_delay(self):
        self.assertEquals(find_delay(read_file("./13/test/test_input.txt")), 10)
