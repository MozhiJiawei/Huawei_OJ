def count1(num):
    if num < 0:
        num = - num
    count = 0
    while num != 0:
        count += num & 1
        num >>= 1
    return count


if __name__ == "__main__":
    n = int(input())
    print(count1(n))
