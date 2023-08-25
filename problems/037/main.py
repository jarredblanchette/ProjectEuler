# The number 3797 has an interesting property.
# Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage:
# 3797,
# 797,
# 97,
# and 7.
# Similarly we can work from right to left:
# 3797,
# 379,
# 37,
# and 3.
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
from sympy import prime, sieve
from functools import cache, reduce
from itertools import product

@cache
def get_truncated(n: int) -> set[int]:
    acc: set[int] = set()

    stringN = str(n)

    for i in range(0, len(stringN)):
        lhs = (stringN[:i].lstrip('0'))
        rhs = (stringN[i:].lstrip('0'))

        if lhs != '':
            lhs = int(lhs)
            acc.add(lhs)
        if rhs != '':
            rhs = int(rhs)
            acc.add(rhs)

    return acc


def candidate_generator():
    body_digits = (1,3,7,9)
    head_digits = range(1,10)

    def generate_candidate():
        digits = 1
        while True:
            items = product(body_digits, repeat=digits)
            for item in items:
                root_value = reduce(lambda x,y: x*10 + y, item)

                # req because we can start with non-body digits but not have them elsewhere.
                for head in head_digits:
                    value = root_value + pow(10,digits) * head
                    if value in sieve:
                        yield value
            digits += 1

    return generate_candidate()


def trunkatable_prime(candidate:int) -> bool:
    children = get_truncated(candidate)
    if all([child in sieve for child in children]):
        return True
    return False


if __name__ == '__main__':
    primes = set()

    gen = candidate_generator()
    while len(primes) < 11:
        candidate = next(gen)
        if trunkatable_prime(candidate):
            primes.add(candidate)

    print(primes, sum(primes))

