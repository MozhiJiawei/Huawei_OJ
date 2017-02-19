"""
iNOC产品部--完全数计算
"""
import math


def count(n):
    if n < 0 or n > 500000:
        return -1
    complete_num = [6, 28, 496, 8128]
    for i, item in enumerate(complete_num):
        if item > n:
            return i
    return 4


def print_complete_num(n):
    for i in range(2, n):
        sum_i = 1
        for j in range(2, int(math.sqrt(i)) + 1):
            if i % j == 0:
                sum_i += j + i / j
            else:
                pass
        if sum_i == i:
            print(i)


if __name__ == "__main__":
    n = int(input())
    print(count(n))
