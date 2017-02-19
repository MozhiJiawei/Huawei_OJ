"""
查找输入整数二进制中1的个数（100分）
"""


def count1(num):
    count = 0
    while num != 0:
        count += 1
        num &= (num - 1)
    return count


if __name__ == "__main__":
    n = int(input())
    print(count1(n))
