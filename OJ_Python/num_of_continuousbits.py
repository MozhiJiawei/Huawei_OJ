"""
最大连续bit数（100分）
"""

num = bin(int(input())).replace('0b', '')
n = 0
cur_max = 0
for i, c in enumerate(num):
    if num[i] == '1':
        n += 1
    else:
        cur_max = max(cur_max, n)
        n = 0
print(max(cur_max, n))
