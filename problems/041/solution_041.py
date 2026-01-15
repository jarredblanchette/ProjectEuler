# We shall say that an n-digit number is pandigital if it makes use of all the digits
# 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
#
# What is the largest n-digit pandigital prime that exists?
from sympy import isprime
from itertools import permutations
from functools import reduce

if __name__ == '__main__':
    size = 9
    result = 0

    # taking advantage of permutations's ordering of results.
    # We are using a reversed range (ie, [size, size-1 ... 1]) so we start with the largest value
    while not result or size == 0:
        candidates = [reduce(lambda a, b: a * 10 + b, candidate) for candidate in permutations(range(size, 0, -1), size)
                      if candidate[-1] in [1, 3, 7]]

        for candidate in candidates:
            if isprime(candidate):
                result = candidate
                break

        size -= 1

    print(result)
