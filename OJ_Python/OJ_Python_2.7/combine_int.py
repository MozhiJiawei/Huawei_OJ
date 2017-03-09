def combine_by_sort(list_1, list_2):
    result = set()
    for x in list_1:
        if x not in result:
            result.add(x)
    for x in list_2:
        if x not in result:
            result.add(x)
    result = list(result)
    result.sort()
    return result


if __name__ == "__main__":
    n1 = int(input())
    list_1_in = [int(i) for i in raw_input().strip().split()]
    n2 = int(input())
    list_2_in = [int(i) for i in raw_input().strip().split()]
    result = combine_by_sort(list_1_in, list_2_in)
    print(''.join(map(str, result)))
