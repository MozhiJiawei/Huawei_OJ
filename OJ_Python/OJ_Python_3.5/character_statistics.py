"""
字符统计（100分）
"""

str_input = input()
c_dict = dict()
for c in str_input:
    if ord(c) < 128:
        if c in c_dict:
            c_dict[c] += 1
        else:
            c_dict[c] = 1
c_list = list(c_dict.items())
c_list.sort(key=lambda x: x[0])
c_list.sort(key=lambda x: x[1], reverse=True)
for x in c_list:
    print(x[0], end='')
