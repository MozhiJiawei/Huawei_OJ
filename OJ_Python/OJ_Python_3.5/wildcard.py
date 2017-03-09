"""
通配符（100分）
"""


def is_same_character(c_wildcard, c_s):
    c_wildcard = c_wildcard.upper()
    c_s = c_s.upper()
    if c_wildcard == "?" or c_wildcard == c_s:
        return True
    else:
        return False


def wildcard_valid_backtrack(wildcard, wildcard_start, s, s_start):
    if s_start == len(s) and wildcard_start == len(wildcard):
        return True
    s_index = s_start
    for wildcard_index in range(wildcard_start, len(wildcard)):
        if is_same_character(wildcard[wildcard_index], s[s_index]):
            s_index += 1
        elif wildcard[wildcard_index] == "*":
            # "*" is the last character
            if wildcard_index + 1 == len(wildcard):
                return True
            # check every character
            for s_index in range(s_start, len(s)):
                if is_same_character(wildcard[wildcard_index + 1], s[s_index]) or wildcard[wildcard_index + 1] == "*":
                    if wildcard_valid_backtrack(wildcard, wildcard_index + 1, s, s_index):
                        return True
            return False
        else:
            return False
    return True


def wildcard_valid_checker(wildcard, s):
    return wildcard_valid_backtrack(wildcard, 0, s, 0)


if __name__ == '__main__':
    input_with_wildcard = input().strip()
    s_input = input().strip()
    if wildcard_valid_checker(input_with_wildcard, s_input):
        print("true")
    else:
        print("false")
