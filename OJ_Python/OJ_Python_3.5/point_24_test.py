import unittest
from point_24 import try_24_exhaustive


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(try_24_exhaustive([7, 2, 1, 10]), True)

    def test2(self):
        self.assertEqual(try_24_exhaustive([1, 2, 3, 4]), False)


if __name__ == '__main__':
    unittest.main()
