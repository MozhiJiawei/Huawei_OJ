import unittest
from str_encrypt import encrypt
from str_encrypt import decrypt


class MyTestCase(unittest.TestCase):
    def test_encrypt1(self):
        self.assertEqual(encrypt("abcdefgzZ"), "BCDEFGHAa")

    def test_encrypt2(self):
        self.assertEqual(encrypt("1234567890"), "2345678901")

    def test_encrypt3(self):
        self.assertEqual(encrypt("abcdefgzZ1234567890"), "BCDEFGHAa2345678901")

    def test_encrypt4(self):
        self.assertEqual(encrypt("abcdefgzZ1234567890!@#%^*(*^%*&"), "BCDEFGHAa2345678901!@#%^*(*^%*&")

    def test_decrypt1(self):
        self.assertEqual(decrypt("BCDEFGHAa"), "abcdefgzZ")

    def test_decrypt2(self):
        self.assertEqual(decrypt("2345678901"), "1234567890")

    def test_decrypt3(self):
        self.assertEqual(decrypt("BCDEFGHAa2345678901"), "abcdefgzZ1234567890")

    def test_decrypt4(self):
        self.assertEqual(decrypt("BCDEFGHAa23   45678901!@#%^*(*^%*&"), "abcdefgzZ12   34567890!@#%^*(*^%*&")

if __name__ == '__main__':
    unittest.main()
