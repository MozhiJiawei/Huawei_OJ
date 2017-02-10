"""
质数因子
"""

def PrimeFactor(num):
    i = 2
    while i <= num:
        if num % i == 0:
            yield i
            num = num / i
        else:
            i += 1

n = int(input())
s = ""
for n in PrimeFactor(n):
    s += "{} ".format(n)

print(s.strip())
input()