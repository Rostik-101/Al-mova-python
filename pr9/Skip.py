import mymath
import sys
import unittest


class TestAdd(unittest.TestCase):
    def test_add_integers(self):
        result = mymath.add(1, 2)
        self.assertEqual(result, 3)


    def test_add_floats(self):
        result = mymath.add(10.5, 2)
        self.assertEqual(result, 12.5)

    @unittest.skip('Skip this test')
    def test_add_strings(self):
        result = mymath.add('abc', 'def')
        self.assertEqual(result, 'abcdef')

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test_adding_on_windows(self):
        result = mymath.add(1, 2)
        self.assertEqual(result, 3)

    