import unittest

class Problem7Test(unittest.TestCase):
    
    def test_find_base(self):
        self.assertEquals(find_base("./7/test/test_input.txt"), "tknk")
