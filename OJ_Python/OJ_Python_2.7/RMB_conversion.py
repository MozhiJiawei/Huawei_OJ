# coding:utf-8
"""
人民币转换（100分）
"""

import re


def decimal_conversion(decimal):
    num_dict = {"0": u"零", "1": u"壹", "2": u"贰", "3": u"叁", "4": u"肆", "5": u"伍", "6": u"陆", "7": u"柒",
                "8": u"捌", "9": u"玖"}

    result = ""
    if decimal[0] != "0":
        result += num_dict[decimal[0]] + u"角"
    if decimal[1] != "0":
        result += num_dict[decimal[1]] + u"分"

    if not result:
        return u"整"
    else:
        return result


def yuan_group_conversion(yuan):
    num_dict = {"0": u"零", "1": u"壹", "2": u"贰", "3": u"叁", "4": u"肆", "5": u"伍", "6": u"陆", "7": u"柒",
                "8": u"捌", "9": u"玖"}

    while len(yuan) < 4:
        yuan = "0" + yuan
    result = ""
    result += num_dict[yuan[0]]
    if yuan[0] != "0":
        result += u"仟"

    result += num_dict[yuan[1]]
    if yuan[1] != "0":
        result += u"佰"

    if yuan[2] == "1":
        result += u"拾"
    else:
        result += num_dict[yuan[2]]
        if yuan[2] != "0":
            result += u"拾"

    result += num_dict[yuan[3]]
    result = re.sub(ur"零+$", "", result)
    if not result:
        return u"零"
    else:
        return result


def yuan_group_connection(yuan_list):
    digit_dict = {0: "", 1: u"万", 2: u"亿"}
    result = ""
    for i, item in enumerate(yuan_list):
        if item != u"零":
            result += item + digit_dict[len(yuan_list) - i - 1]
        else:
            result += u"零"
    result = re.sub(ur"零+", u"零", result)
    result = re.sub(ur"^零+", "", result)
    result = re.sub(ur"零$", "", result)
    if result == "":
        return u"零"
    else:
        return result


def convert(money):
    yuan, decimal = money.split('.')
    while len(yuan) % 4 != 0:
        yuan = "0" + yuan
    yuan_group = re.findall(ur".{4}", yuan)
    yuan_group = list(map(yuan_group_conversion, yuan_group))
    yuan_cn = yuan_group_connection(yuan_group)
    decimal_cn = decimal_conversion(decimal)
    if yuan_cn == u"零" and decimal_cn != u"整":
        return u"人民币" + decimal_cn
    return u"人民币" + yuan_cn + u"元" + decimal_cn


if __name__ == "__main__":
    print(convert(raw_input().strip()).encode('utf-8'))
