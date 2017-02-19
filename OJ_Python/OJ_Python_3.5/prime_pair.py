"""
查找组成一个偶数最接近的两个素数
"""


def generate_prime_set(n):
    prime_set = {2, 3, 5}
    for i in range(7, n):
        is_prime = True
        for item in prime_set:
            if i % item == 0:
                is_prime = False
            else:
                pass
        if is_prime:
            prime_set.add(i)
    return prime_set


def find_prime_number(n):
    prime_set_n = generate_prime_set(n)
    prime_list_n = list(prime_set_n)
    prime_list_n = list(filter(lambda x: x <= n / 2, prime_list_n))
    prime_list_n.sort(reverse=True)
    for x in prime_list_n:
        if (n - x) in prime_set_n:
            print(x)
            print(n - x)
            break


if __name__ == "__main__":
    n = int(input())
    find_prime_number(n)
