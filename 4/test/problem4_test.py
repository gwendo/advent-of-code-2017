import unittest
from ..problem4 import *


class Problem4Test(unittest.TestCase):

    def test_is_valid_password(self):
        self.assertTrue(is_valid_password("aa bb cc dd"))
        self.assertFalse(is_valid_password("aa bb aa cc"))
        self.assertTrue(is_valid_password("aa bb cc dd aaa"))

    def test_find_valid_passwords(self):
        self.assertEquals(find_valid_passwords("./4/test/test_input.txt", is_valid_password), 2)
        self.assertEquals(find_valid_passwords("./4/test/problem_input.txt", is_valid_password), 451)

    def test_anagram_password(self):
        self.assertTrue(is_anagram_password("abcde fghij"))
        self.assertFalse(is_anagram_password("abcde xyz ecdab"))
        self.assertTrue(is_anagram_password("a ab abc abd abf abj"))
        self.assertTrue(is_anagram_password("iiii oiii ooii oooi oooo"))
        self.assertFalse(is_anagram_password("oiii ioii iioi iiio"))

    def test_find_valid_anagram_passwords(self):
        self.assertEquals(find_valid_passwords("./4/test/problem_input.txt", is_anagram_password), 223)
