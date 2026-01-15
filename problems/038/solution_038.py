# Take the number 192 and multiply it by each of 1, 2, and 3:
#
# 192 * 1 = 192
# 192 * 2 = 384
# 192 * 3 = 576
#
# By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3).
# The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).
# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ..., n) where n > 1?
from functools import reduce
from itertools import permutations


def pandigitial(n: int) -> bool:
    """takes an integer and returns if it contains each digit (1,2,3 ... 9) exactly once"""
    if len(str(n)) != 9:
        return False

    return all([str(i) in str(n) for i in range(1, 10)])


def stepwise_multiply(n: int, i: int):
    """Takes a number and a degree, and returns the concatinated product of the number times the (1,2, ... degree)"""
    acc = 0
    for k in range(1, i + 1):
        res = n * k
        acc = pow(10, len(str(res))) * acc + res
    return acc


def pandigital_degree(n: int) -> int:
    """Returns the maximum i such that n*1 concat n*2 concat n*3 concat ... n*i is pandigital, or -1 if no such value of i"""
    for degree in range(9, 0, -1):
        if (pandigitial(stepwise_multiply(n, degree))):
            return degree
    return -1


def check_candidate(candidate: int) -> int:
    """Takes a candidate pandigital number, and returns the largest n that we can have a concatenated  product, or -1 if no such value exists"""
    for head_length in range(1, 5):
        head = int(str(candidate)[:head_length])
        degree = pandigital_degree(head)
        if degree > 1 and stepwise_multiply(head, degree) == candidate:
            return degree
    return -1


if __name__ == '__main__':
    # for all pandigitials, start with the biggest and check each.
    solution = -1

    for candidate_tuple in permutations(range(9, 0, -1), 9):
        candidate = reduce(lambda x, y: x * 10 + y, candidate_tuple)
        if check_candidate(candidate) > 1:
            solution = candidate
            break

    print(solution)
