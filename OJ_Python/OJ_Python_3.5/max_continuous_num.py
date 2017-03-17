"""
在字符串中找出连续最长的数字串（100分）
"""

import re


def continue_max(input_str: str) -> str:
    num_list = re.split(r'\D+', input_str)
    result = ""
    for item in num_list:
        if len(item) > len(result):
            result = item
    if not result:
        return "0"
    else:
        return result + "," + str(len(result))


if __name__ == "__main__":
    input_str = input()
    print(continue_max(input_str))
