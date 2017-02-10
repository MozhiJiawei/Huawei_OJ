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

data = [int(t) for t in input().split()]
n, height = data[0], data[1:]
positive_inc = longest_inc(*height)
print(positive_inc)
negative_inc = longest_inc(*(height[::-1]))
print(negative_inc)
negative_inc.reverse()
for i, value in enumerate(positive_inc):
    positive_inc[i] += negative_inc[i] - 1
print(len(positive_inc) - max(positive_inc))
