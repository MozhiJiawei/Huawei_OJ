def generate_matrix(N):
    result = []
    for i in range(N):
        line_i = []
        for j in range(N - i):
            num = int(((i + j) ** 2 + (i + j)) / 2 + j + 1)
            line_i.append(num)
        result.append(line_i)
    return result


if __name__ == '__main__':
    N = int(input())
    matrix = generate_matrix(N)
    for m in matrix:
        m = map(str, m)
        print(' '.join(m))
