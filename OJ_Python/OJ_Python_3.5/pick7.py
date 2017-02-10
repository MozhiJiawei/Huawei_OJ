"""
挑7（100分）
"""


def pick_7(N):
    n = 0
    for i in range(1, N+1):
        if i % 7 == 0 or str(i).count('7') != 0:
            n += 1
    return n

if __name__ == '__main__':
    N = int(input())
    print(pick_7(N))
