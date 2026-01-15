# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values:
# 13, 23, 43, 53, 73, and 83,
# are all prime.
#
# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers,
# yielding the family:
# 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
# Consequently 56003, being the first member of this family, is the smallest prime with this property.
#
# Find the smallest prime which, by replacing part of the number
# (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
from functools import reduce
from itertools import combinations
from sympy import sieve, prime


def family_generator(parent: int, replacement_indexs: list[int]) -> list[int]:
    string_parent = [str(parent)[i] for i in range(len(str(parent)))]

    acc: list[int] = []
    starting_index = 0
    if 0 in replacement_indexs:
        starting_index = 1

    for replacementCharacter in range(starting_index, 10):
        candidate: list[str] = string_parent
        for replacementIndex in replacement_indexs:
            candidate[replacementIndex] = replacementCharacter
        acc.append(reduce(lambda a, b: a * 10 + b, [int(c) for c in candidate]))

    return acc


def get_extended_family(parent: int) -> list[list[int]]:
    """for an input parent, derive the children we have.  Returns a list of the branches of the family, where each branch have had the same digits replaced"""
    acc = []
    parentLength = len(str(parent))
    # ie, replace between 1 and len(parent)-1 digits
    for numReplacements in range(1, parentLength):
        # select all the different combinations of digits we can replace
        digitsForReplacement = combinations(range(0, parentLength), numReplacements)
        for replacements in digitsForReplacement:
            children = family_generator(parent, [i for i in replacements])
            acc.append(children)
    return acc


def family_size(family: list[int]) -> int:
    return len([member for member in family if member in sieve])


if __name__ == '__main__':
    start = 103
    n = 5
    candidate = prime(n)
    while max([family_size(family) for family in get_extended_family(candidate)]) < 8:
        n += 1
        candidate = prime(n)

    candidateFamily = [(family_size(f), f) for f in get_extended_family(candidate)]
    best = max([size for size, family in candidateFamily])
    bestFamily = candidateFamily[[size for size, family in candidateFamily].index(best)][1]
    print(min(bestFamily))
