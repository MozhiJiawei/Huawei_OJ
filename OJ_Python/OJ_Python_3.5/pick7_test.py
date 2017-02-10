import unittest
from pick7 import pick_7


class MyTestCase(unittest.TestCase):
    def test_pick7_1(self):
        self.assertEqual(pick_7(20), 3)

    def test_pick7_2(self):
        self.assertEqual(pick_7(0), 0)

    def test_pick_3(self):
        self.assertEqual(pick_7(10), 1)

    def test_pick_4(self):
        self.assertEqual(pick_7(30), 6)

if __name__ == '__main__':
    unittest.main()
