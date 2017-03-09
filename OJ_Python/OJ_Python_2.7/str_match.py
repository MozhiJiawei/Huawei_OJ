def is_all_char_exist(short_str, long_str):
    short_str_set = set(short_str)
    for c in long_str:
        short_str_set.discard(c)
    if short_str_set:
        return "false"
    else:
        return "true"


if __name__ == "__main__":
    short_str_in = raw_input()
    long_str_in = raw_input()
    print(is_all_char_exist(short_str_in, long_str_in))
