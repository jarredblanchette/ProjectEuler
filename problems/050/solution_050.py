# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13.
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most consecutive primes?
from typing import List
from sympy import sieve, primerange, prime

# This is an obvious candidate for @cache, but we don't actually call it with the same values ever so there's no point
def prime_sum(i: int, j: int) -> int:
    """Returns the sum of the primes between the ith and jth prime"""

    if i <= 0:
        raise Exception("i must be greater than 0")
    if j <= 0:
        raise Exception("j must be greater than 0")
    if j < i:
        raise Exception("j must be more than i")

    # We could use sum(list(primerange(prime(i),prime(j))),
    # but I believe this won't require us to instantiate the whole range from prime(i) to prime(j).
    # So it should be faster if j >> i
    acc = 0
    for p in primerange(prime(i), prime(j)):
        acc += p
    return acc


if __name__ == '__main__':
    ONE_MILLION = 1000000

    max_prime_index = sieve.search(ONE_MILLION)[0]

    best_run_length = -1
    best_value = -1

    for start in range(1, max_prime_index):
        run_length = 1
        candidate_sum = prime_sum(start, start + run_length)
        while candidate_sum < ONE_MILLION:
            if run_length > best_run_length and candidate_sum in sieve:
                best_run_length = run_length
                best_value = candidate_sum
            run_length += 1
            candidate_sum = prime_sum(start, start + run_length)

    print(best_value, best_run_length)
