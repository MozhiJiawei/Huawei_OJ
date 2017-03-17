import re


def continue_max(input_str):
    num_list = re.split(r'\D+', input_str)
    result = ""
    for item in num_list:
        if len(item) > len(result):
            result = item
    if not result:
        return "0"
    else:
        return result + "," + str(len(result))


if __name__ == "__main__":
    input_str = raw_input()
    print(continue_max(input_str))
