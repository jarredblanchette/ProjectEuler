# An irrational decimal fraction is created by concatenating the positive integers:
# 0.123456789101112131415161718192021...
#              ^
# It can be seen that the 12th digit of the fractional part is 1.
# If d_n represents the nth digit of the fractional part, find the value of the following expression.
# d_1 * d_10 * d_100 * d_1000 * d_10000 * d_100000 * d_1000000
from functools import reduce


def dumb_generator():
    s = ''
    f = 1

    def dumb(n:int):
        nonlocal s,f
        while n > len(s):
            s += str(f)
            f += 1
        print(len(s))
        return int(s[n-1])

    return dumb


if __name__ == '__main__':
    dg = dumb_generator()

    targets = [pow(10,t) for t in range(0, 7)]

    res = [dg(target) for target in targets]

    print(res, reduce(lambda a,b:a*b,res))