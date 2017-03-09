def get_max_gcs_exhaustive(dna, n):
    if n > len(dna):
        return None
    dp = [[-1 for j in range(len(dna) - i)] for i in range(len(dna))]
    cur_max = 0
    result = ""
    for i in range(n - 1, len(dna)):
        for j in range(len(dna) - i):
            if i == 0 or dp[i - 1][j] == -1:
                dp[i][j] = 0.
                for k in range(i + 1):
                    if dna[j + k] == 'G' or dna[j + k] == 'C':
                        dp[i][j] += 1
                dp[i][j] /= (i + 1)
            elif dna[i + j] == 'G' or dna[i + j] == 'C':
                dp[i][j] = (dp[i - 1][j] * i + 1) / (i + 1)
            else:
                dp[i][j] = (dp[i - 1][j] * i) / (i + 1)
            if dp[i][j] > cur_max:
                cur_max = dp[i][j]
                result = dna[j: j + i + 1]
    return result


if __name__ == "__main__":
    dna_input = raw_input()
    n = int(input())
    print(get_max_gcs_exhaustive(dna_input, 5))
