import unittest

class Problem12Test(unittest.TestCase):

    def test_find_connected(self):
        self.assertEquals(find_connected(""), 6)