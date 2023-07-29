# The fraction 49/98 is a curious fraction,
# as an inexperienced mathematician, in attempting to simplify it, may incorrectly believe that
# 49/98 = 4/9 which is correct, is obtained by cancelling the 9s.
#
# We shall consider fractions like,
#     30/50 = 3/5
# to be trivial examples.
#
# There are exactly four non-trivial examples of this type of fraction,
# less than one in value, and containing two digits in the numerator and denominator.
#
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
from fractions import Fraction
from functools import reduce

def badSimplify(numerator: int, denominator: int) -> list[Fraction]:
    if numerator %10 == 0 or denominator % 10 == 0: return []

    numerator = str(numerator)
    denominator = str(denominator)
    acc = []

    if numerator[0] == denominator[0]:
        candidate = (int(numerator[1]), int(denominator[1]))
        if candidate not in acc:
            acc.append(candidate)

    if numerator[1] == denominator[0]:
        candidate = (int(numerator[0]), int(denominator[1]))
        if candidate not in acc:
            acc.append(candidate)

    if numerator[0] == denominator[1]:
        candidate = (int(numerator[1]), int(denominator[0]))
        if candidate not in acc:
            acc.append(candidate)

    if numerator[1] == denominator[1]:
        candidate = (int(numerator[0]), int(denominator[0]))
        if candidate not in acc:
            acc.append(candidate)

    return acc


if __name__ == '__main__':
    acc = []
    for n in range(11, 100):
        for d in range(n, 100):
            if n == d: continue
            BS = badSimplify(n, d)
            for badFraction in BS:
                if Fraction(badFraction[0], badFraction[1]) == Fraction(n, d):
                    acc.append((n,d))

    # visual inspection of the result shows we have a floating point error, but the result is 0.01 ... 2,
    # which I interpret as 1/100
    print(reduce((lambda a,b:a*b) , [n/d for (n,d) in acc]))

