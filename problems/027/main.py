from sympy.ntheory import isprime
from sympy import sieve
from functools import reduce


def evaluate(a: int, b: int) -> int:
    n = 0
    while isprime(n * n + a * n + b):
        n += 1
    return n


if __name__ == '__main__':
    # So we know that b must be prime
    # because, for
    # n**2 + an + b
    # ST n == 0,
    # if b is not prime, no prime, so we instantly failout
    results = ([(a, b, evaluate(a, b)) for a in range(-999, 1000) for b in sieve.primerange(0, 1000)])
    best = (reduce(lambda a, b: a if a[2] > b[2] else b, results))

    print(best, best[0] * best[1])
