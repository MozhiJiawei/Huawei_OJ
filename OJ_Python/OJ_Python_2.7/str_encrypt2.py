def generate_keymap(key):
    key = key.upper()
    key_value = []
    for c in key:
        if c not in key_value:
            key_value.append(c)
    for i in range(26):
        if chr(ord('A') + i) not in key_value:
            key_value.append(chr(ord('A') + i))
    key_key = [chr(ord('A') + i) for i in range(26)]
    return dict(zip(key_key, key_value))


def encrypt(keymap, s):
    s = bytearray(s, 'ascii')
    for i, c in enumerate(s):
        if chr(c).isalpha():
            s[i] = ord(keymap[chr(c).upper()])
            if chr(c).islower():
                s[i] += ord('a') - ord('A')
            else:
                pass
        else:
            pass
    return s.decode('ascii')


if __name__ == '__main__':
    key = raw_input()
    s = raw_input()
    key_map = generate_keymap(key)
    print(encrypt(key_map, s))
