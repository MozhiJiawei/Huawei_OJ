"""
自守数（100分）
"""


def calc_self_holding_numbers(n):
    result = []
    for i in range(n + 1):
        i_square = i * i
        is_self_holding = True
        num = i
        while i != 0:
            if i % 10 != i_square % 10:
                is_self_holding = False
                break
            else:
                i //= 10
                i_square //= 10
        if is_self_holding:
            result.append(num)
    return result


if __name__ == "__main__":
    print(len(calc_self_holding_numbers(2000)))
