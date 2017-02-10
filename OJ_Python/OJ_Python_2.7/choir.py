# -*- coding: utf-8 -*-
"""
合唱队(100分)
"""


def longest_inc(*seq):
    n = len(seq)
    inc = []
    for i in range(n):
        cur_max = 1
        for j in range(i):
            if seq[i] > seq[j]:
                cur_max = max(cur_max, inc[j] + 1)
        inc.append(cur_max)
    return inc

n = input()
height = [int(t) for t in raw_input().split()]
positive_inc = longest_inc(*height)
negative_inc = longest_inc(*(height[::-1]))
negative_inc.reverse()
for i, value in enumerate(positive_inc):
    positive_inc[i] += negative_inc[i] - 1
print(len(positive_inc) - max(positive_inc))
