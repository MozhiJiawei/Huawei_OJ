import unittest
from wildcard import wildcard_valid_checker


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(wildcard_valid_checker("te?t*.*", "txt12.xls"), False)

    def test_2(self):
        self.assertEqual(wildcard_valid_checker("*.*", "txt12.xls"), True)

    def test_3(self):
        self.assertEqual(wildcard_valid_checker("AABBCCDDEEFFGG?*CBW", "AABBCCDDEEFFGGvCBW"), True)

    def test_4(self):
        self.assertEqual(wildcard_valid_checker("Tex*.*ls", "tex.ls"), True)

    def test_5(self):
        self.assertEqual(wildcard_valid_checker("cmbcmbklcawet", "q7e8612424"), False)

    def test_6(self):
        self.assertEqual(wildcard_valid_checker("******001", "b001"), True)


if __name__ == '__main__':
    unittest.main()
