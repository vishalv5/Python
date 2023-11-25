from rearrange import rearrange_name
import unittest

class TestRearrange(unittest.TestCase):
    def test_basi(self):
        testcase="LaveLace, Ada"
        expected="Ada LaveLace"
        self.assertEqual(rearrange_name(testcase),expected)


    def test_empty(self):
        testcase=""
        expected=""
        self.assertEqual(rearrange_name(testcase),expected
        )

unittest.main()