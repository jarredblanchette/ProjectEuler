# The decimal number,
# 585 = 1001001001 (binary),
# is palindromic in both bases.
#
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
#
# (Please note that the palindromic number, in either base, may not include leading zeros.)
from functools import cache


@cache
def palendromic(candidate: str) -> bool:
    # This can trivially, and better, be acheived by just doing a scan and comparing n to len-n
    # but This amuses me
    # base cases, len 1 or 2
    if len(candidate) == 1:
        return True
    if len(candidate) == 2:
        return candidate[0] == candidate[1]

    if candidate[0] == candidate[-1]:
        return palendromic(candidate[1:-1])

    return False


def to_bin(n: int) -> str:
    if n == 0: return '0'
    acc = ''
    while n > 0:
        if n % 2 == 1:
            acc = '1' + acc
            n = (n - 1) / 2
        else:
            acc = '0' + acc
            n /= 2
    return acc


if __name__ == '__main__':
    OneMillion = 1000000
    acc = [n for n in range(1, OneMillion) if palendromic(str(n)) and palendromic(to_bin(n))]
    print(sum(acc))
