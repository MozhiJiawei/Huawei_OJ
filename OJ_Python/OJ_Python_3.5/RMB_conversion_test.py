import unittest
from RMB_conversion import decimal_conversion, yuan_group_conversion, yuan_group_connection, convert


class MyTestCase(unittest.TestCase):
    def test_decimal_conversion_1(self):
        self.assertEqual(decimal_conversion("00"), "整")

    def test_decimal_conversion_2(self):
        self.assertEqual(decimal_conversion("01"), "壹分")

    def test_decimal_conversion_3(self):
        self.assertEqual(decimal_conversion("15"), "壹角伍分")

    def test_decimal_conversion_4(self):
        self.assertEqual(decimal_conversion("10"), "壹角")

    def test_decimal_conversion_5(self):
        self.assertEqual(decimal_conversion("72"), "柒角贰分")

    def test_yuan_group_conversion_1(self):
        self.assertEqual(yuan_group_conversion("0072"), "零零柒拾贰")

    def test_yuan_group_conversion_2(self):
        self.assertEqual(yuan_group_conversion("1001"), "壹仟零零壹")

    def test_yuan_group_conversion_3(self):
        self.assertEqual(yuan_group_conversion("0000"), "零")

    def test_yuan_group_conversion_4(self):
        self.assertEqual(yuan_group_conversion("0001"), "零零零壹")

    def test_yuan_group_conversion_5(self):
        self.assertEqual(yuan_group_conversion("8000"), "捌仟")

    def test_yuan_group_conversion_6(self):
        self.assertEqual(yuan_group_conversion("8010"), "捌仟零拾")

    def test_yuan_group_conversion_7(self):
        self.assertEqual(yuan_group_conversion("6247"), "陆仟贰佰肆拾柒")

    def test_yuan_group_conversion_8(self):
        self.assertEqual(yuan_group_conversion("0247"), "零贰佰肆拾柒")

    def test_yuan_group_connection_1(self):
        self.assertEqual(yuan_group_connection(["零零柒拾贰", "零零零壹", "零贰佰肆拾柒"]),
                         "柒拾贰亿零壹万零贰佰肆拾柒")

    def test_yuan_group_connection_2(self):
        self.assertEqual(yuan_group_connection(["零零零壹", "零", "零"]),
                         "壹亿")

    def test_convert_1(self):
        self.assertEqual(convert("151121.15"), "人民币拾伍万壹仟壹佰贰拾壹元壹角伍分")

    def test_convert_2(self):
        self.assertEqual(convert("10.00"), "人民币拾元整")

    def test_convert_3(self):
        self.assertEqual(convert("120000.00"), "人民币拾贰万元整")

    def test_convert_4(self):
        self.assertEqual(convert("0.15"), "人民币壹角伍分")

    def test_convert_5(self):
        self.assertEqual(convert("0.05"), "人民币伍分")

    def test_convert_6(self):
        self.assertEqual(convert("0.50"), "人民币伍角")

    def test_convert_7(self):
        self.assertEqual(convert("101.00"), "人民币壹佰零壹元整")

    def test_convert_8(self):
        self.assertEqual(convert("300000001.00"), "人民币叁亿零壹元整")


if __name__ == '__main__':
    unittest.main()
