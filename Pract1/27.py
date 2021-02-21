import math


def f11(x, y, z):
    res1 = math.pow(math.fabs(z) - math.sin(y), 7)/42
    res2 = 52 * math.pow(y, 2)
    res3 = (math.pow(y, 7) - math.pow(x, 6)/44)/(49*math.pow(z, 6) + x)
    res4 = (math.exp(x) + 46 * math.pow(y, 3))/(math.cos(z) + 51*math.pow(z, 4) - 81)
    return res1 + res2 + res3 + res4


def f12(x):
    if x < 46:
        return math.pow(math.fabs(x) - math.sin(x), 7)/42 + 52 * math.pow(x, 2)
    elif x < 95:
        return math.pow(x, 7) - math.pow(x, 4)/44 + 69
    elif x < 184:
        return 49 * math.pow(math.pow(x, 5)/90 - math.exp(x), 6) + math.cos(x)
    elif x < 207:
        return (x - math.pow(x, 5))/87 - math.pow(x, 6)
    else:
        return 6 * (math.pow(x, 2) - math.pow(x, 7)/70 - 52) - 49 * math.pow(x, 5)


def f13(n, m):
    sum1 = 0
    sum2 = 0
    for i in range(1, n + 1):
        sum1 += math.pow(i, 7)/28 + math.cos(i)
        for j in range(1, m + 1):
            sum2 += math.exp(i) - 93 * math.pow(i, 4)
    return sum1 - 97 * sum2


def f14(n):
    if n == 0:
        return 8
    elif n == 1:
        return 9
    else:
        return math.tan(f14(n - 2)) + math.fabs(f14(n - 2)) - 31
