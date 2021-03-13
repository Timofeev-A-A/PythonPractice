def f21(x):
    if x[1] == 1987:
        if x[2] == 1975:
            if x[0] == 'java':
                if x[3] == 'awk':
                    return 0
                elif x[3] == 'sql':
                    return 1
                elif x[3] == 'raml':
                    return 2
            elif x[0] == 'sass':
                if x[4] == 1986:
                    return 3
                elif x[4] == 2011:
                    return 4
        elif x[2] == 1992:
            return 5
        elif x[2] == 2012:
            if x[0] == 'java':
                if x[4] == 1986:
                    return 6
                elif x[4] == 2011:
                    return 7
            elif x[0] == 'sass':
                return 8
    elif x[1] == 1983:
        if x[4] == 1986:
            return 9
        elif x[4] == 2011:
            return 10
    elif x[1] == 1957:
        return 11


def f22(x):
    a = x & 0b00000000000000000111111111111111
    b = x & 0b00000000000111111000000000000000
    c = x & 0b01111111111000000000000000000000
    d = x & 0b10000000000000000000000000000000
    b <<= 11
    c >>= 5
    d >>= 16
    return a | b | c | d


print(hex(f22(0x473a7775)))
