import unittest
from ip_subnet import (is_ip_valid,
                       is_mask_valid,
                       check_net_segment)

class MyTestCase(unittest.TestCase):
    def test_ipvalid(self):
        self.assertEqual(is_ip_valid("192.168.1.152"), True)

    def test_ipvalid1(self):
        self.assertEqual(is_ip_valid("255.255.255.256"), False)

    def test_ipvalid2(self):
        self.assertEqual(is_ip_valid("255.255.255.256dd"), False)

    def test_ipvalid5(self):
        self.assertEqual(is_ip_valid("c44va562wegbvcxa"), False)

    def test_maskvalid1(self):
        self.assertEqual(is_mask_valid("255.255.255.0"), True)

    def test_maskvalid2(self):
        self.assertEqual(is_mask_valid("255.224.0.0"), True)

    def test_maskvalid3(self):
        self.assertEqual(is_mask_valid("255.192.224.0"), False)

    def test_subnet1(self):
        self.assertEqual(check_net_segment("255.255.255.0", "192.168.224.256", "192.168.10.4"), 1)

    def test_subnet2(self):
        self.assertEqual(check_net_segment("255.255.255.0", "192.168.0.1", "192.168.0.254"), 0)

    def test_subnet3(self):
        self.assertEqual(check_net_segment("255.255.255.0", "192.0.0.1", "192.168.0.254"), 2)

if __name__ == '__main__':
    unittest.main()
