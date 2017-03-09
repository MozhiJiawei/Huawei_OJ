def get_result(my_list):
    for i in range(101):
        for j in range(101 - i):
            k = 100 - i - j
            if i * 5 + j * 3 + float(k) / 3 == 100:
                my_list.append([i, j, k])


start = int(input())
result = []
get_result(result)
for item in result:
    print ' '.join(map(str, item))
