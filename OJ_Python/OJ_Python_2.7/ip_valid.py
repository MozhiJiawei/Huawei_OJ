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


if __name__ == "__main__":
    if is_ip_valid(raw_input()):
        print "YES"
    else:
        print "NO"
