"""
字符串加解密（100分）
"""


def encrypt(s):
    s_ascii = bytearray(s, 'ascii').swapcase()
    for i, c in enumerate(s_ascii):
        if chr(c).isalpha():
            if c == ord('z') or c == ord('Z'):
                s_ascii[i] += ord('A') - ord('Z')
            else:
                s_ascii[i] += 1
        elif chr(c).isalnum():
            if c == ord('9'):
                s_ascii[i] = ord('0')
            else:
                s_ascii[i] += 1
        else:
            pass
    return s_ascii.decode('ascii')


def decrypt(s):
    s_ascii = bytearray(s, 'ascii').swapcase()
    for i, c in enumerate(s_ascii):
        if chr(c).isalpha():
            if c == ord('a') or c == ord('A'):
                s_ascii[i] += ord('Z') - ord('A')
            else:
                s_ascii[i] -= 1
        elif chr(c).isalnum():
            if c == ord('0'):
                s_ascii[i] = ord('9')
            else:
                s_ascii[i] -= 1
        else:
            pass
    return s_ascii.decode('ascii')


if __name__ == '__main__':
    s1 = input()
    s2 = input()
    print(encrypt(s1))
    print(decrypt(s2))
