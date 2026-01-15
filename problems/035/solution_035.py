# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?
# https://projecteuler.net/problem=35

from functools import reduce
from sympy import sieve

def rotate(n: int) -> list[int]:
    acc = []
    ln = [int(i) for i in str(n)]
    for i in range(len(ln)):
        acc.append(reduce(lambda a,b: a * 10 + b, ln[i:] + ln[:i]))
    return acc


if __name__ == '__main__':
    OneMillion = 1000000

    circularPrimes = []

    for candidate in sieve.primerange(OneMillion):
        if candidate in sieve and candidate not in circularPrimes:
            rotations = rotate(candidate)
            if all([rotation in sieve for rotation in rotations]):
                [circularPrimes.append(rotation) for rotation in rotations if rotation not in circularPrimes]

    print(circularPrimes,len(circularPrimes))