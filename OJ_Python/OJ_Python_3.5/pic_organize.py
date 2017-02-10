"""
图片整理（100分）
"""


def sort_str(seq):
    str_list = list(seq)
    str_list.sort()
    result = ''.join(str_list)
    return result

if __name__ == '__main__':
    s = input().strip()
    print(sort_str(s))
