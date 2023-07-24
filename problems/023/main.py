# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example,
# the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number. A
# number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum
# exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum
# of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can
# be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis
# even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is
# less than this limit. Find the sum of all the positive integers which cannot be written as the sum of two abundant
# numbers.
from functools import cache
from itertools import product


@cache
def properFactors(n: int) -> list[int]:
    pf: list[int] = []
    for i in range(1, n):
        if n % i == 0:
            pf.append(i)

    return pf


def perfection(n: int) -> int:
    """Given n, returns if that number is deficient (-ve), perfect (0), or abundant (+ve)"""
    return sum(properFactors(n)) - n


if __name__ == '__main__':
    MAGIC = 28123

    abundant = [i for i in range(0, MAGIC) if perfection(i) > 0]
    print(abundant)

    sums = {sum(i) for i in product(abundant, repeat=2)}

    print(sum([i for i in range(0, MAGIC) if i not in sums]))
