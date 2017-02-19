"""
24点（100分）/;'p
"""


def permute_recursive(num, begin, result):
    if begin == len(num):
        result.append(num.copy())

    for i in range(begin, len(num)):
        num[i], num[begin] = num[begin], num[i]
        permute_recursive(num, begin + 1, result)
        num[i], num[begin] = num[begin], num[i]


def permutation_4():
    result = []
    num = [0, 1, 2, 3]
    permute_recursive(num, 0, result)
    return result


def operator(a, b, op):
    if op == 0:
        return a + b
    if op == 1:
        return a - b
    if op == 2:
        return a * b
    if op == 3:
        return a / b


def try_24_exhaustive(num):
    if len(num) != 4:
        raise ValueError
    id_list = permutation_4()
    for x in id_list:
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    try:
                        result = operator(num[x[0]], num[x[1]], i)
                        result = operator(result, num[x[2]], j)
                        result = operator(result, num[x[3]], k)
                    except ZeroDivisionError:
                        continue
                    if result == 24:
                        """
                        operator_dict = {0: "+", 1: "-", 2: "*", 3: "/"}
                        print(num[x[0]], operator_dict[i], num[x[1]], operator_dict[j], num[x[2]], operator_dict[k],
                              num[x[3]], sep=" ")
                        """
                        return True
    return False


if __name__ == "__main__":
    num_input = [int(x) for x in input().strip().split()]
    if try_24_exhaustive(num_input):
        print("true")
    else:
        print("false")
