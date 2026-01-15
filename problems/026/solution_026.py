from sympy.ntheory.factor_ import primefactors
from functools import reduce


def p(d: int) -> int:
    while 2 in primefactors(d):
        d = d / 2

    while 5 in primefactors(d):
        d = d / 5

    d = int(d)

    # TODO: This can be improved by more careful consideration of the candidates, look into Carmichael reduced totient
    for n in range(1, d):
        if pow(10, n) % d == 1:
            return n
        if pow(10, n) % d == -1:
            return n*2

    return -1


if __name__ == '__main__':
    periods = [(i, i) for i in range(0, 1000)]
    periods = [(i, p(j)) for i, j in periods[1:]]
    print(reduce(lambda a, b: a if a[1] > b[1] else b, periods))
