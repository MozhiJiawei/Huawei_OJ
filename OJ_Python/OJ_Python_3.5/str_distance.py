"""
计算字符串的相似度（100分）
"""


def calculate(a, a_start, b, b_start, result):
    if a_start >= len(a) and b_start >= len(b):
        return 0
    if a_start >= len(a):
        return len(b) - b_start
    if b_start >= len(b):
        return len(a) - a_start
    if a[a_start] == b[b_start]:
        if result[a_start + 1][b_start + 1] == -1:
            result[a_start + 1][b_start + 1] = calculate(a, a_start + 1, b, b_start + 1, result)
        return result[a_start + 1][b_start + 1]
    if result[a_start + 1][b_start] == -1:
        result[a_start + 1][b_start] = calculate(a, a_start + 1, b, b_start, result)
    if result[a_start][b_start + 1] == -1:
        result[a_start][b_start + 1] = calculate(a, a_start, b, b_start + 1, result)
    if result[a_start + 1][b_start + 1] == -1:
        result[a_start + 1][b_start + 1] = calculate(a, a_start + 1, b, b_start + 1, result)
    return min(result[a_start + 1][b_start] + 1,
               result[a_start][b_start + 1] + 1,
               result[a_start + 1][b_start + 1] + 1)


def calculate_string_distance(expression_A, expression_B):
    result = [[-1 for j in range(len(expression_B) + 1)] for i in range(len(expression_A) + 1)]
    return calculate(expression_A, 0, expression_B, 0, result)


if __name__ == "__main__":
    print("1/{}".format(calculate_string_distance(input(), input()) + 1))
