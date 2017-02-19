import unittest
from DNA_gc_sequence import get_max_gcs_exhaustive


class MyTestCase(unittest.TestCase):
    def test1(self):
        self.assertEqual(get_max_gcs_exhaustive("AACTGTGCACGACCTGA", 5), "GCACG")

    def test2(self):
        self.assertEqual(get_max_gcs_exhaustive("AAACCCAAACCCACCCACCCACCCACCC", 5), "CCCACCC")

    def test3(self):
        self.assertEqual(get_max_gcs_exhaustive("CCGGCCGCGCGCG", 10), "CCGGCCGCGC")

    def test4(self):
        self.assertEqual(get_max_gcs_exhaustive("CCGGCCGCGCGCG", 100), None)


if __name__ == '__main__':
    unittest.main()
