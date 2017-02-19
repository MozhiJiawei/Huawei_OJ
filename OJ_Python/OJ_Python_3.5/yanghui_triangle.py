"""
iNOC产品部-杨辉三角的变形（100分）
"""


def generate_yh_triangle(N, flag=False):
    result = [[1]]
    for i in range(1, N):
        row_i = []
        for j in range(2 * i + 1):
            up_left = 0 if j not in range(2, 2 * i + 1) else result[i - 1][j - 2]
            up = 0 if j not in range(1, 2 * i) else result[i - 1][j - 1]
            up_right = 0 if j not in range(2 * i - 1) else result[i - 1][j]
            if flag:
                if (up_left + up + up_right) % 2 == 0:
                    row_i.append(0)
                else:
                    row_i.append(1)
            else:
                row_i.append(up_left + up + up_right)
        result.append(row_i)
    return result


for item in generate_yh_triangle(20, True):
    print(*item, sep=' ', end='\n')

n = int(input())
result = {0: 4, 1: 2, 2: 3, 3: 2}
if n < 3:
    print(-1)
else:
    print(result[(n - 2) % 4])
