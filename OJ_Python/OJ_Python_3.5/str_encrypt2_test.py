import unittest
from str_encrypt2 import (encrypt,
                          generate_keymap)

class MyTestCase(unittest.TestCase):
    def test_encrypt1(self):
        self.assertEqual(encrypt(generate_keymap("TRAILBLAZERS"), "Attack AT DAWN"), "Tpptad TP ITVH")

    def test_encrypt2(self):
        self.assertEqual(encrypt(generate_keymap("nihao"), "ni"), "le")

    def test_encrypt3(self):
        self.assertEqual(encrypt(generate_keymap("abcccddeeffgghhiijjkk"), "adjvxzjv%^*$^@$#@!!!11111"), "adjvxzjv%^*$^@$#@!!!11111")

if __name__ == '__main__':
    unittest.main()
