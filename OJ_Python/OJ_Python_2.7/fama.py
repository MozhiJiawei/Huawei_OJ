def fama(n, weight, nums):
    DP = {0}
    for i in range(n):
        for j in range(nums[i]):
            for item in DP.copy():
                DP.add(item + weight[i])
    return len(DP)


if __name__ == "__main__":
    n_in = int(input())
    weight_in = []
    nums_in = []
    for i in range(n_in):
        weight = int(input())
        weight_in.append(weight)
    for i in range(n_in):
        nums = int(input())
        nums_in.append(nums)
    print(fama(n_in, weight_in, nums_in))
