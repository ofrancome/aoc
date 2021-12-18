def readfile(file):
    with open(file) as f:
        lines = f.read().splitlines()
    return lines


def bit_list_to_int(bits):
    res = 0
    for bit in bits:
        res = (res << 1) | bit
    return res
