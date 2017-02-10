"""
判断两个IP是否属于同一子网（100分）
"""


def ip_to_int(ip):
    ip = [bin(int(i)).replace('0b', '').zfill(8) for i in ip.strip().split('.')]
    ip = int(''.join(ip), 2)
    return ip


def is_ip_valid(ip):
    ip = ip.strip().split('.')
    if len(ip) != 4:
        return False
    for i, item in enumerate(ip):
        try:
            ip[i] = int(item)
        except ValueError:
            return False
    if ip[0] < 1 or ip[0] > 255:
        return False
    for i in range(1, 4):
        if ip[i] < 0 or ip[i] > 255:
            return False
    return True


def is_mask_valid(mask):
    if not is_ip_valid(mask):
        return False
    mask = ip_to_int(mask)
    if mask | (mask - 1) != 0xFFFFFFFF:
        return False
    return True


def check_net_segment(mask, ip1, ip2):
    if not (is_ip_valid(ip1) and is_ip_valid(ip2) and is_mask_valid(mask)):
        return 1
    mask = ip_to_int(mask)
    ip1 = ip_to_int(ip1)
    ip2 = ip_to_int(ip2)
    if (mask & ip1) == (mask & ip2):
        return 0
    else:
        return 2


if __name__ == "__main__":
    mask = input()
    ip1 = input()
    ip2 = input()
    print(check_net_segment(mask, ip1, ip2))
