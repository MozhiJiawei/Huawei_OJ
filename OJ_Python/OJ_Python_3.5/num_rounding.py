"""
取近似值
"""


s = float(input())
if s>0:
    print(int(s+0.5))
else:
    print(int(s-0.5))

"""
s = str(float(input())).split('.')
if len(s) == 1:
    result = int(s[0])
else:
    if s[0][0] != '-':
        if s[1][0] >= '0' and s[1][0] <= '4':
            result = int(s[0])
        else:
            result = int(s[0]) + 1
    else:
        if s[1][0] >= '0' and s[1][0] <= '4':
            result = int(s[0])
        else:
            result = int(s[0]) - 1

print(result)
input()
"""