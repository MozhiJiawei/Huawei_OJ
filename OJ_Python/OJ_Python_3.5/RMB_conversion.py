"""
人民币转换（100分）
"""

import re


def decimal_conversion(decimal: str) -> str:
    num_dict = {"0": "零", "1": "壹", "2": "贰", "3": "叁", "4": "肆", "5": "伍", "6": "陆", "7": "柒", "8": "捌",
                "9": "玖"}

    result = ""
    if decimal[0] != "0":
        result += num_dict[decimal[0]] + "角"
    if decimal[1] != "0":
        result += num_dict[decimal[1]] + "分"

    if not result:
        return "整"
    else:
        return result


def yuan_group_conversion(yuan: str) -> str:
    num_dict = {"0": "零", "1": "壹", "2": "贰", "3": "叁", "4": "肆", "5": "伍", "6": "陆", "7": "柒", "8": "捌",
                "9": "玖"}
    digit_list = ["仟", "佰", "拾", ""]
    result = ""
    for i, c in enumerate(yuan):
        result += num_dict[c] + digit_list[i]

    result = re.sub(r"零[仟佰拾]", "零", result)
    result = re.sub(r"壹拾", "拾", result)
    result = re.sub(r"零+$", "", result)
    if not result:
        return "零"
    else:
        return result


def yuan_group_connection(yuan_list: list) -> str:
    digit_dict = {0: "", 1: "万", 2: "亿"}
    result = ""
    for i, item in enumerate(yuan_list):
        if item != "零":
            result += item + digit_dict[len(yuan_list) - i - 1]
        else:
            result += "零"
    result = re.sub(r"零+", "零", result)
    result = re.sub(r"^零+", "", result)
    result = re.sub(r"零$", "", result)
    if result == "":
        return "零"
    else:
        return result


def convert(money: str) -> str:
    yuan, decimal = money.split('.')
    while len(yuan) % 4 != 0:
        yuan = "0" + yuan
    yuan_group = re.findall(r".{4}", yuan)
    yuan_group = list(map(yuan_group_conversion, yuan_group))
    yuan_cn = yuan_group_connection(yuan_group)
    decimal_cn = decimal_conversion(decimal)
    if yuan_cn == "零" and decimal_cn != "整":
        return "人民币" + decimal_cn
    return "人民币" + yuan_cn + "元" + decimal_cn


if __name__ == "__main__":
    print(convert(input().strip()))
