from functools import cache
from itertools import permutations


@cache
def isPandigital(n: int) -> bool:
    n = str(n)
    # Currently supports only len(n) in 1,9
    if(len(n) != 9): return False
    return all([str(d) in n for d in range(1, len(n) + 1)])


def pandigHelper(l: list[int]) -> bool:
    if len(l) == 0:
        return False
    acc = 0
    for element in l:
        acc *= pow(10, len(str(element)))
        acc += element
    return isPandigital(acc)


@cache
def remainingDigits(n:int )-> int:
    """returns the number of free digits we have, for the purpose of a pandigit"""
    return len([d for d in range(1,10) if str(d) not in str(n)])

@cache
def anySharedDigit(left: int, right: int) -> bool:
    left, right = str(left), str(right)

    # ensure left is longer than right
    if len(left) < len(right):
        left, right = right, left

    for character in left:
        if character in right:
            return True
    return False


if __name__ == '__main__':

    multiplicands: set = set()
    for length in range(2, 5):
        str_c = [[str(k) for k in j] for j in (permutations(range(10), length))]
        [multiplicands.add(int(''.join(i).lstrip('0'))) for i in str_c ]


    acc = set()

    # Key insight is that x * y = z
    # ST len(z) >= max(len(x) , len(y))
    # for x,y,z E N
    # so we can exclude ALL multiplands ST they consume more than 50%-1 of the avalible digits (ie, any with length >3)
    # example, suppose we have a multipland with len 4.  The minimal multiplier is len(1).
    # any len(4) x any len(1) yields >=len(4), and 4+1+4 >=9 ,
    # therefore we should only consider multiplands at most 3 digits long
    for multiplicand in multiplicands:
        multipliers = {i for i in multiplicands if not anySharedDigit(i, multiplicand) and len(str(i)) + len(str(multiplicand)) <= 5 and i < multiplicand}
        for multiplier in multipliers:
            product = multiplicand * multiplier
            if product not in acc and pandigHelper([product, multiplicand, multiplier]):
                acc.add(product)

    print(acc,sum(acc))
