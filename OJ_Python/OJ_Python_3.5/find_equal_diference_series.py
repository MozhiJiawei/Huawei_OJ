"""
寻找等差数列（100分）
"""


def generate_prime_list(m, n):
    prime_list = [2, 3, 5]
    for i in range(7, n + 1):
        is_prime = True
        for item in prime_list:
            if i % item == 0:
                is_prime = False
            else:
                pass
        if is_prime:
            prime_list.append(i)
    return list(filter(lambda x: x >= m, prime_list))


def find_eds(prime_list: list, dp: list, eds: list, diff: int, j: int):
    eds.append(prime_list[j])
    for i in range(j, len(dp)):
        if dp[i][j] == diff:
            dp[i][j] = -1
            find_eds(prime_list, dp, eds, diff, i)
    return


def find_longest_eds(m, n):
    prime_list = generate_prime_list(m, n)
    n_prime = len(prime_list)
    dp = [[-1] * n_prime for i in range(n_prime)]
    for i in range(n_prime):
        for j in range(i):
            dp[i][j] = prime_list[i] - prime_list[j]

    eds_list = []
    for i in range(n_prime):
        for j in range(i):
            if dp[i][j] != -1:
                eds = [prime_list[j]]
                find_eds(prime_list, dp, eds, dp[i][j], i)
                dp[i][j] = -1
                if len(eds) > 2:
                    eds_list.append(eds)
    len_eds = list(map(len, eds_list))
    max_len_eds = max(len_eds)
    result = []
    for i, item in enumerate(len_eds):
        if item == max_len_eds:
            if not result:
                result = eds_list[i]
            elif eds_list[i][-1] > result[-1]:
                result = eds_list[i]
    return result


if __name__ == "__main__":
    m = int(input())
    n = int(input())
    print(*find_longest_eds(m, n), sep='\n')
